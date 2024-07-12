#bmi = น้ำหนัก / ส่วนสูง (m)**2
#input = น้ำหนัก,ส่วนสูง
#process สูตรหา bmi
#output = bmo
def bmi(Kg,Cm):
    bmi = Kg/(Cm/100)**2
    return bmi

def check(b):
    if(b < 18.5):
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif(b >= 18.5 and b <= 22.9):
        print("สมส่วน")
    elif(b >=23.8 and b <=24.9):
        print("น้ำหนักเกิน")
    elif(b >=25.0 and b <=29.9):
        print("โรคอ้วน")
    elif(b >= 30.0):
        print("โรคอ้วนอันตราย")

Kg = int(input("น้ำหนัก"))
Cm = int(input("ส่วนสูง"))
print("bmi %.2f" % bmi(Kg,Cm))
check(bmi(Kg,Cm))