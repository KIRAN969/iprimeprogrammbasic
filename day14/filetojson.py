import csv,json
myfile='student.csv'
jsonfilepath='student.json'
student_list=[]
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.DictReader(f)
    for data in dataReader:
        student_list.append(data)

student_list_json=json.dumps(student_list)
with open(jsonfilepath,'w',encoding='utf-8') as f:
    f.write(student_list_json)