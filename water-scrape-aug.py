import requests
import csv
from bs4 import BeautifulSoup

reservoirs = [["LVQ"], ["HTH"], ["APN"], ["KNT"], ["SHA"]]

for reservoir in reservoirs:
    storageURL = "https://cdec.water.ca.gov/dynamicapp/QueryMonthly?s=" + reservoir[0]
    storagePage = requests.get(storageURL)
    storageSoup = BeautifulSoup(storagePage.content, "html.parser")
    storageRow = storageSoup.find(text="08/2021").parent.parent
    reservoir.append(storageRow.findAll('td')[1].text.strip())

    avgURL = "https://cdec.water.ca.gov/dynamicapp/profile?s=" + reservoir[0] + "&type=res"
    avgPage = requests.get(avgURL)
    avgSoup = BeautifulSoup(avgPage.content, "html.parser")
    reservoir.append(avgSoup.find(text="August").parent.parent.parent.findAll('td')[1].text.strip())

####################

outfile = open("./water-data-all-august.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Reservoir", "August storage", "August average"])
writer.writerows(reservoirs)