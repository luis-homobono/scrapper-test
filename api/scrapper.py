# import httpx
from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# import json

url = 'https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas'
session = HTMLSession()

response = session.get(url=url)

response.html.render(keep_page=True)

breakpoint()

# response = httpx.get(url=url)
# import urllib.request

# get = urllib.request.urlopen("https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas")
# html = get.read()

# with open('enlatados.html', '+w', encoding="utf-8") as file:
#     file.write(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')
# data_template = soup.find('template', attrs={'data-varname': '__STATE__'})

# script_data = data_template.find('script')
# data = json.loads(script_data.text)