# Arbitrary Arguments(agrs) 
# *agrs
# พารามิเตอร์ไร้ชื่อ ใช้ argument ได้หลายๆตัว
# คือ แค่function เดียวแต่ส่ง argument ได้หลายตัว

def add(*agrs): #args เก็บข้อมูลแบบ Tuple เราเข้าถึงข้อมูล argument ผ่าน index ของ agrs[i]
    print(agrs)
    sum = 0

    for i in agrs :
        sum += i
    print("บวกกันได้ = ",sum)

   
     


add(10)
add(10,11,65)
add(10,11,65,754)
