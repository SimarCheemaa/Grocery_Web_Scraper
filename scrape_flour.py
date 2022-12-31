from bs4 import BeautifulSoup
import requests
from csv import writer


def create_csv(file_title: str, lists: list, value: str, item_type: str = None):
    """
    Creates csv file based on the following variables:
        file_title = "name.csv"
        lists = BeautifulSoup object with data
        value = "w" for writing
                "a" for appending
    """
    with open(file_title, value, encoding='utf8', newline='') as f:  # w = overwrite,  a = append
        thewriter = writer(f)
        # These lines are for creating new file and giving headers
        # Comment out if appending
        if value == "w":
            header = ["Title", "Brand", "Quantity", "Price", "Category"]
            thewriter.writerow(header)

        # Main loop - iterates over each list and gets values from html objects
        for lst in lists:
            title = lst.find('a', class_="title").text
            try:
                price = lst.find('span', class_="amount theme-money").text
            except:
                price = "$0.0"
            try:
                weight = lst.find(
                    'div', class_="product-block__weight-value").text
            except:
                weight = "na lb"

            title = title.strip().title()
            price = price.strip()[1:]
            weight = weight.strip()[:-3]
            i = title.index(" ")
            brand = title[:i]
            info = [title, brand, weight, price, item_type]
            thewriter.writerow(info)


# Cornmeal Flour
URL = "https://newindiansupermarket.com/collections/cornmeal-flour"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'w', 'Cornmeal Flour')

# Gram Flour
URL = "https://newindiansupermarket.com/collections/gram-flour"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Gram')

# Multigrain Flour
URL = "https://newindiansupermarket.com/collections/multigrain-flour"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Multigrain')

# Organic Flour
URL = "https://newindiansupermarket.com/collections/organic-rice-1"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Organic')

# Prasad Flour
URL = "https://newindiansupermarket.com/collections/prasad-flour"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Prasad')

# Sharbati Flour
URL = "https://newindiansupermarket.com/collections/sharbati-flour"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Sharbati')

# Sooji and Millets
URL = "https://newindiansupermarket.com/collections/sooji"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('flour.csv', lists, 'a', 'Sooji and Millets')
