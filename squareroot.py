import cmath

a,b,c = 1,-2,1


disc = b**2-4*a*c

root1=(-b+cmath.sqrt(disc))/2*a

root2=(-b-cmath.sqrt(disc))/2*a

print("the roots of equation is {0} and {1} ".format(root1,root2))
