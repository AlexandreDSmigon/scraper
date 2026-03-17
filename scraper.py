import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

URL = "https://news.ycombinator.com/"

def scrape_noticias():
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()  # Lança erro se o site falhar
    except requests.RequestException as e:
        print(f"Erro ao aceder ao site: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    noticias = []
    titulos = soup.find_all("span", class_="titleline")
    pontos = soup.find_all("span", class_="score")

    for i, item in enumerate(titulos):
        link_tag = item.find("a")
        titulo = link_tag.text
        url = link_tag.get("href", "")
        votos = pontos[i].text if i < len(pontos) else "0 points"

        noticias.append({
            "titulo": titulo,
            "url": url,
            "votos": votos,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    return noticias

def guardar_csv(noticias, ficheiro="noticias.csv"):
    with open(ficheiro, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["titulo", "url", "votos", "data"])
        writer.writeheader()
        writer.writerows(noticias)
    print(f"Guardadas {len(noticias)} notícias em '{ficheiro}'")

if __name__ == "__main__":
    print("A fazer scraping...")
    noticias = scrape_noticias()

    if noticias:
        for i, n in enumerate(noticias[:5], 1):
            print(f"{i}. {n['titulo']} ({n['votos']})")
        guardar_csv(noticias)