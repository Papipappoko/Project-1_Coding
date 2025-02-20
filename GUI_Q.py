import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_service_fee():
    try:
        # รับค่าเวลา วัน เดือน ปี เข้าและเวลาออกจาก Entry
        date_in = entry_in.get()
        date_out = entry_out.get()

        # แปลงข้อมูลที่รับมาเป็นประเภท datetime
        time_in = datetime.strptime(date_in, "%d/%m/%Y %H:%M")
        time_out = datetime.strptime(date_out, "%d/%m/%Y %H:%M")

        # ตรวจสอบว่าเวลาเข้าไม่น้อยกว่าเวลาออก
        if time_in < time_out:
            # คำนวณระยะเวลาที่ใช้
            duration = time_out - time_in
            total_hours = duration.total_seconds() / 3600

            # กำหนดค่าบริการตามชั่วโมง
            if total_hours <= 2:
                service_fee = 0
            elif total_hours <= 4:
                service_fee = total_hours * 20
            elif total_hours <= 5:
                service_fee = total_hours * 50
            else:
                service_fee = total_hours * 100

            # แสดงผลค่าบริการ
            label_result.config(text=f"ค่าบริการที่ต้องจ่าย: {service_fee:.2f} บาท")
        else:
            messagebox.showerror("Error", "เวลาเข้าไม่สามารถมากกว่าเวลาออก กรุณากรอกใหม่")

    except ValueError:
        messagebox.showerror("Error", "รูปแบบวันที่หรือเวลาไม่ถูกต้อง กรุณากรอกใหม่")

# ฟังก์ชันปิดโปรแกรม
def close_program():
    root.quit()

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณค่าบริการ")

# ตั้งค่าหน้าต่างให้เป็นโหมดเต็มจอ
root.attributes("-fullscreen", True)  # เปิดโหมดเต็มจอ
root.config(bg="#f0f8ff")  # ตั้งสีพื้นหลังเป็นสีฟ้าอ่อน

# ตั้งค่าขนาดตัวอักษรที่ใหญ่ขึ้น
font_large = ("Arial", 18)

# สร้างและวาง Label และ Entry สำหรับเวลาเข้า
label_in = tk.Label(root, text="กรุณากรอกวันที่และเวลาเข้า (DD/MM/YYYY HH:MM):", font=font_large, bg="#f0f8ff")
label_in.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

# สร้างกรอบสำหรับช่องกรอก (Entry) เวลาเข้า
entry_in_frame = tk.Frame(root, bg="#f0f8ff")
entry_in_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

entry_in = tk.Entry(entry_in_frame, font=font_large, width=25, bd=2, relief="solid", highlightbackground="#add8e6", highlightthickness=1, justify="center")
entry_in.pack(padx=5, pady=5)

# สร้างและวาง Label และ Entry สำหรับเวลาออก
label_out = tk.Label(root, text="กรุณากรอกวันที่และเวลาออก (DD/MM/YYYY HH:MM):", font=font_large, bg="#f0f8ff")
label_out.grid(row=2, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

# สร้างกรอบสำหรับช่องกรอก (Entry) เวลาออก
entry_out_frame = tk.Frame(root, bg="#f0f8ff")
entry_out_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

entry_out = tk.Entry(entry_out_frame, font=font_large, width=25, bd=2, relief="solid", highlightbackground="#add8e6", highlightthickness=1, justify="center")
entry_out.pack(padx=5, pady=5)

# สร้างกรอบสำหรับปุ่มคำนวณค่าบริการ (เอาเส้นออก)
frame_calculate = tk.Frame(root, bg="#f0f8ff")
frame_calculate.grid(row=4, column=0, columnspan=2, pady=30, sticky="nsew")

button_calculate = tk.Button(frame_calculate, text="คำนวณค่าบริการ", command=calculate_service_fee, font=font_large, width=20, bg="#4caf50", fg="white", relief="flat")
button_calculate.pack(padx=10, pady=10)

# สร้างกรอบสำหรับปุ่มปิดโปรแกรม (เอาเส้นออก)
frame_close = tk.Frame(root, bg="#f0f8ff")
frame_close.grid(row=6, column=0, columnspan=2, pady=30, sticky="nsew")

button_close = tk.Button(frame_close, text="ปิดโปรแกรม", command=close_program, font=font_large, width=20, bg="#f44336", fg="white", relief="flat")
button_close.pack(padx=10, pady=10)

# สร้าง label สำหรับแสดงผลค่าบริการ
label_result = tk.Label(root, text="ค่าบริการที่ต้องจ่าย: 0 บาท", font=("Arial", 22), bg="#f0f8ff", fg="#ff6347")
label_result.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

# ฟังก์ชันสำหรับย่อหน้าต่างกลับไปเป็นปกติ
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    root.geometry("600x400")  # กำหนดขนาดหน้าต่างเป็น 600x400

# ฟังก์ชันเพื่อออกจากโหมดเต็มจอโดยการกดปุ่ม Escape
root.bind("<Escape>", exit_fullscreen)

# ทำให้โปรแกรมอยู่กลางหน้าต่าง
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# เริ่มต้นหน้าต่าง
root.mainloop()
