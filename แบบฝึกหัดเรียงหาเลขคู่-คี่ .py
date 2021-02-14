number=[]
number_odd=[]
number_even=[]
while True :
    x=int(input("ป้อนตัวเลข : "))
    if x<0 :
        break
    elif x % 2 ==0 :
        number_even.append(x)

    elif x % 2 !=0 :
        number_odd.append(x)
    number.append(x)        

print("List เลขทั้งหมด =>",number)
print("List เลขคี่ =>",number_odd)
print("List เลขคู่ =>",number_even)
print("จบโปรแกรม")        