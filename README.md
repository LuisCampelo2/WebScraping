# WebScraping
 # **Automação e Coleta de Dados com Selenium e BeautifulSoup**

Este projeto é um script em Python que utiliza **Selenium** e **BeautifulSoup** para acessar páginas da web, coletar informações específicas (imagens, links ou textos) e salvá-las em um arquivo JSON. Ideal para demonstração de habilidades em automação e raspagem de dados.

---

## **Funcionalidades**
- **Coleta Dinâmica de Dados**: Permite escolher o que coletar (imagens, links ou textos).
- **Interatividade**: O usuário define a quantidade de itens a serem coletados.
- **Armazenamento Estruturado**: Os dados são salvos em um arquivo JSON na pasta `data/`.
- **Automação de Navegador**: Utiliza o Selenium para acessar páginas dinâmicas.

---

## **Tecnologias Utilizadas**
- **Python**: Linguagem de programação principal.
- **Selenium**: Automação do navegador para acessar páginas.
- **BeautifulSoup**: Raspagem de dados do HTML da página.
- **WebDriver Manager**: Gerenciamento automático do driver do navegador Chrome.
- **JSON**: Para armazenamento dos dados coletados.

---

## **Requisitos**
Certifique-se de ter os seguintes itens instalados:
- **Python 3.9+**
- **Google Chrome**
- **Bibliotecas Python**:
  - `selenium`
  - `webdriver-manager`
  - `beautifulsoup4`

Você pode instalar as dependências com:
```bash
pip install selenium webdriver-manager beautifulsoup4

## **Como Usar**
1. **Clone o Repositório**:
   Primeiro, clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/LuisCampelo2/WebScraping
   cd WebScraping
Instale as Dependências: Basta digitar no terminal: pip install -r requirements.txt

Informe a URL: O programa pedirá a URL da página que você deseja acessar.
Escolha o Tipo de Dado: Você poderá escolher o que deseja coletar:
Digite 1 para imagens.
Digite 2 para links.
Digite 3 para textos.
Defina o Limite: Insira o número de itens a serem coletados.
Resultado:

Após a coleta, os dados serão salvos em um arquivo JSON na pasta data/.
O arquivo será chamado output.json.

