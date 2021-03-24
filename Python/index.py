import random

def a_Finder(x, y, p):
	
	res = 1;
	
	x = x % p;
	while (y > 0):
		
		if (y & 1):
			res = (res * x) % p;

		y = y>>1; # y = y/2
		x = (x * x) % p;
	
	return res;


def miillerTest(d, n):
	

	a = 2 + random.randint(1, n - 4);


	x = a_Finder(a, d, n);

	if (x == 1 or x == n - 1):
		return True;


	while (d != n - 1):
		x = (x * x) % n;
		d *= 2;

		if (x == 1):
			return False;
		if (x == n - 1):
			return True;


	return False;

def isPrime( n, k):
	

	if (n <= 1 or n == 4):
		return False;
	if (n <= 3):
		return True;

	d = n - 1;
	while (d % 2 == 0):
		d //= 2;


	for i in range(k):
		if (miillerTest(d, n) == False):
			return False;

	return True;

def StylisPrint(s,txt):
    print(txt)
    print(s)
    print("=================")
def gcd(a,b):
    if (not b):
        return a
    return gcd(b, a % b)

k=5
Numbers =[]
while len(Numbers)<2:
    Rand =random.getrandbits(2048)
    if(isPrime(Rand, k)):
        print("Random Number")

        print(Rand)
        Numbers.append(Rand)
print("=====================")
p=Numbers[0]
q=Numbers[1]
n = p *q
StylisPrint(n,"Voici N")

phi = (p-1) * (q-1)
StylisPrint(phi,"Voici Phi")

e=0
i=2
while True:
    if(gcd(i,phi)==1):
        e=i
        break
    i=i+1
StylisPrint(e,"Voici e")

d=0
j=1
while True:
    Num =float("{:.2f}".format((phi*j+1)/e))
    print(Num)
    if Num.is_integer() ==True:
        d=Num
        break
    j=j+1
StylisPrint(d,"Voici d")


   



