import csv,json
myfile='petrol.csv'
jsonfilepath='petrol.json'
petrol_list=[]
with open(myfile,'r',encoding='utf-8') as p:
    dataReader=csv.DictReader(p)
    for data in dataReader:
        petrol_list.append(data)

petrol_list_json=json.dumps(petrol_list)
with open(jsonfilepath,'w',encoding='utf-8') as p:
    p.write(petrol_list_json)