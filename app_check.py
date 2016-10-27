import bs4
import urllib.request
from openpyxl import Workbook
from openpyxl import load_workbook

file = "H:\classify.xlsx"
wb = load_workbook(file, data_only=True)
ws = wb["Sheet1"]

#get first google result
def get_res(search):
	url  = "https://www.google.com/search?q=" + str(search).replace(" ","+")
	req  = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib.request.urlopen(req).read()
	soup = bs4.BeautifulSoup(html, "html.parser")
	res  = soup.find("div", {"id" : "ires"}).find("h3", {"class" : "r"}).find("a").get_text()
	return str(res)

#add Play store
def get_play(s):
	return get_res(s + "google play")

#add App store
def get_iOS(s):
	return get_res(s + "app store")

#start slow
for i in range(2, 100):
	cell = ws["A"+str(i)].value
	ws["B"+str(i)] = get_res(cell)
	ws["C"+str(i)] = get_play(cell)
	ws["D"+str(i)] = get_iOS(cell)
	if(i % 10 ==0):
		print("10 passed")
wb.save(file)
