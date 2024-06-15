import os
import requests
from bs4 import BeautifulSoup

# Using eBay as test site 
product_name = input(str("Enter object name below\n>> ")).lower()
print("This scripts is fetching all the images from ebay and it's only scrape the firstpage atleats for now")
domain = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw="
url = f'{domain}{product_name}'

fetch = requests.get(url)
if fetch.status_code == 200:
    soup = BeautifulSoup(fetch.text, 'html.parser')
    image_counter = 1
    

    def convert_to_file(img_url, counter):
        folder_name = 'train_images'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        print(f'Downloading image: {img_url}')
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            image_path = os.path.join(folder_name, f'image_{counter}.jpg')
            with open(image_path, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f'Saved image to {image_path}')
        else:
            print(f'Failed to download image: {img_url}')

    for data in soup.find_all('div', {'class': 's-item__wrapper clearfix'}):
        img = data.find('img')
        if img:
            image_url = img.get('src')
            if image_url:
                convert_to_file(image_url, image_counter)
                image_counter += 1
        else:
            print('Image not found in the current data block')
else:
    print(f'Failed to fetch the URL: {url}')

