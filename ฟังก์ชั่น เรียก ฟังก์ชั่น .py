# ฟังก์ชั่น เรียก ฟังก์ชั่น

#เขียน function เปรียบเทียบค่ามากน้อย

def compareMax(x,y):
    if x > y :
        return x
    else :
        return y   

#max=compareMax(10,5)
#print("ค่ามากสุด = ",max)

def compareMax_three(x,y,z) : # ฟังก์ชั่นนี้เปรียบเทียบค่ามากสุด จากเลข 3 ตัว
        return compareMax(compareMax(x,y),z) # เขียน ฟังก์ชั่น เรียก ฟังก์ชั่น แบบลดรูป

'''   m = compareMax(x,y)  #เขียนแบบเดิม
    max_of_three = compareMax(m,z)
    return max_of_three
'''

print("ค่าที่มากสุด ใน 3 ตัว = ",compareMax_three(30,17,10))    