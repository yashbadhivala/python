fval1 = 123.2567
fval2 = 204.1234

print("Values are", "%.2f" %fval1, "and", "%.2f" %fval2)

print(f"Values are {fval1:.2f} and {fval2:.2f}")

print("Values are {fval1:.2f} and {fval2:.2f}".format(fval1 = 
123.2567, fval2 = 204.1234))

print("Values are {0:.2f} and {1:.2f}".format(fval1, fval2))

print("Values are {:.2f} and {:.2f}".format(fval1, fval2))

print("Values are %.2f and %.2f" % (fval1, fval2)) 