import requests
import json
import pyttsx3
city = input("Enter the key You want to know the temperature of : \n")
url=f"http://api.weatherapi.com/v1/current.json?key=03d711fcb8b64cf58af100348242712&q={city}&aqi=no"
r=requests.get(url)

# print(r.text)
d=json.loads(r.text)
w=d["current"]["temp_c"]
engine = pyttsx3.init()
print(f"The temperature in {city} currently is {w} degrees celsius.")
engine.say(f"The temperature in {city} currently is {w} degrees celsius.")
engine.runAndWait()