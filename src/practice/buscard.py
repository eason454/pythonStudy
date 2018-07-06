from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
def queryCard(value):
    payload = {'CardNumder': value, 'Pid': '96'}
    r = requests.get('http://www.cdgjbus.com/Card.aspx', params=payload)
    soup = BeautifulSoup(r.text)
    # print(soup.prettify())
    # print(soup.find('table',class_='TablecLass').find_all('td')[12].text)
    count=0
    title=['CardNo', 'Line', 'GPS', 'Time', 'Consume', 'Rest', 'Wallet']
    consumes=[]
    for x in soup.find('table',class_='TablecLass').find_all('td'):
        if count >6 and count < 14:
            consumes.append(x.text.replace("\r\n","").replace("'","").strip())
        count=count+1
    # title=['CardNo', 'Line', 'GPS', 'Time', 'Consume', 'Rest', 'Wallet']
    # title=['11', '22', '22', '22', '22', '22', '22']
    # consumes=['010080013040', 'G79', '029155', '2018-7-5 18:38:23', '0', '2', '']
    print(title)
    print(consumes)
    print(tabulate([consumes], headers=title, tablefmt='orgtbl'))


if __name__ == '__main__':
    queryCard('010080013040')
