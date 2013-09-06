from pyquery import PyQuery
import requests

def main():
   d = PyQuery(requests.get("http://localhost:5000/").content)
   print d('h1')

if __name__ == '__main__':
    main()
