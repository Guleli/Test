1.x=int(input(“Eded daxil edin:”))          
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")
2. n = int(input("Eded daxil edin:"))
if n % 2 == 0:
    print("cut")
else:
    print("tek")
3.a = float(input("a ədədini daxil edin: "))
b = float(input("b ədədini daxil edin: "))
c = float(input("c ədədini daxil edin: "))

print("Ən böyük ədəd:", max(a, b, c))
4. day = int(input("Gun daxil edin:"))
if day ==1:
    print("Bazar gunu")
if day ==2:
    print("Cersenbe axsami")
if day ==3:
    print("Cersenbe")
if day ==4:
    print("Cume axsami")
if day ==5:
    print("Cume")
if day ==6:
    print("Senbe")
if day ==7:
    print("Bazar")
else:
    print("Yanlis gun")
5. temp = int(input("Tempratur daxil edin:"))
if temp<0:
    print("soyuq")
if temp>0 and temp<20:
    print("normal")
else:
    print("isti")
6. password = input("Şifrəni daxil edin: ")
length = len(password)

if length < 8:
    print("qısa")
elif 8 <= length <= 12:
    print("orta")
else:
    print("uzun")
8.for i in range(0, 21, 2):
    print(i)
9. text = "Bağda ərik var idi …"
for char in text:
    print(char
10. for i in range(1, 11):
    if i == 3:
        continue
    print(i)
11. i = 1
while True:
    if i % 5 == 0:
        print("İlk 5-ə bölünən rəqəm:", i)
        break
    i += 1
12. numbers = [1, 3, 5, 7, 9]

for index in range(len(numbers)):
    if numbers[index] == 5:
        print("5-in indeksi:", index)
        break




