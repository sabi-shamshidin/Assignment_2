# Assignment 2

Done by Shamshidin Sabina from SE-2008

## Installation

```bash
git clone 
cd webScrappingAssignment
pip install requirements.txt
```

## Usage

### MacOS
```bash
python main.py
```
### Windows 
```bash
python main.py
```
#### Get exact coin
```python
from src.scrapper import WebScrapper

if __name__ == '__main__':
    newScapper = WebScrapper()
    data = newScapper.get_currency("BTC") #get exact coin with its symbol

    print("Rank: ", data[0])
    print("Name: ", data[1])
    print("Symbol: ", data[2])
    print("Market Cap: ", data[3])
    print("Price: ", data[4])
    print("Circulating Supply: ", data[5]) 
```
#### Get all coins
```python
from src.scrapper import WebScrapper

if __name__ == '__main__':
    newScapper = WebScrapper()
    data = newScapper.get_currencies() #print out loaded currencies

    for i in range(len(data)):
        print("Rank: ", data[i][0])
        print("Name: ", data[i][1])
        print("Symbol: ", data[i][2])
        print("Market Cap: ", data[i][3])
        print("Price: ", data[i][4])
        print("Circulating Supply: ", data[i][5])
```
#### Search coin in google search
```python
from src.scrapper import WebScrapper

if __name__ == '__main__':
    newWebScrapper = WebScrapper()
    query = "cardano"
    number_of_results = 10
    newWebScrapper.search_for_google(query, number_of_results)
```
