# Set เป็น Non-primitive datatype อีกตัวหนึ่งที่มีคุณสมบัติ เหมือน List และ Tuple
# แต่จะเก็บข้อมูลสมาชิกที่ ซํ้ากันไม่ได้ 
# ลําดับ ของ Set ไม่แน่นอน เพราะไม่มี index
 
# การสร้าง Set แบบปกติ
fruit={"มะม่วง","มะขาม","มะยม" }
print(fruit)

# การสร้าง Set แบบ constructor
lis=["ปลาทู","ปลาตะเพียน"]
fish=set(lis)
print(fish)

# การเพิ่มข้อมูลสมาชิก
fish.add("ปลาปิรันย่า")
print(fish)

#ลองหัดเพิ่มข้อมูล โดยใช้ loop ดู

#ให้เขียน loop while รับค่าที่ต้องการที่จะเพิ่มใน Set เรื่อยๆ
'''
while True :
    add_fish = str(input("เพิ่มข้อมูลปลา : "))
    if add_fish == "n" or add_fish ==  "N" :
        break
    fish.add(add_fish)
   
print(fish)
'''
# การใช้ Set operator
# การที่เราจะใช้ Set operator ได้นั้น เราต้องสร้าง Set ออกมา 2 กลุ่ม

# 1. union ยูเนี่ยน
fruitA={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB={"แอปเปิ้ล","ทุเรียน","สตอว์เบอร์รี่","กีวี่","มะม่วง"}

allFruit= fruitA.union(fruitB)
print("ใช้ union",allFruit)


# 2. different เหมือน A-B ในคณิตเรื่องเซต ที่จะเอาเฉพาะใน SetของA ที่ไม่มีอยู่ใน SetของB 

fruitC=fruitA.difference(fruitB)
print("ใช้ difference",fruitC)

# 3. intersection เอาเฉพาะข้อมูลที่มีเหมือนกัน ในทั้ง 2 set
fruitD=fruitA.intersection(fruitB)
print("ใช้ intersection",fruitD)
