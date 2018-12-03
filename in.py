login = 'developerbreno@gmail.com'
senha = '257breno'
pedido ='desenvolvimento de sistemas'

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')

#import
from selenium.webdriver.common.keys import Keys



time.sleep(1)






escrever = driver.find_element_by_xpath('//*[@id="login-email"]')
escrever.send_keys(login)



escrever = driver.find_element_by_xpath('//*[@id="login-password"]')
escrever.send_keys(senha)


escrever = driver.find_element_by_xpath('//*[@id="login-submit"]')

escrever.click()


time.sleep(1)

escrever = driver.find_element_by_xpath('//*[@id="ember41"]/input')
escrever.send_keys(pedido)


escrever.send_keys(Keys.ENTER)

time.sleep(1)


driver.get('https://www.linkedin.com/search/results/people/?keywords=desenvolvimento%20de%20sistemas&origin=CLUSTER_EXPANSION')




escrever = driver.find_element_by_xpath('//*[@id="ember3495"]/button')

escrever.click()












escrever = driver.find_element_by_link_text("Conectar")

escrever.send_keys(Keys.ENTER)








sair=input('sair')
