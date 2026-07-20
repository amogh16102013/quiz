# dct = {"age": 12,
#         "name": "amogh",
#         "sport": "soccer"}
# print(dct["age"])
# dct["sport"] = "basketball"
# print(dct)
# print(len(dct))
# print(dct.keys())
# print(dct.values())
# print(dct.items())
# print(dct.get("age"))
# print(dct.get("other"))
# # print(dct["other"])

# for i in dct:
#     print(i)

# for i in dct.keys():
#     print(i)

# for i in dct.values():
#     print(i)

# print(10 in dct.values())

# word = "amogh"
# new = {}
# for char in word: 
#     if char in new:
#         new[char] += 1
#     else:
#         new[char] = 1
# print(new)

# words = ["hello", "hi", "hello", "greetings", "hi", "salutations", "hi"]
# new = {}
# for w in words:
#     if w in new:
#         new[w] += 1
#     else:
#         new[w] = 1
# print(new)







# word = "codingg"
# new = {}
# for w in word:
#     if w in new:
#        new[w] += 1
#     else: 
#         new[w] = 1
# print(new)

# quiz = {"what year is it?": str(2026), "what subject uses numbers?": "math"}
# for q in quiz:
#     x = input(q+"\n").lower()
#     if x == quiz[q]:
#         print("correct")
#     else: 
#         print("incorrect")
# var = input("whats ur name?")

quiz = {"what year is it?": str(2026), "what subject uses numbers?": "math"}
wrong = 0
for q in quiz:
    flag = True
    while flag:
        x = input(q+"\n").lower()
        if x == quiz[q]:
            print("correct")
            flag = False
        else: 
            print("incorrect")
            wrong += 1
print(f"you got {wrong} incorrect guesses")




 
# import random
# number = random.randint(0,50)
# wrong = 0
# flag = True
# while flag:
#     guess = int(input("guess a number: \n"))
#     if number > guess:
#         wrong += 1
#     elif number < guess:
#         wrong += 1
#     else:
#         print("you guessed the number")
#         print(f"you got {wrong} incorrect guesses")
#         flag = False



