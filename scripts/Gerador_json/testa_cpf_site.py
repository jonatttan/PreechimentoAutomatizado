from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


with open('lista_cpf.json', 'r') as json_file:
    clientes = json.load(json_file)

for cliente in clientes:

    driver=webdriver.Firefox()
    driver.get('https://www.geradordecpf.org/')
    campo = driver.find_element_by_xpath('//*[@id="numero"]')
    campo.click()
    campo.send_keys(cliente["cpf"])
    campo = driver.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/div[1]/input')
    campo.click()