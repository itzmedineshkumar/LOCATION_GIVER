import requests
key = '2472c2eb627da1c41290acbe6bf4f203'
city = input("ENTER YOUR CITY NAME FOR LOCATION >>> ")
aq = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
data= requests.get(aq).json()
b=len(data)
print(b)
if b==1:
    lon=data[0]['lon']
    print(lon)
    lat=data[0]['lat']
    print(lat)
    country=data[0]['country']
    motherlang=data[0]['local_names'].get('hi',None)
    print(motherlang)
    print(f"YOU HAD ENTERED FOR {city} FOR {country} AND ITS LONGITUDE IS {lon} , ITS LATITUDE IS {lat} AND CITY NAME IN HINDI IS {motherlang}")
else:
    print("CITY NAME NOT FOUND")



