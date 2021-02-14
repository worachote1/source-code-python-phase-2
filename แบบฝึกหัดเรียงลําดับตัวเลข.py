# รับและเรียงลําดับข้อมูลตัวเลข

number=[]
while True :
    x=int(input("ป้อนตัวเลข : "))
    if x<0 :
        break
    number.append(x)

print("ก่อนเรียง => ",number)
number.sort() #ใช้ฟังก์ชั่น sort() ที่ List เพื่อให้ทําการเรียงลําดับเลขในข้อมูลจากน้อยไปมาก
print("หลังเรียง แบบน้อยไปมาก => ",number) 
number.reverse() # เรียงจาก มาก ไป น้อย
print("หลังเรียง แบบมากไปน้อย => ",number) 
print("จบโปรแกรม")