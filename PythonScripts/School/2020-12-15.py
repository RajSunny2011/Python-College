#Q: WAP to add new key-value pair to the dict month and display the updated dict
month = {1:'jan',2:'feb'}
month.update({3:'mar'})
print(month)

#Q: WAP to concatinate dict d1 and dict d2 to form dict d
d1 = {1:1}
d2 = {2:2}
d = {}
for i in d1,d2:
    d.update(i)
print(d)