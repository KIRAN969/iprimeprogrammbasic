import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/posts")
ExtractedData=data.json()
# print(ExtractedData)
# x=ExtractedData["articles"]
l=[]
for i in ExtractedData:
    l.append(i["title"])
list=[x for x in l if x[0]=='a' in x]
print(list)