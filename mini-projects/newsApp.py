import requests

query = "Web Development"
apikey = "4ce812a5e8e448f190f14df1f1a0e99a"



url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-02&to=2025-06-02&sortBy=popularity&apiKey=4ce812a5e8e448f190f14df1f1a0e99a"

print(url)

r = requests.get(url)

data = r.json()

article = data["articles"]

print("*************** New News *****************")

for art in article:
    print(art["title"])
    print(art["url"])
    print(art["description"])
    print("***********************************")



# print(url)