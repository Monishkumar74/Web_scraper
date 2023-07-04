
import requests
from bs4 import BeautifulSoup

oyo_url=("https://www.oyorooms.com/hotels-in-chennai/")
req = requests.get(oyo_url)
content = req.content

soup = BeautifulSoup(content,"html.parser")

all_hotels = soup.find_all("div",{"class":"hotelCardlisting"})

for hotel in all_hotels:
    hotel_name = hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    hotel_address=hotel.find("span",{"itemprop":"steertAddress"}).text
    hotel_price=hotel.find("span",{"class":"listingPrice"}).text
    try:
        hotel_rating=hotel.find("span",{"class":"hotelRating_ratingSummary"}).text
    except AttributeError:
        pass

    print(hotel_name,hotel_address,hotel_price,hotel_rating)

