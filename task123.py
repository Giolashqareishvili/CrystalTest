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

#4 პალინდრომი
# def clean_text(text):
#   result = ""
#   for ch in text.lower():
#     if ch.isalnum():
#       result += ch
#   return result
#
# def is_palindrome(s):
#   return len(s) > 0 and s == s[::-1]
#
# def suggest_palindrome(s):
#   for i in range(len(s)):
#     removed = s[:i] + s[i + 1 :]
#     if is_palindrome(removed):
#       return f"ერთი სიმბოლოს წაშლით ('{s[i]}'): {removed}"
#
#
#   left = 0
#   right = len(s) - 1
#   while left < right:
#     if s[left] != s[right]:
#       insert_left = s[:left] + s[right] + s[left:]
#       if is_palindrome(insert_left):
#         return f"ერთი სიმბოლოს ჩასმით ('{s[right]}'): {insert_left}"
#
#       insert_right = s[: right + 1] + s[left] + s[right + 1 :]
#       if is_palindrome(insert_right):
#         return f"ერთი სიმბოლოს ჩასმით ('{s[left]}'): {insert_right}"
#       break
#     left += 1
#     right -= 1
#
#   return "ერთი სიმბოლოს ჩასმით ან წაშლით პალინდრომი ვერ მიიღება."
# while True:
#   raw = input("შეიყვანე ტექსტი(არ გამოიყენო სიმბოლები): ")
#
#   if any(not ch.isalnum() for ch in raw):
#     print("სიმბოლოს გამოყენება არ შეგიძლია! გამოიყენე მხოლოდ ასოები და ციფრები.")
#     continue
#   cleaned = clean_text(raw)
#   if is_palindrome(cleaned):
#     print(f"'{cleaned}' არის პალინდრომი!")
#     break
#   suggestion = suggest_palindrome(cleaned)
#   print(f"'{cleaned}' არ არის პალინდრომი. შემოთავაზება — {suggestion}")


#5 ზედმეტსახელების გენერატორი
# while True:
#   raw = input("შეიყვანე მხოლოდ ერთი სიტყვა: ").strip()
#
#   if not raw:
#     print("ცარიელი ველი არ შეიძლება! შეიყვანე ერთი სიტყვა.")
#     continue
#
#   if len(raw.split()) > 1:
#     print("შეიყვანე მხოლოდ ერთი სიტყვა (ჰარების გარეშე)!")
#     continue
#
#   if any(not ch.isalnum() for ch in raw):
#     print("სიმბოლოს გამოყენება არ შეგიძლია! გამოიყენე მხოლოდ ასოები.")
#     continue
#
#   if not raw.isalpha():
#     print("რიცხვების გამოყენება არ შეიძლება! შეიყვანე მხოლოდ ერთი სიტყვა.")
#     continue
#
#   word = raw.lower()
#   break
#
# nicknames = [
#     f"pro_{word}",
#     f"{word}_x",
#     f"the_{word}",
#     f"{word}_99",
#     f"{word}_{word[:2]}",
# ]
#
# print(f"\nზედმეტსახელები სიტყვისთვის '{word}':")
# for i, nick in enumerate(nicknames, start=1):
#   print(f"{i}. {nick}")

#6 დავალება

# import random
#
# while True:
#   parts = input("შეიყვანე რიცხვები გამოტოვებით: ").strip().split()
#   if parts and all(
#       p.isdigit() or (p.startswith("-") and p[1:].isdigit()) for p in parts
#   ):
#     nums = [int(p) for p in parts]
#     break
#   print("შეიყვანე მხოლოდ რიცხვები, თითო გამოტოვებით!")
#
# while True:
#   print(
#       "\nაირჩიე სორტირების წესი:\n1 - კლებადობით\n2 - ზრდადობით\n3 -"
#       " random"
#   )
#   choice = input("შენი არჩევანი (1-3): ").strip()
#
#   if choice == "1":
#     res = sorted(nums, reverse=True)
#     break
#   if choice == "2":
#     res = sorted(nums)
#     break
#   if choice == "3":
#     res = nums.copy()
#     random.shuffle(res)
#     break
#
#   print("არასწორი არჩევანია, შეიყვანე 1, 2, 3 ან 4.")
#
# print(f"შედეგი: {res}")

# 7 დავალება
# while True:
#   text = input("შეიყვანე ტექსტი: ")
#   if text.strip():
#     break
#   print("ცარიელი ტექსტი არ შეიძლება, შეიყვანე რამე.")
#
# filtered = "".join(ch for ch in text if ch.isalpha() or ch == " ")
#
# print(f"გაფილტრული ტექსტი: {filtered}")

# 8 დავალება
# while True:
#   raw = input("შეიყვანე რიცხვები (მაგ. 3,5,7,2 ან 3 5 7 2): ").strip()
#   parts = raw.replace(",", " ").split()
#
#   if len(parts) >= 2 and all(
#       p.isdigit() or (p.startswith("-") and p[1:].isdigit()) for p in parts
#   ):
#     current = [int(p) for p in parts]
#     break
#
#   print("შეიყვანე მინიმუმ ორი რიცხვი (მძიმით ან გამოტოვებით)!")
#
# print()
# while True:
#   print(" ".join(str(x) for x in current))
#   if len(current) == 1:
#     break
#
#   next_row = []
#   for i in range(len(current) - 1):
#     next_row.append(current[i] + current[i + 1])
#   current = next_row

# #9 დავალება
# while True:
#   text = input("შეიყვანე ტექსტი: ").strip()
#   if text:
#     break
#   print("ცარიელი ტექსტი არ შეიძლება, შეიყვანე რამე")
#
# words = []
# for part in text.lower().split():
#   clean_word = "".join(ch for ch in part if ch.isalnum())
#   if clean_word:
#     words.append(clean_word)
#
# counts = {}
# for w in words:
#   counts[w] = counts.get(w, 0) + 1
#
# max_count = max(counts.values())
# most_common = [w for w, c in counts.items() if c == max_count]
#
# if len(most_common) == 1:
#   print(f"ყველაზე ხშირი სიტყვაა: '{most_common[0]}' (გამეორდა {max_count}-ჯერ)")
# else:
#   joined = ", ".join(f"'{w}'" for w in most_common)
#   print(
#       f"ყველაზე ხშირი სიტყვებია (თანაბარი რაოდენობით): {joined} (თითოეული"
#       f" {max_count}-ჯერ)"
#   )

#10 დავალება
#
# while True:
#   sentence = input("შეიყვანე წინადადება: ").strip()
#
#   if not sentence:
#     print("ცარიელი წინადადება არ შეიძლება, შეიყვანე რამე.")
#     continue
#
#   if any(not ch.isalnum() and ch != " " for ch in sentence):
#     print(
#         "სიმბოლოების გამოყენება არ შეგიძლია! გამოიყენე მხოლოდ სიტყვები/ასოები."
#     )
#     continue
#
#   break
#
# word_lengths = {}
# for word in sentence.split():
#   word_lengths[word] = len(word)
#
# print(f"სიტყვების სიგრძეები: {word_lengths}")

# last commit
