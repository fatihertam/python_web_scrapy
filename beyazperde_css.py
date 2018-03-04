import csv
import requests
from bs4 import BeautifulSoup

j=1
while True:
	url  = "http://www.beyazperde.com/filmler/tum-filmleri/kullanici-puani/?page=" + str(j)
	sayfa = requests.get(url)
	if sayfa.status_code !=200:
		break
	
	j=j+1

	
	filmadi = BeautifulSoup(sayfa.content,"html.parser")
	veri = filmadi.find_all("a", {"class":"no_underline"})
	veri2 = filmadi.find_all("span", {"class":"note"})
	
	i=0
	while i<=19:
		baslik = veri[i].text
		puan = veri2[i].text
		
		with open("beyazperde.csv", "a") as cikti:
			baslik=baslik.encode('utf-8')
			puan=puan.encode('utf-8')
			writer = csv.writer(cikti)
			writer.writerow([baslik,puan])				
		
		i=i+1

