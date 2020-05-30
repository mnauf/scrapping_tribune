import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

if __name__ == '__main__':
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
    
    s1 = pd.Series(title_list[0:14], name='News Heading')
    s2 = pd.Series(description_list[0:14], name='News Description')
    df = pd.concat([s1,s2], axis=1)
    df = df.fillna("None")
    # d = {'Phone name': phone_name_list, 'Price per month': price_per_month_list,'Interest List': interest_list, 'Total Price List': total_price_list,'Unlimited Offer List': unlimited_offer_list}
    # df = pd.DataFrame(data=d)
    print(df)
    df.to_csv('tribune.csv', encoding='utf-8')