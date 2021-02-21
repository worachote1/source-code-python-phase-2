# Keyword Arguments
# ระบุชื่อ Parameter เข้าไปใน function พร้อม argument ได้เลย 
# เพื่อ จะได้ไม่ต้องเจอปัญหา การไม่เรียงลําดับ argument ตามลําดับ paraeter ใน function
def displayData(fname,lname,city) :
    print("ชื่อ = ",fname)
    print("นามสกุล = ",lname)
    print("จังหวัด = ",city)

displayData(city="Cologne",lname="Jairew",fname="Worachote")    