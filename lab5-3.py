def price(amt):
    sum = 0
    for i in range(amt):
        price = float(input("ราคาสินค้า %d  : " % (i+1)))
        sum += price
    return sum
    
def tax(tp):
    vat = tp*7/100
    return vat

def totalprice(price, disc,vat) :
    tp = (price-disc) + vat
    return tp

def discount(tp):
    disc = tp * 5/100
    return disc

amt = int(input("จำนวนสินค้า: "))
tp = price(amt)
print("ราคารวม = %.2f" % tp)
print("ภาษี = %.2f" % tax(tp))
print("ส่วนลด = %.2f บาท" % discount(tp))
print("รวมค่าใช้จ่ายทั้งหมด = %.2f" % totalprice(tp,discount(tp),tax(tp)))