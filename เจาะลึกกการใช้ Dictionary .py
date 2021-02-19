# Dictionary กําหนด index ได้ โดยอ้างที่ key
# key (การเข้าถึงข้อมูล) , value (ค่าของข้อมูล)

# การสร้าง Dict แบบ ปกติ
# ชื่อตัวแปร = {key:value,key:value,key:value}
colors = {"red": "สีแแดง", "yellow": "สีเหลือง", "green": "สีเขียว"}
print(["green"])

city = {"bangkok": "กรุงเทพ", "korat": "นครราชสีมา"}
print(city["bangkok"])

# การสร้าง Dict แบบ constructor

pets = dict(cat="แมว", dog="หมา")
print(pets["cat"])

# การแก้ไขข้อมูล
colors["red"] = "สีม่วง"
print(colors["red"])

# การเพิ่มข้อมูลเข้าไปที่ Dictionary
# ใช้ .update

colors.update({"blue": "สีนํ้าเงิน", "black": "สีดํา"})
print(colors)

for item in colors.values():
    print(item)

# การสร้าง Nested Dictionary (dict แบบซ้อนกัน)
'''
#แบบเดิม
market={
"ร้านป้าพร":"ขายอาหารตามสั่ง",
"ร้านลุงป้อม":"ขายผลไม้",
"ร้านนํ้าใจ":"ขายเครื่องดื่ม"
}

'''

# แบบใช้ nested dict จะได้ใส่ข้อมูลร้านอาหารที่มากขึ้น

market = {
    "ร้านป้าพร": {
        "โซน": "แถว B ช่องที่ 1",
        "ประเภท": "อาหารตามสั่ง",
        "Menu": ["ข้าวผัด", "กระเพรา"]
    },


    "ร้านลุงป้อม": {
        
        "โซน": "แถว C ช่องที่ 4",
        "ประเภท": "ขายผลไม้",
        "Menu": ["ส้มโอ", "ทุเรียน"]
        },

    "ร้านนํ้าใจ": {
        
        "โซน": "แถว H ช่องที่ 6",
        "ประเภท": "เครื่องดื่ม",
        "Menu": ["เบียร์", "เหล้าขาว"]

    }


}

print(market["ร้านลุงป้อม"])
print(market["ร้านลุงป้อม"] ["โซน"])
