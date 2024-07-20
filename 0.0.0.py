
value=input()

if bool(value)==True:
    result=open("database.py",mode='r')
    resultread=result.read()
    if resultread==None:
        print("apple")
    elif resultread != None:
        print("banana")
else:
    print("")

