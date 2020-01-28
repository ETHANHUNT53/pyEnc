name =input("What is your name")
for x in name:
    if(x>='A' and x<='Z' or x>='a' and x<='z'):
        x=ord(x)
        x+=5
        print(chr(x), end='')