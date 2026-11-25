# #1 დაწერეთ პაროლის გენერატორი.
# #
# import random
#
# lower = list("abcdefghijklmnopqrstuvwxyz")
# upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# digits = list("0123456789")
# symbols = list("!@#$%^&*")
#
# while True:
#   length_input = input("შეიყვანე პაროლის სიგრძე: ").strip()
#   if length_input.isdigit() and int(length_input) > 0:
#     length = int(length_input)
#     break
#   print("შეიყვანე სწორი დადებითი რიცხვი")
#
# pool = []
#
# for label, chars in [
#     ("პატარა ლათინური ასოები", lower),
#     ("დიდი ლათინური ასოები", upper),
#     ("რიცხვები", digits),
#     ("სიმბოლოები", symbols),
# ]:
#   while True:
#     ans = input(f"გინდა {label}? (y/n): ").strip().lower()
#     if any("ა" <= ch <= "ჰ" for ch in ans):
#       print("შეიყვანე მხოლოდ ლათინური ასოები")
#       continue
#     if ans in ("yes", "y"):
#       pool.extend(chars)
#       break
#     if ans in ("no", "n"):
#       break
#     print("ჩაწერე მხოლოდ y ან n")
#
# if not pool:
#   pool = lower
#
# password = ""
# for _ in range(length):
#   password += random.choice(pool)
#
# print(f"შენი დაგენერირებული პაროლია: {password}")

#2  პაროლის სირთულის შემოწმება

# while True:
#   pw = input("შეიყვანე პაროლი შესაფასებლად: ")
#   if any("ა" <= ch <= "ჰ" for ch in pw):
#     print("გამოიყენე მხოლოდ ლათინური ასოები")
#   else:
#     break
# score = 0
# if len(pw) >= 8:
#   score += 2
# if len(pw) >= 12:
#   score += 1
#
#
# has_lower = False
# has_upper = False
# has_digit = False
# has_symbol = False
#
# for ch in pw:
#   if ch.islower():
#     has_lower = True
#   elif ch.isupper():
#     has_upper = True
#   elif ch.isdigit():
#     has_digit = True
#   elif not ch.isalnum():
#     has_symbol = True
#
# if has_lower:
#   score += 2
# if has_upper:
#   score += 2
# if has_digit:
#   score += 1
# if has_symbol:
#   score += 1
#
#   #(გამეორებაზეც 1 ქულას ვუმატებ)
# if len(pw) > 0 and len(set(pw)) == len(pw):
#   score += 1
# if score <= 3:
#   level = "weak"
# elif score <= 6:
#   level = "medium"
# else:
#   level = "strong"
# print(f"ქულა: {score}/10 | შეფასება: {level}")

#3
# def get_length():
#   while True:
#     val = input("შეიყვანე ფიბონაჩის რიგის სიგრძე: ").strip()
#     if val.isdigit() and int(val) > 0:
#       return int(val)
#     elif val.isalpha():
#       print("შენ შემოიტანე ასოები, არასწორია! მხოლოდ რიცხვი!")
#     else:
#       print("შენ შემოიტანე სიმბოლო, არასწორია! მხოლოდ რიცხვი!")
#
#
# def fibonacci(n):
#   if n == 1:
#     return [0]
#
#   seq = [0, 1]
#   while len(seq) < n:
#     seq.append(seq[-1] + seq[-2])
#   return seq
#
#
# length = get_length()
# result = fibonacci(length)
# print(f"ფიბონაჩის რიგი ({length} ელემენტი): {result}")
