with open("C:\\Sunny\\Python\\PythonProgramming\\DemoSatvik.txt","r") as f, open("copy.txt","w") as f2:
    count = 0 
    for line in f:
        count+=1
        f2.write(f"{count}: {line}")