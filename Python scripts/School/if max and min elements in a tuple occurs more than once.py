t = eval(input("Enter a tuple: "))
if t.count(max(t)) > 1:
    print('there more than one maximum element')
else:
    print('there is only one maximum element')
if t.count(min(t)) > 1:
    print('there more than one minimum element')
else:
    print('there is only one minimum element')