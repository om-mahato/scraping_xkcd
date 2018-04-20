from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin

from bs4 import BeautifulSoup

for i in range(171, 1000): #number of comics to download from 1 and upto.
	url = 'https://xkcd.com/'+ str(i) +'/'
	u = urlopen(url)
	page_html = u.read()
	u.close()

	soup = BeautifulSoup(page_html, "html.parser")
	img = soup.find(id="comic").img['src']
	print(img)
	file = img.rsplit('/',1)[-1]
	print(file)
	urlretrieve('http:' + img, file)