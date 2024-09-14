l = "  la  "
l = l.replace("la","al")
print(l.strip(),"|",l.rstrip(),"|",l.lstrip(),"|",sep="")
l = "Hello World"
ls = l.split(" ")
print(ls)
l2 = " ".join(ls)
print(l2)
