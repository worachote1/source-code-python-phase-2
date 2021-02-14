
number=[]
while True :
    x=int(input("ป้อนตัวเลข : "))
    if x<0 :
        break
    number.append(x)

print("ค่าที่ตํ่าที่สุดคือ => ",min(number))
print("ค่าที่สูงที่สุดคือ =>",max(number))    