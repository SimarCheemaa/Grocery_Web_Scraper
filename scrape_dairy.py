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

            if item_type == None:
                if title.find("Cheese") != -1:
                    item_type = "Cheese"

                elif title.find("Butter") != -1:
                    item_type = "Butter"

                elif title.find("Nonfat Yogurt") != -1:
                    item_type = "Nonfat Yogurt"

                elif title.find("Lowfat Yogurt") != -1:
                    item_type = "Lowfat Yogurt"

                elif title.find("Whole Milk Yogurt") != -1:
                    item_type = "Whole Milk Yogurt"

                elif title.find("Whole Milk") != -1:
                    item_type = "Whole Milk"

                elif title.find("Vitamin D") != -1:
                    item_type = "Whole Milk"

                elif title.find("2%") != -1:
                    item_type = "2% Milk"

                elif title.find("Fat Free") != -1:
                    item_type = "Fat Free Milk"

                elif title.find("1%") != -1:
                    item_type = "1% Milk"

                else:
                    item_type = "na"

            info = [title, brand, weight, price, item_type]
            thewriter.writerow(info)
            item_type = None


# Butter and Cheese
URL = "https://newindiansupermarket.com/collections/butter-cheese"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('butter_cheese.csv', lists, 'w')

# Milk
URL = "https://newindiansupermarket.com/collections/milk?page=1"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('milk.csv', lists, 'w')

URL = "https://newindiansupermarket.com/collections/milk?page=2"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('milk.csv', lists, 'a')

# Eggs
URL = "https://newindiansupermarket.com/collections/eggs"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('eggs.csv', lists, 'w', "Eggs")

# Paneer
URL = "https://newindiansupermarket.com/collections/paneer"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('paneer.csv', lists, 'w', "Paneer")

# Tofu
URL = "https://newindiansupermarket.com/collections/tofu"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('tofu.csv', lists, 'w', "Tofu")

# Whipped Cream
URL = "https://newindiansupermarket.com/collections/whipped-cream"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('whipped_cream.csv', lists, 'w', "Whipped Cream")

# Yogurt Drink / Lassi
URL = "https://newindiansupermarket.com/collections/yogurt-drink-lassi"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('yogurt_drink_or_lassi.csv', lists, 'w', "Lassi")

# Yogurt / Dahi
URL = "https://newindiansupermarket.com/collections/yogurt-dahi?page=1"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('yogurt_dahi.csv', lists, 'w')

URL = "https://newindiansupermarket.com/collections/yogurt-dahi?page=2"  # URL to go to
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
create_csv('yogurt_dahi.csv', lists, 'a')
