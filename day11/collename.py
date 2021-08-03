# named tuple
import collections as c
employees=c.namedtuple('employees',["name","empId","salary"])
e1=employees("raju","1021","52111")
print(e1.name)