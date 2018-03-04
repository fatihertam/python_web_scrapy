# ABM306 Web uzerinden bilgiye erisim 
# python ile web sitesinden bilgi cekme


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
	i=0

	while i<=19:
		baslik = veri[i].text
				
		with open("filmadlari.txt", "a") as cikti:
			baslik=baslik.encode('utf-8')
			cikti.write("%s " % baslik)
			cikti.close()
		
		i=i+1


