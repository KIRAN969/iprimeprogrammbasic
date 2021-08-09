#myfile=open('demo2.bin','w+b')

# print(myfile.tell())
# myfile.write("hello")

# # myfile=open('demo.txt','r')
# myfile.seek(0)
# x=myfile.read()
# print(str(x))
# myfile.close()

# test=bytearray([23,56,25,28,21])
# myfile.write(test)
# myfile.close

# with open('file.txt','w+') as f:
#     f.write("hello")
#     f.seek(0)
#     print(f.read())

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
