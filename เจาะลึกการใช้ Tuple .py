# ใช้ Tuple ข้อมูลจะเปลี่ยนแปลงไม่ได้ แต่ถ้าใช้ List ข้อมูลจะเปลี่ยนแปลงได้   
#ข้อมูลสมาชิกภายในเขียนภายใต้ ( )

tup=(1,2,3,4,"Time Worachote",3.99,True) # Tuple
print(tup)


#การเข้าถึงข้อมูล คล้ายกับของ List เลย
print(tup[0:4]) #ไล่ index จากขวามาซ้าย เริ่มจาก indexที่ 0 จบที่ ก่อน indexที4 ได้ output คือ (1,2,3,4)
print(tup[-3]) #negative index ได้ output คือ Time Worachote

#การแก้ไขข้อมูล
#เนื่องจาก tuple ไม่สามารถแก้ไขข้อมูลได้ 
#ถ้าต้องการจะแก้ไขข้อมูลต้อง แปลงจาก Tuple ให้เป็น List ซะก่อนเพราะว่า List นั้นสามารถแก้ไขข้อมูลได้

tup_to_list = list(tup) #แปลง Tuple ให้เป็น List โดย สร้างตัวแปรที่มี คอนสตรัคเตอร์ list มาเก็บข้อมูลจาก Tuple เดิม
print("ก่อนแก้ไข =>",tup_to_list) # ได้ output เป็น List แล้วคือ [1,2,3,4,"Time Worachote",3.99,True]
tup_to_list[4]="Jessi Lingard" #เรื่มเปลี่ยนข้อมูล โดยเปลี่ยนที่ index ที่ 4 "Time Worachote"
print("หลังแก้ไข =>",tup_to_list) # ข้อมูล ตรง index ที่ 4 ถูก เปลี่ยนเป็น "Jessi Lingard"


#แสดงผลด้วย loop 

#ดึงข้อมูลของสมาชิกแต่ละตัวของ tup_to_list มาเก็บไว้ใน item
'''
for item in tup_to_list :
    print("สมาชิก =",item)
'''
print("-----------------------------------")

# len(tup_to_list) ได้เท่ากับ 7

for i in range(len(tup_to_list)) : # เหมือน for i in range(0,7)
    print("สมาชิก index ที่",i,"=",tup_to_list[i])

                                  

          

 