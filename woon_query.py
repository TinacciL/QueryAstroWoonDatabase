from bs4 import BeautifulSoup
import os
import requests
import pandas as pd
from urllib.request import urlopen, urlretrieve

pwd = '/Users/tinaccil/Documents/GitHub/woon_query/xyz_files'
main_url = "http://www.astrochymist.org/properties/"
url =  requests.get(main_url).text
soup = BeautifulSoup(url,features="html.parser")
hrf_Natoms = []
for link in soup.find_all('a'):
    tmp = link.get('href')
    if 'atoms' in tmp:
        hrf_Natoms.append(tmp)
for j,item_j in enumerate(hrf_Natoms): 
    tmp_url = main_url + item_j
    url =  requests.get(tmp_url).text
    soup = BeautifulSoup(url,features="html.parser")
    hrf_mol = []
    for link in soup.find_all('a'):
        tmp = link.get('href')
        if '.xyz' in tmp:
            hrf_mol.append(tmp)
    tmp_bl = True
    tmp_str_url = ''
    for i,item in enumerate(item_j):
        if item == '/':
            tmp_bl = False
        if tmp_bl == True:
            tmp_str_url = tmp_str_url + item
    for i,item in enumerate(hrf_mol):
        filename = os.path.join(pwd, item.rsplit('/', 1)[-1])
        tmp_url = main_url + tmp_str_url + item[1:]
        try:
            urlretrieve(tmp_url, filename)
            #print(tmp_url,filename)
        except:
            print(item_j,item,tmp_url)