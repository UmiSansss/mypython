def circle(r):
    area = 22/7*(r**2)
    return area
    
radius = float(input("รับค่ารัศมี : "))

print("วงกลมของคุณมีพื้นที่ = %.2f" % circle(radius))