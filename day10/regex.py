import re
a="a234"
v=re.search("[a-zA-Z][0-9]{3}",a)
print(v)