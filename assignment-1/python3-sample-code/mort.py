import math
  
# assignment upon declaration (see 3.2.3) 
D = 100 # $ deposited per month
p = 0.075 / 12 # monthly rate
T = 10 * 12 # number of months

#the pow function call (new) 
S = D * ((math.pow(1 + p, T) - 1) / p)

#the output
print(S)