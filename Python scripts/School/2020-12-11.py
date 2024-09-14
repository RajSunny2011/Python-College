#To remove an item using the key <dict>.pop(<key>[,<default>]) or del <dict>[<key>]
"""d = {1:1,2:2,3:3,4:4}
print(d.pop(1))
del d[2]
print(d)
print(d.pop(5,"Not found"))"""
#To remove the last element added in a dict <dict>.popitem()
"""d = {1:1,2:2,3:3,4:4}
print(d.popitem())
print(d)"""
#Q WAP remove the key-item pair with key 'tiger'
d = {'lion':'wild','tiger':'wild','cat':'domestic'}
d.pop('tiger')
print(d)