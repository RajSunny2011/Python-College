def decor(func): #creates the wrap func
    def wrap(*args): #prints the output
        print("="*60)
        print("Start of funtion")
        
        try:
            res = func(*args)
            print(res)
        except Exception as e:
            print("Error occured: {}".format(e))

        print("End of Function")
        print("="*60)
    return wrap


@decor #this decorates the following func so whenever the func is called it atomatically gets decorated
def primenumbers(x, y=2):
    j = y
    l = []
    while j < x:
        e = int((j**0.5)+1)
        if any([j % i == 0 for i in range(2,e)]):
            j += 1
        else:
            l.append(j)
            j += 1
    return l


@decor #can be used multiple times
def printtext():
    return "Hello world!"



printtext()

primenumbers(100,50)