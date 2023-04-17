## Notícias no prompt

Um buscador de notícias para utilizar no prompt de comando e automatizar suas buscas

### Ferramentas

- python: https://www.python.org
- newsapi: https://newsapi.org

### Uso

Crie uma chave de api no site da [newsapi](https://newsapi.org) e substitua a variável API_KEY no arquivo app.py.
Depois tenha em mente uma categoria e um país para filtrar as notícias.

Categorias disponíveis na newsapi:

- business
- entertainment
- general
- health
- science
- sports
- technology

Para os países, pode ser usado o codigo 2-letter ISO 3166-1, por exemplo:

- Brasil (br)
- Estados Unidos (us)


Insira o seguinte comando no terminal do diretório:

```python app.py <categoria> <país>```

ou 

```python app.py```

O segundo comando possui o Brasil como país padrão e todas as categorias selecionadas

