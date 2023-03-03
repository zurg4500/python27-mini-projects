import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    response.status_code
    
def main():
    stack_url = 'https://stackoverflow.com/questions'
    pages = '?page='
    get_html(stack_url)
source = response.status_code
print(source)
main()