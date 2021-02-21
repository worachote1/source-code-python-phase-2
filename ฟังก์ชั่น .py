# ฟังก์ชั่น
# เอาไว้แบ่งส่วนการทํางาน เวลาสร้างโปรแกรมที่มีการใช้งานหลายๆส่วน (โปรแกรมย่อยที่ทํางานของโปรแกรมหลัก)
# แยกการทํางานของคําสั่งซํ้าๆ โดยที่เราไม่ต้องเขียนขึ้นมาใหม่


# การสร้าง และ เรียกใช้ ฟังก์ชั่น
# def ชื่อฟังก์ชั่น () : 
#       statement
     
def sayHi(): #ฟังก์ชั่นที่เป็นโปรแกรมย่อย
    print("Hello , Function !!!")

sayHi() # โปรแกรมหลัก   

# Global Variable / Local Variable

def displayNumber() :
    x=50
    print("Hello = ",x," ใน")

#โปรแกรมหลัก
x=20
displayNumber()
print("Hello = ",x," นอก")

# Global Variable ตือ โปรแกรมหลักที่ข้อมูลทุกส่วนสามารถเข้าถึงค่าตัวนี้ได้ (ก็คือ x ตัวนอก)
# ส่วน Local Variable คือ โปรแกรมที่ทํางานเฉพาะในฟังก์ชั่นส่วนนั้นๆแล้วจบการทํางานไปเลย (ก็คือ x ตัวใน)

#การส่งค่าเข้ามาที่ function

def myData(name) : #ตัวแปร name ในวงเล็บ เราจะเรียกว่า Paramiter
    print("Hello ,",name)

myData("Time Worachote") # ส่งค่า Time Worachote เข้าไปเก็บที่ตัวแปร name ในฟังก์ชั่น

def myData_2(First_name,Last_name) : # function นี้เก็บ paramiter 2 ตัว
    print("ชื่อ = ",First_name," นามสกุล = ",Last_name)

myData_2("Worachote ","Jairew")

'''
# Argument และ Parameter

# Argument => เป็นค่าที่จะส่งเข้าไปในตัว function
# ในตัวอย่าง ฟังก์ชั่น def def myData_3( ) คือ fname,lname,age ตอนที่เรียกใช้ function

# Parameter => เป็นตัวแปรที่รับข้อมูลส่งมาทํางาน โดย ข้อมูลที่ส่งมานัั้นส่งมาจาก Argument 
# ในตัวอย่าง ฟังก์ชั่น def def myData_3( ) คือ a,b,c

def myData_3(a,b,c):
    print("ชื่อ = ",a," นามสกุล = ",b," อายุ = ",c)

fname = "Worachote" # จะได้เอาค่าที่อยู่ใน fname ทีเป็น Argument ไปเก็บใน Parameter ที่มีชื่อว่า a
lname="Jairew"
age=19

myData_3(fname,lname,age)

'''
# ฟังก์ชันเลขคู่-เลขคี่

def check_OddOrEven(num) :
    if num % 2==0 :
          print(num,"เป็นเลขคู่")
    if num % 2!=0 :
          print(num,"เป็นเลขคี่")   
      
a,b,c,d=10,23,40,50

check_OddOrEven(a)
check_OddOrEven(b)
check_OddOrEven(c)
check_OddOrEven(d)

