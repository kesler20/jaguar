import smtplib
import requests 
import bs4
from bs4 import BeautifulSoup
url = 'https://dqydj.com/sp-500-return-calculator'
headers = { 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}

# try to use the webdriver instead and apply it to 2 websites for student loan calculator and for rent repayiment calculator
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
roi = soup.find(id='h-the-s-p-500-dividends-reinvested-price-calculator').get_text()
print(roi)