import requests
key = '2472c2eb627da1c41290acbe6bf4f203'
cityname = input("ENTER YOUR CITY NAME FOR LOCATION >>> ")
aq = f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&appid={key}"
a= requests.get(aq).json()
b=len(a)
print(b)
if b==1:
    longitude=a[0]['lon']
    print(longitude)
    latitude=a[0]['lat']
    print(latitude)
    country=a[0]['country']
    hindi=a[0]['local_names'].get('hi',None)
    print(hindi)
    print(f"YOU HAD ENTERED FOR {cityname} FOR {country} AND ITS LONGITUDE IS {longitude} , ITS LATITUDE IS {latitude} AND CITY NAME IN HINDI IS {hindi}")
else:
    print("CITY NAME NOT FOUND")



