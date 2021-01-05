import xlsxwriter
import requests
from bs4 import BeautifulSoup


workbook = xlsxwriter.Workbook('CraigsList.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

URL = 'https://berlin.craigslist.org/search/bka?lang=en&cc=gb'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

name_list = []
price_list = []
final_dict = {}
counter = 1

names = soup.find_all("h3", class_='result-heading')
for name in names:
    name_list.append(name.text.replace('\n', ''))

prices = soup.find_all("span", class_='result-price')
for price in prices:
    price_list.append(price.text)

for name in name_list:
    final_dict[name] = price_list[(counter*2)-1]
    counter += 1

for entry in final_dict:
    worksheet.write(row, col, entry)
    worksheet.write(row, col + 1, final_dict[entry])
    row += 1

workbook.close()