import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/hosting-a-next.js-app-in-production-on-ubuntu-vps"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

# print(soup.prettify())

for heading in soup.find_all("h1"):
    print(heading.text)

# # response = requests.get("https://www.iimtaligarh.com")
# # print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title":"harsh",
#     "body":"bhai",
#     "userId":12
# }
# headers = {
#     "Content-type":"application/json; charset = UTF-8"
# }

# response = requests.post(url,headers=headers,json=data)

# print(response.text)