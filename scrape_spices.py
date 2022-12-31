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
            try:
                i = title.index(" ")
                brand = title[:i]
            except:
                brand = title

            info = [title, brand, weight, price, item_type]
            thewriter.writerow(info)


# Spices
i = 1
file_type = 'w'
while i < 33:
    # URL to go to
    URL = f"https://newindiansupermarket.com/collections/spices-herbs?page={i}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all(
        'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
    create_csv('spices.csv', lists, file_type, 'Spice')
    file_type = 'a'
    i += 1
