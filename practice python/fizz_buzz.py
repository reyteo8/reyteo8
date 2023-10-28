x = 0
if x != 100
    x+=1
    try:
        y = int(x / 3)
        print(x)
    except:
        x = 'fizz'
    try:
        y = int(x / 5)
        print(x)
    except:
        x = 'buzz'
    print(x)