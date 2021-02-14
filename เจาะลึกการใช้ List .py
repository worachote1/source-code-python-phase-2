#   เจาะลึกการใช้ List

'''
#เขียนแบบ primitive
a1=1
a2=2
a3=3
a4=4
a5=5
a6=6
a7=7
a8=8
a9=9
a10=10

'''

# เขียนแบบ Non primitive : List
number = [] # list ว่าง
number = [1,2,3,4,5,6] # list มีสมาชิก 1-6
name = ["นาย A","นาย B","นาย C"] # list name มีสมาชิกเป็นข้อมูล

# List สามารถเก็บข้อมูลหลายชนิดได้
all = [10,"นายไข่",True,3.14,-10]

#แสดงผล
print(all)

#เข้าถึงข้อมูลของ List
#เรียงข้อมูลเหมือนใน Array โดย index เริ่มนับที่ 0 
# ส่วน negative index เริ่มนับที่ -1

print(number[4]) #เข้าโดยใช้ index ได้ output คือ 5
print(number[-2])#เข้าโดยใช้ negative index ได้ output คือ 5 เช่นกัน
print(all[1:3]) #เข้าถึงข้อมูลโดยระบุช่วง ตั้งแต่ [1] จนถึง ข้อมูลที่ก่อนจะถึง[3] ได้ output คือ ['นายไข่',True]

'''
#การแก้ไขข้อมูล 
#ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
# ต้องการแก้ข้อมูล เลข 3 ใน list number ให้เป็นเลข 9 

print("ก่อนแก้ไข => ",number) # ได้ output ที่ index ที่2 เป็น 3
number[2] = 9 #แก้ไขข้อมูล
print("ก่อนแก้ไข => ",number) # ได้ output index ที่2 เป็น 9

'''

'''
# นับจํํานวน สมาชิกโดยใช้ len ทํางานร่วมกับ loop for

fruit = ["มะม่วง","มะนาว","มะยม"]

for i in range (len(fruit)) :
    print(fruit[i])
print("-----------------------------------")

for item in  (fruit) :
    print(item)
    
'''

#การเพิ่มข้อมูลโดยใช้ append , insert

fruit = ["มะม่วง","มะนาว","มะยม"]

print("ก่อนเพิ่ม => ",fruit)

#append นําสมาชิกใหม่มาต่อท้ายเพื่อน
fruit.append("มะปราง")
fruit.append("แตงโม")
print("หลังเพิ่ม => ",fruit)

# insert เพิ่มข้อมูลโดยเลือกว่าจะให้แทรกระหว่างสมาชิกใด สมาชิกหนึ่ง
# ใช้โดย .insert( index ที่อยากให้ข้อมูลใหม่เข้าไปแทรก , ข้อมูลใหม่ )
fruit.insert(1,"ทุเรียน")
print("หลังแทรก => ",fruit)

'''
# การลบข้อมูลออกจาก List โดยใช้ remove,pop,del,clear

# remove เป็นการลบที่สามารถ ระบุได้เลยว่าจะลบสมาชิกตัวใดออก
fruit.remove("มะยม") # ลบ remove มะยม
print("หลังใช้ remove =>",fruit)

'''
'''
# pop จะลบสมาชิกตัวล่าสุดออก ก็คือ จะลบสมาชิกตัวสุดท้ายนั่นแหละ!
fruit.pop() # ลบสมาชิกตัวล่าสุด
print("หลังใช้ pop =>",fruit) # จากเดิม แตงโมจะหายไป

'''
'''
# del เป็นการลบที่ระบุได้เหมือน remove แต่แค่ระบุ index แทน
del fruit[2] #ลบสมาชิก index ที่ 1 ใน List ออก
print("หลังใช้ del =>",fruit)
'''
'''
# clear เป้นการลบสมาชิก ใน List ทั้งหมด แต่ตัวแปรของList ยังอยู่
fruit.clear()
print("หลังใช้ clear =>",fruit)
'''
'''
#การคัดลอกข้อมูล
#เป็นการนําข้อมูลใน List เดิม ไปใส่ในอีก List โดยใช้ copy()

x=[]
print("เดิม => ",x ) # เดิมให้ x เป้น List เปล่า
x=fruit.copy()
print("หลังจากคัดลอกข้อมูลจาก fruit มาใส่ใน x => ",x)

'''
