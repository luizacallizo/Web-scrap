import urllib.request
import bs4 as bs

def mercado(produto,m):

    url = "https://lista.mercadolivre.com.br/{}".format(produto)
    print("Acessando o site...")
    pagina = urllib.request.urlopen(url)
    #pegando o codigo da pagina
    codigo_pagina= bs.BeautifulSoup(pagina, features="html.parser")

    print("Pesquisando produtos...")

    itens = codigo_pagina.find_all('span', attrs={'class':'price__fraction'})
    links = codigo_pagina.find_all('a', attrs={'class':'item__info-title'})

    menor=m
    volta=0
    posicao=0

    for i in itens:
        for i in itens:
            valor = float(i.text.strip().replace('.', ""))
            if valor < menor:
                menor = valor
                posicao = volta
            volta = volta + 1

    print(menor)
    print(posicao)
    print(links[posicao].get('href'))

if __name__=="__main__":
    mercado()

