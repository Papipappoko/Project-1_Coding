from datetime import datetime

def calculate_service_fee():
    while True:
        # รับค่าเวลา วัน เดือน ปี เข้าและเวลาออก
        try:
            date_in = input("กรุณากรอกวันที่และเวลาเข้า (DD/MM/YYYY HH:MM): ")
            date_out = input("กรุณากรอกวันที่และเวลาออก (DD/MM/YYYY HH:MM): ")

            # แปลงข้อมูลที่รับมาเป็นประเภท datetime
            time_in = datetime.strptime(date_in, "%d/%m/%Y %H:%M")
            time_out = datetime.strptime(date_out, "%d/%m/%Y %H:%M")

            # ตรวจสอบว่าเวลาเข้าไม่น้อยกว่าเวลาออก
            if time_in < time_out:
                break
            else:
                print("เวลาเข้าไม่สามารถมากกว่าเวลาออก กรุณากรอกใหม่")
        except ValueError:
            print("รูปแบบวันที่หรือเวลาไม่ถูกต้อง กรุณากรอกใหม่")

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
    print(f"ค่าบริการที่ต้องจ่าย: {service_fee:.2f} บาท")

# เรียกใช้งานฟังก์ชัน
calculate_service_fee()
