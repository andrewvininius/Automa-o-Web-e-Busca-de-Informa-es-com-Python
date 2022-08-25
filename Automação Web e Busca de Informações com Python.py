pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#passo 1: pegar cotaçao do dola
# abrir o navegador
navegador = webdriver.Chrome()

#entrar no google
navegador.get("https://www.google.com.br/")

#pesquisar cotaçao do google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotaçao do dolar")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#pegar a cotaçao
cotaçao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotaçao_dolar)

#passo 2: pegar cotaçao do euro
navegador.get("https://www.google.com.br/")
#pesquisar cotaçao do google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotaçao do euro")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#pegar a cotaçao
cotaçao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotaçao_euro)

#passo 3: pegar cotaçao do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotaçao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotaçao_ouro = cotaçao_ouro.replace(',','.') 
print(cotaçao_ouro)

navegador.quit()

#passo 4: atualizar a base de dados
import pandas as pd
tabela = pd.read_excel(r"C:\Users\rapha\Downloads\Produtos.xlsx")
display(tabela)

#passo 5:recalcular o preços

#atualizar as cotacoes

tabela.loc[tabela["Moeda"] == "dolar", "Cotação"] = float(cotaçao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotaçao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotaçao_ouro)

#preço de compra =preço original * cotaçao
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]


#preço de venda = preço de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

display(tabela)

tabela.to_excel("Produtos novos.xlsx", index=False)