import requests
import csv
from bs4 import BeautifulSoup

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
## print (soup.prettify())

with open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    listings = soup.findAll("objTrainPositions")
    
    for listing in listings:
        lat = listing.Direction.string
        if (lat == "Northbound"):

       # print(listing.TrainLatitude.string)
       # print("--------")
            entryList = []
            for retrieveTag in retrieveTags:
                # print(listing.find(retrieveTag).string)
                entryList.append(listing.find(retrieveTag).string)
            train_writer.writerow(entryList)