from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

"""
Este script utiliza Selenium e BeautifulSoup para acessar uma página da web,
coletar dados (imagens, links ou textos) e exibi-los de forma interativa.
Ideal para demonstração de habilidades em automação e web scraping.
"""


# Funçao para inicializar o navegador Chrome com as opções fornecidas 
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """Inicializa o navegador Chrome com as opções especificadas."""
    chrome_options = webdriver.ChromeOptions()

    # Adiciona opções de configuração, se existirem
    if options:
        for option in options:
            chrome_options.add_argument(option)

    # Configura o driver usando o WebDriverManager
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

# Função para definir o que sera coletado da página
def switch_elements(soup: BeautifulSoup):
    """Exibe e coleta dados da página de acordo com a escolha do usuário."""
    continuar = 's'
    resultados={}
    while continuar == 's':
        limit = input('Qual quantidade voce quer que seja coletada de itens') # Limite de elementos exibidos 
        # Validação da entrada do usuário
        try:
            limit=int(limit)   
        except ValueError:
            print('valor digitado tem que ser um valor inteiro')
            continue
        #   Definindo o que será coletado
        element = input('Escolha o que você quer coletar da página:\n'
                        '1. Para coletar imagens, digite 1\n'
                        '2. Para coletar links, digite 2\n'
                        '3. Para coletar textos, digite 3\n')

        # Validação da entrada do usuário
        try:
            element = int(element)
        except ValueError:
            print("Opção inválida! Por favor, insira um número entre 1 e 3.")
            continue

        # Realiza a coleta com base na escolha do usuário
        match element:
            case 1:  # Coletar imagens
                imagens = soup.find_all('img', src=True)
                if imagens:
                    print(f"Foram encontradas {len(imagens)} imagens. Exibindo as {min(limit, len(imagens))} primeiras:\n")
                    for i, imagem in enumerate(imagens[:limit], 1):
                        print(f"{i}. URL: {imagem['src']}")
                    resultados['imagens'] = [
                        imagem['src'] for imagem in imagens[:limit]
                    ]
                else:
                    print('Nenhuma imagem encontrada no site.')
            case 2:  # Coletar links
                links = soup.find_all('a', href=True)
                if links:
                    print(f"Foram encontrados {len(links)} links. Exibindo os {min(limit, len(links))} primeiros:\n")
                    for i, link in enumerate(links[:limit], 1):
                        print(f"{i}. URL: {link['href']}")
                    resultados['links'] = [
                        link['href'] for link in links[:limit]
                    ]
                else:
                    print('Nenhum link encontrado no site.')
            case 3:  # Coletar textos
                textos = soup.find_all('p')
                if textos:
                    print(f"Foram encontrados {len(textos)} parágrafos de texto. Exibindo os {min(limit, len(textos))} primeiros:\n")
                    for i, texto in enumerate(textos[:limit], 1):
                        print(f"{i}. Texto: {texto.get_text(strip=True)}")
                    resultados['textos'] = [
                        texto.get_text(strip=True) for texto in textos[:limit]
                    ]
                else:
                    print('Nenhum texto encontrado no site.')
            case _:  # Opção inválida
                print("Opção inválida! Por favor, insira um número entre 1 e 3.")

        continuar = input('Quer continuar? (s/n): ').strip().lower()
    # Salva os resultados em um arquivo JSON
    with open('data/output.json', 'w', encoding='utf-8') as json_file:
        json.dump(resultados, json_file, indent=4, ensure_ascii=False)
        print("\nOs dados coletados foram salvos no arquivo 'output.json' na pasta Data.")

def main():
    # Configuração inicial
    url = input('Informe a URL do site: ')

    # Opções para o navegador
    options = '--disable-gpu',
    browser = make_chrome_browser(*options)

    try:
        # Acessar a página desejada
        browser.get(url)
        print(f"\nTítulo da página: {browser.title}")

        # Pausa para garantir o carregamento
        sleep(3)

        # Processar o HTML com BeautifulSoup
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Chamar a função para escolher elementos
        switch_elements(soup)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fechar o navegador
        browser.quit()

if __name__ == '__main__':
    main()




