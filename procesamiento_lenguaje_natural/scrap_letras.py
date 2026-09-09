"""Baja las letras de Las Pastillas del Abuelo desde letras.com y arma el corpus.

Deja un verso por linea en dataset/pastillas_del_abuelo.txt (mismo formato que
songs_dataset/beatles.txt de la clase) y un dataset/canciones.csv con lo que entro.
"""
import csv
import random
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ARTISTA = "las-pastillas-del-abuelo"
BASE = "https://www.letras.com"
CARPETA = Path(__file__).parent / "dataset"
SALIDA = CARPETA / "pastillas_del_abuelo.txt"
LISTADO = CARPETA / "canciones.csv"

# headers de un chrome real en macos, para que el sitio no corte los pedidos
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
    "Referer": f"{BASE}/{ARTISTA}/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def pedir(session, url):
    """GET con pausa aleatoria y un reintento si el sitio devuelve 429 o 5xx."""
    time.sleep(random.uniform(1, 2.5))
    for intento in range(2):
        r = session.get(url, timeout=30)
        if r.status_code == 429 or r.status_code >= 500:
            print(f"  {r.status_code} en {url}, espero 30s")
            time.sleep(30)
            continue
        r.raise_for_status()
        return r.text
    return None


def titulo_base(titulo):
    """Titulo sin la version entre parentesis, en minuscula, para colapsar duplicados."""
    return re.sub(r"\s*\(.*?\)\s*$", "", titulo).strip().lower()


def listar_canciones(session):
    """Dict titulo -> href con una sola version por cancion."""
    soup = BeautifulSoup(pedir(session, f"{BASE}/{ARTISTA}/"), "html.parser")
    # las canciones son /artista/slug/, los links de navegacion terminan en .html
    es_cancion = re.compile(rf"^/{ARTISTA}/[^/]+/$")
    canciones, vistos = {}, set()
    for a in soup.select(f'a[href^="/{ARTISTA}/"]'):
        titulo = a.get_text(" ", strip=True)
        href = a["href"]
        if not titulo or not es_cancion.match(href) or href in vistos:
            continue
        vistos.add(href)
        canciones.setdefault(titulo_base(titulo), (titulo, href))
    return canciones


def bajar_letra(session, href):
    """Lista de versos de una cancion, uno por <br> dentro de div.lyric-original."""
    html = pedir(session, BASE + href)
    if html is None:
        return []
    div = BeautifulSoup(html, "html.parser").select_one("div.lyric-original")
    if div is None:
        return []
    versos = []
    for p in div.find_all("p"):
        versos += [v.strip() for v in p.get_text("\n").split("\n") if v.strip()]
    return versos


def main():
    CARPETA.mkdir(exist_ok=True)
    session = requests.Session()
    session.headers.update(HEADERS)

    canciones = listar_canciones(session)
    print(f"Canciones encontradas: {len(canciones)}")

    corpus, filas = [], []
    for i, (titulo, href) in enumerate(canciones.values(), 1):
        versos = bajar_letra(session, href)
        print(f"[{i}/{len(canciones)}] {titulo}: {len(versos)} versos")
        if not versos:
            continue
        corpus += versos
        filas.append({"titulo": titulo, "url": BASE + href, "versos": len(versos)})

    SALIDA.write_text("\n".join(corpus) + "\n", encoding="utf-8")
    with LISTADO.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["titulo", "url", "versos"])
        w.writeheader()
        w.writerows(filas)

    print(f"\nCanciones bajadas: {len(filas)}")
    print(f"Versos totales: {len(corpus)}")
    assert len(corpus) > 1000, "corpus demasiado chico"


if __name__ == "__main__":
    main()
