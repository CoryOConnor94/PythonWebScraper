import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yl1d2Z_MK2s")
soup = BeautifulSoup(page.content, "html.parser")
sevenDays = soup.find(id="seven-day-forecast")

periodTags = sevenDays.select(".tombstone-container .period-name")
periods = [pt.get_text()for pt in periodTags]

short_desc = [sd.get_text() for sd in sevenDays.select(".tombstone-container .short-desc")]
temp = [t.get_text() for t in sevenDays.select(".tombstone-container .temp")]
desc =[d["title"] for d in sevenDays.select(".tombstone-container img")]


weather = pd.DataFrame({
	"Period":periods,
	"Short Description": short_desc,
	"Temperature": temp,
	"Description": desc
	
})
print(weather)
	






'''single period code'''
#forecasts = sevenDays.find_all(class_="tombstone-container")
#tonight = forecasts[0]
#period = tonight.find(class_="period-name")
#short_desc = tonight.find(class_="short-desc")
#temp = tonight.find(class_="temp temp-high")
#print(period.text)
#print(short_desc.text)
#print(temp.text)

#img = tonight.find("img")
#desc = img['title']
#print(desc)
