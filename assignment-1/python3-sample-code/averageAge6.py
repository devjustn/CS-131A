# input values
age1 = 19
age2 = 21
age3 = 31

# output (calculated) values 
averageAge = (age1 + age2 + age3) / 3.0 # 23.66666...

# rounded output (see 4.1)
averageAgeFormatted = "%.0f" % averageAge
print("The average of three ages is", averageAgeFormatted)