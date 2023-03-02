import requests
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/'

response = requests.get(main_url) # отправляем запрос
# print(type(response.text)) # <class 'str'>

soup = BeautifulSoup(response.text, 'lxml')
# print(dir(soup))

phones_span = soup.find('span', {"id":"phones"})
raw_phones = phones_span.text
phones_list = []

for ph in raw_phones.split("\n"):
    clear_phone = ph.replace('\r', '').strip()
    if clear_phone:
        phones_list.append(clear_phone)

"-------------------------Детализация продукта----------------"
product_url = 'product/view/elektrosamokat-ninebot-kickscooter-f40'

response = requests.get(main_url+product_url)
soup = BeautifulSoup(response.text, 'lxml')

product_card = soup.find('div', {"class":"product-view"})

title = product_card.find('h1').text

#print(product_card.find_all('img'))

image_box = product_card.find('div', {'class':'img_full'})
image = image_box.find('img').get('src')
#print(image)

price = product_card.find('span', {'itemprop':'price'}).text

data = {'title':title, 'image':image, 'price':price}

print(data)


