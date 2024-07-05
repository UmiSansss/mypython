def fh(c):
    f = 9/5*c+32
    return f

def kv(c):
    k = c +273.15
    return k

c = float(input("enter your degree celcius: "))
print ("the celcius in farenheit is equal to %.2f and in kelvin is equal to %.2f" % (fh(c), kv(c)))