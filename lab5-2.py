def bmi(w, h):
    bmi = w/(h/100)**2
    return bmi

def status(bmi) :
    if(bmi < 18.5):
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif(bmi >= 18.5 and bmi <= 22.99):
        print("สมส่วน")
    elif(bmi >= 23 and bmi <= 24.99):
        print("น้ำหนักเกิน")
    elif(bmi >= 25 and bmi <= 29.99):
        print("โรคอ้วน")
    elif(bmi >= 30):
        print("โรคอ้วนอันตราย")
    
w = int(input("น้ำหนัก = "))
h = int(input("ส่วนสูง = "))

print("BMI คุณ = %.2f" % (bmi(w,h)))
status(bmi(w,h))