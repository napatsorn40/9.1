def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

# รับค่าตัวเลขจำนวนเต็ม 1 จำนวน
number = int(input("กรุณาป้อนแม่สูตรคูณที่ต้องการ: "))

# แสดงตารางแม่สูตรคูณของตัวเลขที่รับเข้ามา
multiplication_table(number)
