from tkinter import*

sequential = Tk()
sequential.geometry("948x550")
sequential.title("Sequential Search")
sequential.configure(background="#C1FFC1")

def exit ():
    sequential.destroy()

def reset_array():
    data.clear()  # Clear the list
    lb.delete(0, END)  # Clear the listbox


def clear ():
    cal.set(" ")
    cal2.set(" ")
    cal3.set(" ")

def add_number():
    input_text = cal.get()
    if input_text.strip():  # Check if the input is not empty
        input_numbers = input_text.split()  # Split input by whitespace
        for num_str in input_numbers:
            try:
                number = int(num_str)
                data.append(number)
                lb.insert(END, number)
            except ValueError:
                # Handle non-integer input
                pass
        cal.set("")  # Clear the input field

def search():
    target = int(cal2.get())
    position = -1
    for i, num in enumerate(data):
        if num == target:
            position = i
            break
    sqInput3.config(state="normal")
    if position != -1:
        sqInput3.delete(0, END)
        sqInput3.insert(0, f"พบข้อมูล {target} ที่ตำแหน่ง {position}")
    else:
        sqInput3.delete(0, END)
        sqInput3.insert(0, "ไม่พบข้อมูลที่ต้องการค้นหา")
    sqInput3.config(state="readonly")


data = []
sqtitle = Label(sequential,text="Sequential Search",font=16,bg="#C1FFC1")
sqtitle.grid(row=0,column=0,columnspan=5,padx=400,pady=20)

cal = StringVar()
cal.set(" ")
sqtitle2 = Label(sequential,text="กรอกข้อมูลตัวเลข",font=20,bg="#C1FFC1")
sqtitle2.grid(row=2,column=0,columnspan=2,padx=0,pady=20)
sqInput = Entry(sequential,font=20,textvariable=cal)
sqInput.grid(row=2,column=1,columnspan=2)


sqbotton = Button(sequential,text="เพิ่ม",font=2,bg="#9BCD9B",command=add_number)
sqbotton.grid(row=2,column=2,columnspan=2)


sqbotton4 = Button(sequential,text="Reset",font=2,bg="#9BCD9B",command=reset_array)
sqbotton4.grid(row=3,column=2,columnspan=2)

cal2 = StringVar()
cal2.set(" ")
sqtitle3 = Label(sequential,text="ค้นหาข้อมูล",font=20,bg="#C1FFC1")
sqtitle3.grid(row=3,column=0,columnspan=2)
sqInput2 = Entry(sequential,font=20,textvariable=cal2)
sqInput2.grid(row=3,column=1,columnspan=2)


cal3 = StringVar()
cal.set(" ")
sqtitle4 = Label(sequential,text="ผลลัพธ์",font=20,bg="#C1FFC1")
sqtitle4.grid(row=4,column=0,columnspan=2,padx=0,pady=20)
sqInput3 = Entry(sequential,font=20,textvariable=cal3)
sqInput3["state"] = "readonly"
sqInput3.grid(row=4,column=1,columnspan=2)

sqbotton2 = Button(sequential,text="ค้นหา",font=2,bg="#9BCD9B",command=search)
sqbotton2.grid(row=5,column=1,columnspan=2,padx=0,pady=20)

sqbotton3 = Button(sequential,text="ยกเลิก",font=2,bg="#9BCD9B",command=clear)
sqbotton3.grid(row=5,column=1,columnspan=3,padx=0,pady=20)

sqbotton5 = Button(sequential,text="Exit",font=2,bg="#9BCD9B",command=exit)
sqbotton5.grid(row=5,column=2,columnspan=4,padx=0,pady=20)


lb = Listbox(sequential, font=("Arial", 20))
lb.grid(row=6, column=0, columnspan=4, padx=20, pady=20)

sequential.mainloop()