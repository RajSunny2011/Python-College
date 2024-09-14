sec =  int(input("Enter seconds: "))
hour = sec//3600
remsec = sec%3600
minute = remsec//60
remsec = remsec%60
print(f"{hour}h {minute}m {remsec}s")
