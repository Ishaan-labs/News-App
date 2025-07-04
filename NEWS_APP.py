import time
import requests

print("---------------------WELCOME-----------------------")
print("-----GET NEWS ON ANY TOPIC FROM THE LAST MONTH-----")
print("---------------------------------------------------")

today = time.time()
thirty = 30*24*60*60
act = today - thirty
t = time.strftime("%Y-%m-%d",time.localtime(act))

topic = input("On which topic, you want news : ")

api = "dfd5e5b49c5c4b8f8cb0d0e5f3ef663e"

url = f"https://newsapi.org/v2/everything?q={topic}&from={t}&sortBy=publishedAt&apiKey={api}"

a = requests.get(url)
b = a.json()
c = b["articles"]

for el in c :
    for al in el :
        print(al,":")
        print(el[al])
        print("   ")
    print("---------------------------------------------------------------------------------------")