import json
studentlist=[{"name":"kiran","roll":11},{"name":"charan","roll":12}]
# print(json.dumps(studentlist))
myjsondata=json.dumps(student)
with open(jsonfilepath,'w',encoding='utf-8') as f:
    f.write(myjsondata)