# wapf to accept as input rad
# return area and circum
 
def ar_ci(rad):
	ar = 3.14159 * rad ** 2
	ci = 2 * 3.14159 * rad 
	return ar, ci
rad = float(input("enter radius "))
a1, a2 = ar_ci(rad)

print("area = ", a1)
print("circumference = ", a2)