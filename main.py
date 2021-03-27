from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

NIKE_SNEAKERS = 'https://www.nike.com.br/Snkrs/#feed'

# Creates webDriver and manage browser version
driver = webdriver.Chrome(ChromeDriverManager().install())

# Opens website
driver.get(NIKE_SNEAKERS)