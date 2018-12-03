nome = 'nome'
numero = '+55 11 94463-4178'
pedido =' Olá, nome seu pedido é P123456 \n total de R$ 12,90  \n 1 chocolate  \n 1 misto \n Volte sempre \n '

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

time.sleep(3)
pesquisar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
pesquisar.click()
pesquisar.send_keys(numero)
time.sleep(2)


#import
from selenium.webdriver.common.keys import Keys

pesquisar.send_keys(Keys.ENTER)

time.sleep(3)


escrever = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
escrever.click()
escrever.send_keys(pedido)

sair=input('sair')
