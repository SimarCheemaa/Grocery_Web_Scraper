from bs4 import BeautifulSoup
import requests
from csv import writer


def create_csv(file_title: str, lists: list, value: str):
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
            header = ["Title", "Brand", "Quantity", "Price"]
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
                link = lst.find('a', class_='quick-buy btn')
                if link:
                    link = link.get('href')
                    link = "https://newindiansupermarket.com" + link
                    page = requests.get(link)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    w = soup.find('option').get('value')
                    weight = ""
                    for num in w:
                        if num.isnumeric():
                            weight += num
                    weight += " lb"
                else:
                    weight = "na lb"
            title = title.strip().title()
            price = price.strip()[1:]
            weight = weight.strip()[:-3]
            i = title.index(" ")
            brand = title[:i]
            info = [title, brand, weight, price]
            thewriter.writerow(info)


# Basmati Rice Page - 1
URL = "https://newindiansupermarket.com/collections/basmati-rice?page=1"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('basmati_rice.csv', lists, 'w')

# Basmati Rice Page - 2
URL = "https://newindiansupermarket.com/collections/basmati-rice?page=2"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('basmati_rice.csv', lists, 'a')

# Brown Rice
URL = "https://newindiansupermarket.com/collections/brown-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('brown_rice.csv', lists, 'w')

# Idly Rice
URL = "https://newindiansupermarket.com/collections/idly-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('idly_rice.csv', lists, 'w')

# Masoori Rice
URL = "https://newindiansupermarket.com/collections/masoori-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('masoori_rice.csv', lists, 'w')

# Organic Rice
URL = "https://newindiansupermarket.com/collections/organic-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('organic_rice.csv', lists, 'w')

# Ponni Rice
URL = "https://newindiansupermarket.com/collections/ponni-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('ponni_rice.csv', lists, 'w')

# Pounded Rice
URL = "https://newindiansupermarket.com/collections/pounded-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('pounded_rice.csv', lists, 'w')

# Sela Rice
URL = "https://newindiansupermarket.com/collections/sela-rice"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('sela_rice.csv', lists, 'w')
