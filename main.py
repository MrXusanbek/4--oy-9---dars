# 4 - oy 9 dars
# map
# filter
# mavzu  Concurrency :Multithreading, Context manager

# Multithreading
# import time
# from threading import Thread
#
#
#
# def read_file():
#     print("O'qish boshlandi!!!")
#     time.sleep(1)
#     print("O'qish tugadi!!!")
#
#
#
# start = time.time()
#
# th1 = Thread(target = read_file)
# th2 = Thread(target = read_file)
# th3 = Thread(target = read_file)
#
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Faylni o'qish uchun{round(end - start,2)} vaqt ketdi")

#---------------------------------------------
# import time
# from threading import Thread
#
#
#
# def read_file():
#     print("O'qish boshlandi!!!")
#     time.sleep(1)
#     print("O'qish tugadi!!!")
#
#
#
# start = time.time()
#
# threades = []
# for i in range (100):
#     th = Thread(target = read_file)
#     th.start()
#     threades.append(th)
#
#
# for th in threades:
#     th.join()
#
#
# end = time.time()

# print(f"Faylni o'qish uchun{round(end - start,)} sekund ketdi")

#------------------------------------------------------------
# homeworks
# 1 misol
def sum_of_digits(number):
    return sum(int(digit)

for digit in str(abs(number)))
print(sum_of_digits(108))
#-------------------------------------
# 2 misol
def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days} kun, {hours} soat, {minutes} minut, {seconds} sekund"

print(convert_seconds(91000))
#--------------------------------------------------
# 3 misol
def capitalize_words(names):
    return [name.capitalize() for name in names]

names = ['messi ', 'yamal', 'william', 'alba']
print(capitalize_words(names))
#-----------------------------------------
# 4 misol
def high_scores(scores):
    return [score for score in scores if score > 75]

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print(high_scores(scores))
#-------------------------------------------
# 5 misol
def find_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]

words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
print(find_palindromes(words))
#-------------------------------------
# 6 misol
text = input("Matn kiriting: ")
i = 0
result = ""
while i < len(text):
    if text[i] == 'e':
        result += '3'
    else:
        result += text[i]
    i += 1
print(result)
#------------------------------------------
# 7 misool
text = input("Matn kiriting: ")
i = 0
result = ""
while i < len(text):
    if text[i] != ' ':
        result += text[i]
    i += 1
print(result)
#--------------------------------
# 8 misol
numbers = [i for i in range(10)]
doubled = [x * 2 for x in numbers]
print(doubled)
#-----------------------------
# 9 misol
import random

streams = [random.randint(1, 100) for _ in range(10)]
print(streams)


