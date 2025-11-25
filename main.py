mashiqlar1_2511

# 1 - masala
docs = input("Hujjat topshirilganmi? (ha/yo'q): ")
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ")
test = input("Testdan o'tdingizmi? (ha/yo'q): ")

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")



# 2 - masala
royxat = [4, 7, 2, 5, 1, 10]
new_list = []

for i in range(len(royxat)):
    new_list.append(royxat[i] * i)

print(new_list)


words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]



# 3 - masala
first = ""
second = ""

for w in words:
    if len(w) > len(first):
        second = first
        first = w
    elif len(w) > len(second) and w != first:
        second = w

print("1-chi eng uzun so'z:", first)
print("2-chi eng uzun so'z:", second)


# 4 - masala
name = input("Ismni kiriting: ")


if len(name) <= 2:
    print(name)
else:
    first = name[0]
    last = name[-1]
    middle = "X" * (len(name) - 2)
    print(first + middle + last)
