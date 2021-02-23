# ใช้ความรู้จากเรื่อง Recursive function 
# มาหาค่า แฟกทอเรียล

'''
5! = 5*4*3*2*1 = 120
'''
def factorial(number):
    if number == 1 :
        return number
    
    else :
       return number * factorial(number-1)

x=factorial(5)
print(x)




