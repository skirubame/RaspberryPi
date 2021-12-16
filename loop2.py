#Global variable
n=0

#setup function
def setup():
    global n
    n=100

def loop():
    global n
    n=n+1
    if((n%2)==0):
        print(n)

#Main
setup()
while True:
    loop()
