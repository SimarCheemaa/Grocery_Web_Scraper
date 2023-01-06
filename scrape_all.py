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
            try:
                i = title.index(" ")
                brand = title[:i]
            except:
                brand = title

            info = [title, brand, weight, price, item_type]
            thewriter.writerow(info)


# Goes to the main website and scrapes for all of the names of sections and gets the href link
URL = 'https://newindiansupermarket.com'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all(
    'a', class_="sub-nav-item-link")

x = 'w'
for lst in lists:
    # For each of the subcategory links, creates the temp link to go to
    category = lst.get('href')[13:]
    # Page number
    i = 1
    temp = URL + lst.get('href') + f'?page={i}'
    page = requests.get(temp)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all(
        'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
    # Keeps going to next page until page has no information
    while lists != []:
        create_csv('master.csv', lists, x, category)
        x = 'a'
        i += 1
        temp = URL + lst.get('href') + f'?page={i}'
        page = requests.get(temp)
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all(
            'div', class_="product-block layout-align-above align-center flex column max-cols-5 min-cols-2")
