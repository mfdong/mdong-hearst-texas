import requests
import csv
from bs4 import BeautifulSoup

storageURL = "https://cdec.water.ca.gov/dynamicapp/QueryMonthly?s=LVQ"
avgURL = "https://cdec.water.ca.gov/dynamicapp/profile?s=LVQ&type=res"

storagePage = requests.get(storageURL)
avgPage = requests.get(avgURL)

storageSoup = BeautifulSoup(storagePage.content, "html.parser")
avgSoup = BeautifulSoup(avgPage.content, "html.parser")

#####################

storageTable = storageSoup.find(id="monthly_values")

storageRows = []

for row in storageTable.findAll('tr')[1:]:
    storageCells = []
    storageCells.append(row.findAll('td')[0].text.strip())
    storageCells.append(row.findAll('td')[1].text.strip())
    storageRows.append(storageCells)

####################

avgTable = avgSoup.find(width="490")

avgRows = []

for row in avgTable.findAll('tr')[:-1]:
    avgCells = []
    avgCells.append((row.findAll('td')[0]).find('b').text.strip())
    avgCells.append(row.findAll('td')[1].text.strip())

    avgRows.append(avgCells)

outfile = open("./water-data.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Date", "Storage"])
writer.writerows(storageRows)
writer.writerow([])
writer.writerow(["Month", "Average"])
writer.writerows(avgRows)
