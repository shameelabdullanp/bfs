from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600)) # Virtual display for Web driver
display.start()

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/tshirts") 

content = driver.page_source 
driver.quit()
display.stop()
soup = BeautifulSoup(content,'lxml')

products = soup.find_all('li', class_ = "product-base")


for product in products:
    product_brand = product.find('h3', class_ = "product-brand").text
    product_name = product.find('h4', class_ = "product-product").text

    print(f'Product Brand :{product_brand}')
    print(f'Product Name :{product_name}')
    
    product_price = product.find('div', class_ = "product-price")
    product_url = product.a['href']
    try:
        image = product.find('img')
        print(image['src'])
    except TypeError:
        print("Image Fetch is limited on this Page Please visit Prodcut URL")


    print(f'Product price :{product_price.text}')
    print(f'Product URL :https://www.myntra.com/{product_url}')
    print('')
    
