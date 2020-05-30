import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

if __name__ == '__main__':
    Date = '-'
    Title = '-'
    record = []

    # Access the page
    r = requests.get('https://tribune.com.pk/kse-100-index/')

    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html,'lxml')

    news_title = soup.find_all("h2",{"class":"title"})
    # news_title = soup.find_all("div",{"class":"story  cat-0 group-0 position-14 sub-story clearfix"})
    
    news_description = soup.find_all("p",{"class":"excerpt"})
    title_list = []
    description_list = []
    # print("Hello world")
    for title in news_title:
        title_list.append(title.text)
    for description in news_description:
        description_list.append(description.text)
    for i in range(14):
        print("Title: ",title_list[i])
        print("Description: ",description_list[i])
        print()
