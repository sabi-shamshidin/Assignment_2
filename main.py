from src.scrapper import WebScrapper

if __name__ == '__main__':
    newWebScrapper = WebScrapper()
    query = "cardano"
    number_of_results = 10
    newWebScrapper.search_for_google(query, number_of_results)
