import requests, json

image_url = 'https://i.pinimg.com/736x/b1/4b/4f/b14b4f6b5d4c7d7c4afe6c8e5c6887c7.jpg'

response = requests.get(image_url)

with open("test.jpg", 'wb') as file:
    file.write(response.content)

print(response)
