



n = int(input())

a,b,c = 0,0,0
d,e,f = 0,0,0
g,h,i = 0,0,0


for j in range(n):
	marks = input().split()
	x,y,z = int(marks[0]), int(marks[1]), int(marks[2])

	a += x
	b += y
	c += z

	d += x**2
	e += y**2
	f += z**2

	g += x*y
	h += y*z
	i += x*z


corr_math_phy = (n*g - a*b)/((n*d - a**2)*(n*e - b**2))**0.5
corr_phy_chem = (n*h - b*c)/((n*e - b**2)*(n*f - c**2))**0.5
corr_chem_math = (n*i - c*a)/((n*f - c**2)*(n*d - a**2))**0.5

print (round(corr_math_phy,2))
print (round(corr_phy_chem,2))
print (round(corr_chem_math,2))
