import tkinter as tk

def showme() :
    n = E1.get()
    num = E2.get()
    print(n) 
    print(num)

app = tk.Tk()
app.geometry("500x300")
app.title("HEY HEY hI")
l1 = tk.Label(text="ท่านกำลังเข้าสู่บริการรับฝาก หัวใจ ลงทะเบียนฝากไว้อะไรต่อไม่รู้จำไม่ได้")
l2 = tk.Label(text="กรอกชื่อ: ")
l3 = tk.Label(text="กรอกเบอร์โทรศัพท์: ")
E1 = tk.Entry()
E2 = tk.Entry()
B1 = tk.Button(text="OK", command= showme)
l1.place(x=50, y=10)
l2.place(x=30, y=30)
E1.place(x=75, y=30)
l3.place(x=30, y=55)
E2.place(x=130, y=55)
B1.place(x=105, y=85)
app.mainloop()