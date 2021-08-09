import csv
headerContent=["Name","Roll"]
studentData=[
    {"Name":"kiran","Roll":11},
    {"Name":"anoop","Roll":21},
    {"Name":"charan","Roll":31},
    {"Name":"mani","Roll":41}
]
with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headerContent)
    writer.writeheader()
    writer.writerows(studentData)
