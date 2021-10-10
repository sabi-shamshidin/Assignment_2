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

    print("Place: ", data[0])
    print("Name: ", data[1])
    print("Symbol: ", data[2])
    print("Market Cap: ", data[3])
    print("Price: ", data[4])
```
#### Search coin in google search
```python
from src.scrapper import WebScrapper

if __name__ == '__main__':
    newWebScrapper = WebScrapper()
    query = "Dogecoin"
    number_of_results = 10
    newWebScrapper.search_for_google(query, number_of_results)
```
