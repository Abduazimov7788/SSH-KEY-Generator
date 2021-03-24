import random

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def a_Finder(x, y, p):
	
	# Initialize result
	res = 1;
	
	# Update x if it is more than or
	# equal to p
	x = x % p;
	while (y > 0):
		
		# If y is odd, multiply
		# x with result
		if (y & 1):
			res = (res * x) % p;

		# y must be even now
		y = y>>1; # y = y/2
		x = (x * x) % p;
	
	return res;

# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
	
	# Pick a random number in [2..n-2]
	# Corner cases make sure that n > 4
	a = 2 + random.randint(1, n - 4);

	# Compute a^d % n
	x = a_Finder(a, d, n);

	if (x == 1 or x == n - 1):
		return True;

	# Keep squaring x while one
	# of the following doesn't
	# happen
	# (i) d does not reach n-1
	# (ii) (x^2) % n is not 1
	# (iii) (x^2) % n is not n-1
	while (d != n - 1):
		x = (x * x) % n;
		d *= 2;

		if (x == 1):
			return False;
		if (x == n - 1):
			return True;

	# Return composite
	return False;

# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime( n, k):
	
	# Corner cases
	if (n <= 1 or n == 4):
		return False;
	if (n <= 3):
		return True;

	# Find r such that n =
	# 2^d * r + 1 for some r >= 1
	d = n - 1;
	while (d % 2 == 0):
		d //= 2;

	# Iterate given nber of 'k' times
	for i in range(k):
		if (miillerTest(d, n) == False):
			return False;

	return True;

# Driver Code
# Number of iterations


# while True:
#     Random_Number =random.getrandbits(2048)
#     if(isPrime(Random_Number, k)):
#         print(Random_Number , end=" ");
#         break
# if (isPrime(random.getrandbits(2048), k)):
# 	print(n , end=" ");
# else:
#     isPrime(random.getrandbits(2048), k)

# This code is contributed by mits
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
# while len(Numbers)<2:
#     Rand =random.getrandbits(2048)
#     if(isPrime(Rand, k)):
#         print("Random Number")

#         print(Rand)
#         Numbers.append(Rand)
# print("=====================")
p=27200058871187110598275136946911518555008979699215068018363473606208302337012811014761969810500762060538898175603866389236843719799993930637625809206088081793922870230672836188598576964238253466759302964489197475074022608696390177264072954311199314676774245252188822830707225016203505808793743992037907539732280211076934597739515330695774248989372209360952303885080319352900879468852448067678808953965565018757675162548377912012461418835817787243463200109086625479417727745236606626931361475295225559786231197874911417668283564357500140086231130224514860498486618753625040004384867542951987139236768087203917425127677
q=1624677112316366029990360759081843605501339250274413704640311532627462479879020130255467846668635394435061232319851951517351082303086721179915213049218917701616676207742251847748552604362904504353792606778136448178818836231285014291708896656653364384513308967621234648347750896945853149329110610591210610299711024415062646755077537983900147980337536189433105919503528790890098284722074994475269042008318462102786026146741607653609281087835496631502972284039689214930762958309147904801348774663635292974530724927043540531005916639033798605171053989530608088381016996039694161801688931293334212383721672445742210621349
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


   



