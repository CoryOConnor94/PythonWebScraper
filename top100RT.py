from bs4 import BeautifulSoup
import requests
import openpyxl

excelFile = openpyxl.Workbook()
sheet = excelFile.active
sheet.title = 'Top Rated Movies'
sheet.append(['Rank','Rating','Title','No. of Reviews'])


try:
	content = requests.get("https://www.rottentomatoes.com/top/bestofrt/")
	soup = BeautifulSoup(content.text, "html.parser")

	movies = soup.find('table', class_="table").find_all('tr')
	#print(movies)
	for movie in movies[1:]:
		title  = movie.find('a').get_text(strip=True)
		#print(title.text)
		
		rank = movie.find('td', class_="bold").get_text(strip=True).strip('.')
		#print(rank)
		rating = movie.find('span', class_="tMeterScore").get_text(strip=True)
		#print(rating.text)
		reviewCount = movie.find('td', class_="right hidden-xs").get_text(strip=True)
		#print(reviewCount.text)
		sheet.append([rank,rating,title,reviewCount])
		
except Exception as e:
	print(e)

excelFile.save('Top 100 Films.xlsx')

