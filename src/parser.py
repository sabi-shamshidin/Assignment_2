from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


class WebParser:

    def get_currency(self, symbol):
        data = self.get_currencies()
        for i in range(20):
            if data[i][2] == symbol:
                return data[i]

    def search_for_google(self, query, number_result):
        query = query.replace(' ', '+')
        ua = UserAgent()
        google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")

        result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})
        links = []
        titles = []
        descriptions = []
        for r in result_div:
            try:
                link = r.find('a', href=True)
                title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
                description = r.find('div', attrs={'class': 's3v9rd'}).get_text()

                if link != '' and title != '' and description != '':
                    links.append(link['href'])
                    titles.append(title)
                    descriptions.append(description)
            except:
                continue

        for i in range(len(descriptions)):
            print("Title: ", titles[i])
            print("Description: ", descriptions[i])
            print("Link: ", links[i])
            print("--------------------------------------------------------------------------------------------------")
