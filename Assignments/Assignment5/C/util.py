__author__ = "Niklas Jönsson & Marcus Rodan"


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def jacobi(a, m):
	j = 1
	a %= m
	while a:
		t = 0
		while not a & 1:
			a = a >> 1
			t += 1
		if t&1 and m%8 in (3, 5):
			j = -j
		if (a % 4 == m % 4 == 3):
			j = -j
		a, m = m % a, a
	return j if m == 1 else 0
