from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


with open('dados.json', 'r') as json_file:
    dados = json.load(json_file)

for dado in dados:

    driver=webdriver.Firefox()
    driver.get('https://unidade1.pizzasportello.com.br/cadastrar/')
    ele=driver.find_element_by_xpath('//*[@id="nomecompleto"]')
    ele.click()
    ele.send_keys(dado["nome"])

    ele=driver.find_element_by_xpath('//*[@id="datanascimento"]')
    ele.click()
    ele.send_keys(dado["nasc"])

    ele=driver.find_element_by_xpath('//*[@id="sexo"]')
    ele.click()
    ele.send_keys(dado["sexo"])
    ele.send_keys(Keys.RETURN)

    ele=driver.find_element_by_xpath('//*[@id="cpf"]')
    ele.click()
    ele.send_keys(dado["cpf"])

    ele=driver.find_element_by_xpath('//*[@id="telefone1"]')
    ele.click()
    ele.send_keys(dado["fone"])

    ele=driver.find_element_by_xpath('//*[@id="telefone2"]')
    ele.click()
    ele.send_keys(dado["cel"])

    ele=driver.find_element_by_xpath('//*[@id="email"]')
    ele.click()
    ele.send_keys(dado["mail"])

    ele=driver.find_element_by_xpath('//*[@id="senha"]')
    ele.click()
    ele.send_keys(dado["pwd"])

    ele=driver.find_element_by_xpath('//*[@id="confirm-senha"]')
    ele.click()
    ele.send_keys(dado["pwd"])

    ele=driver.find_element_by_xpath('//*[@id="cidade"]')
    ele.click()
    ele.send_keys(dado["city"])
    ele.send_keys(Keys.RETURN)

    ele=driver.find_element_by_xpath('//*[@id="logradouro"]')
    ele.click()
    ele.send_keys(dado["street"])

    ele=driver.find_element_by_xpath('//*[@id="numero"]')
    ele.click()
    ele.send_keys(dado["n_res"])

    ele=driver.find_element_by_xpath('//*[@id="complemento"]')
    ele.click()
    ele.send_keys(dado["comp"])

    ele=driver.find_element_by_xpath('//*[@id="bairro"]')
    ele.click()
    ele.send_keys(dado["bairro"])
    ele.send_keys(Keys.TAB)

    ele=driver.find_element_by_xpath('//*[@id="cadastrarcliente"]')
    #ele.click()

    #sleep(2)
