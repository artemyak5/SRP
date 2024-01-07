import spyre as server
import pandas as pd
from datetime import datetime
import urllib
import os

def download_data():
    indexes = ['', 22, 24, 23, 25, 3, 4, 8, 19, 20, 21, 9, 90, 10, 11, 12, 13, 14, 15, 16, 250, 17, 18, 6, 1, 2, 7, 5]
    
    now = datetime.now()
    global date 
    date = now.strftime('%d%m%Y%H%M%S')
            
    if os.path.isdir('data'):
        for f in os.listdir('data'):
            os.remove('data/'+f)
    else:
        os.mkdir('data')
            
    for i in range(1,28):
        urls = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={}&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2=2023'.format(i)
        text = urllib.request.urlopen(urls).read().decode('utf-8')
        
        out = open(f'data/NOAA_ID_{str(indexes[i])}_{date}.csv','wb')

        text = '\n'.join(text.split("\n")[1:]).replace("<tt><pre>", '').replace("<br>", '').replace("</pre></tt>", '').replace(",", ';').encode()
        out.write(text)
        out.close()



class StockExample(server.App):
    title = 'NOAA data vizualization'

    inputs = [
        {
            "type": 'dropdown',
            "label": 'Вибрати дані(1)',
            "options": [{'label': "VCI", "value": 'VCI'},
                        {'label': "TCI", "value": 'TCI'},
                        {'label': "VHI", "value": 'VHI'}],
            "key": 'ticker1',
            "action_id": "update_data"
        },]

