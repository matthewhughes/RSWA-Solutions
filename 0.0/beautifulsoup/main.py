from BeautifulSoup import BeautifulSoup
import requests

def main():
    page = requests.get('http://localhost:5000/')
    soup = BeautifulSoup(page.content)
    print soup('h1')

if __name__ == '__main__':
    main()
