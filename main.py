son = int(input("Juft son kiriting: "))
print('Raxmat!') if son%2==0 else print('Bu son juft emas')
# Foydalanuvchidan yoshini sorab parkka kirish narxini chiqaramiz
yosh = int(input('Yoshingiz nechida: '))
if yosh<4 or yosh>60:
  narx = 'bepul'
if yosh<18:
  narx= '10000 so\'m'
if yosh>18:
  narx = '20000 so\'m'
print(f"Sizning yoshingiz {yosh}da chipta narxi {narx} ")

#Foydalanuvchidan 2 ta son kiritishini so'rab taqoslash
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(son1>son2) if son1>son2 else print(f"{son1<son2")