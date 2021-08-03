import collections
dict1={"name":"kiran","age":22}
dict2={"name":"charan","age":25}
comb_dict=collections.ChainMap(dict1,dict2)
print(comb_dict.maps)