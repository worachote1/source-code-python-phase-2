# Recursive Function
# เป็น ฟังก์ชั่น ที่เรียก ฟังก์ชั่นตัวเอง


'''
def a() :
    print("A")
    a() #เรียกใช้ a() อีกรอบนึง

def b() :
    print("B")

a() # output คือ A A A A....  ไปเรื่อยๆ

'''

# ใช้ Recursive function หา 1-5 โดยไม่ใช้ คําสั่ง loop

# หาจุดวนซํ้า
# และ หาจุดออกจาก function ให้ได้ ต้องระบุ return เพื่อ ออกจากfunction
# ต้องมี Parameter

def addNumber(number):
    if number == 6 :
        return  # กลับออกมาจาก ฟังก์ชั่น เมื่อ วนloopครบ 1-5
    print(number)
    number += 1
    addNumber(number)
    
addNumber(1)    

# สร้าง recursive function เพื่อบวกเลข 1-5

def summation(number):
    
    if number == 1 :
        return  # กลับออกมาจาก ฟังก์ชั่นเมื่อวนloopจนเจอ 1
    else :
        return number+summation(number-1)
          

x=summation(5) # 5+4+3+2+1
print(x)