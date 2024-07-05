def beforeMidterm(w,a,t):
    if(w > 20) :
        print("คะแนนเก็บไม่สามารถมีค่ามากกว่า 20 ได้")
    elif(a > 10) :
        print("คะแนนจิตพิสัยไม่สามารถมีค่ามากกว่า 10 ได้")
    elif(t > 20) :
        print("คะแนนสอบไม่สามารถมีค่ามากกว่า 20 ได้")
    else :
        midterm = w + a + t
        return midterm

w = int(input("คะแนนเก็บ: "))
a = int(input("คะแนนจิตพิสัย: "))
t = int(input("คะแนนสอบ: "))

print("คะแนน midterm = %d" % beforeMidterm(w,a,t))