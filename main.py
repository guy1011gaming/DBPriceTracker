import requests
from bs4 import BeautifulSoup

url = input("Please paste the url to the train connecion you wish to get information on: ")

def download_url(url):
    html = requests.get(url).text
    bs_element = BeautifulSoup(html, features="html.parser")
    return bs_element

def get_prices(bs_element):
    prices = bs_element.find_all(class_='fareAmount')
    for index in range(len(prices)):
        prices[index] = str(prices[index].contents[0])
    return prices

def get_tickets(bs_element):
    tickets = bs_element.find_all(class_='availabilityOfferName')
    for index in range(len(tickets)):
        tickets[index] = str(tickets[index].contents[0])
        tickets[index] = tickets[index].replace('\n', "")

    for index in range(len(tickets)):
        if "preis" not in  tickets[index]:
            tickets.pop(index)

    return tickets

def generate_price_table(prices, tickets):
    price_table = []
    for index in range(len(tickets)):
        price_touple = (tickets[index], prices[index])
        price_table.append(price_touple)

    return price_table

bs_element = download_url(url)

prices = get_prices(bs_element)
tickets = get_tickets(bs_element)

print(prices)
print(tickets)

print(generate_price_table(prices, tickets))