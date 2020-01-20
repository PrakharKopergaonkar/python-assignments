n = int(input("enter a digit"))
leftshift = n<<1
rightshift = n>>1
if(leftshift==n*2):
    print("leftshift of n i.e n<<1 = n*2 = {}".format(leftshift))
if(rightshift==int(n/2)):
    print("rightshift of n i.e n>>1 = n/2 = {}".format(rightshift))
