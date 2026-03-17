# News Scraper

Um web scraper simples em Python que extrai notícias do Hacker News e guarda os resultados num ficheiro CSV.

---

## Funcionalidades

- Extrai títulos, links e pontuações das notícias
- Trata erros de rede automaticamente
- Guarda os resultados num ficheiro CSV com data e hora
- Fácil de adaptar para outros sites

---

## Requisitos

- Python 3.x
- requests
- beautifulsoup4

---

## Instalação

1. Clona ou descarrega o projeto:

```
git clone https://github.com/teu-utilizador/news-scraper
cd news-scraper
```

2. Instala as dependências:

```
python -m pip install requests beautifulsoup4
```

---

## Utilização

Corre o script diretamente:

```
python scraper.py
```

O programa vai:
1. Aceder ao Hacker News
2. Extrair as notícias da página principal
3. Mostrar as primeiras 5 no terminal
4. Guardar todas num ficheiro `noticias.csv`

### Exemplo de output

```
A fazer scraping...
1. Show HN: I built a Python tool to... (42 points)
2. Ask HN: What's the best way to... (87 points)
3. New research on AI alignment (134 points)
...
Guardadas 30 notícias em 'noticias.csv'
```

---

## Estrutura do projeto

```
news-scraper/
├── scraper.py       # Script principal
├── noticias.csv     # Ficheiro gerado após correr o script
└── README.md        # Este ficheiro
```

---

## Como funciona

1. **requests** faz o pedido HTTP e descarrega o HTML da página
2. **BeautifulSoup** analisa o HTML e permite navegar pela sua estrutura
3. `.find_all()` encontra todos os elementos com a classe CSS pretendida
4. Os dados são guardados num dicionário e exportados para CSV

---

## Adaptar para outros sites

Para usar noutro site, abre as DevTools do browser (F12), inspeciona o elemento que queres extrair, e substitui a classe CSS no código:

```python
# Exemplo: mudar de Hacker News para outro site
titulos = soup.find_all("h2", class_="nome-da-classe-do-site")
```

---

## Tecnologias usadas

- [Python](https://www.python.org/)
- [requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

---

## Licença

MIT — podes usar, modificar e distribuir livremente.
