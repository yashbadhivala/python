fval1 = 123.2567
fval2 = 204.1234

print("Values are", fval1, "and", fval2) 
print(f"Values are {fval1} and {fval2}") 
print("Values are {fval1} and {fval2}".format(fval1 = 123.2567, 
fval2 = 204.1234)) 
print("Values are {0} and {1}".format(fval1, fval2)) 
print("Values are {} and {}".format(fval1, fval2)) 
print("Values are %f and %f" % (fval1, fval2))