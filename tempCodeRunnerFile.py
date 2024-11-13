def search():
        target = int(cal2.get())
        position = -1
        for i, num in enumerate(data1):
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