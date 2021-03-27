import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

NIKE_SNEAKERS = 'https://www.nike.com.br/Snkrs/#feed'

# Creates webDriver and manage browser version
driver = webdriver.Chrome(ChromeDriverManager().install())

# Opens website
driver.get(NIKE_SNEAKERS)

# Get list of products
listOfProducts = driver.find_elements_by_xpath('//*[@id="DadosPaginacaoFeed"]/div/div')
cont = 0

for product in listOfProducts :
  className = product.get_attribute("class")
  if 'esgotado' in className :
    productData = product.find_element_by_xpath(f'//*[@id="DadosPaginacaoFeed"]/div/div[{cont}]/div/a/img')
    productName, productCode = productData.get_attribute('alt').split(' - Cód.')

    print(productName,' - ',productCode)
  cont+=1