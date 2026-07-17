lst = [1, 3, 5, 7, 9, 11, 11, 11, 11, 11, 11, 11, 11, 13]

# print(lst[6: : -3])
# product = 1
# for val in lst:
#     product *= val
# print(f"the sum of all the numbers is {product}")

# this is how to find out the length of the list ->

# len(lst)
# print(len(lst))

# finding if a value is in a list or not ->

# print(2 in lst)
# print(9 not in lst)

# adding to the end of a list ->

# lst.append(11)
# print(lst)
# lst.sort(reverse=True)
# lst.sort(reverse=False)
# print(lst)
# lst.append([15, 17])
# print(lst)
# lst.extend([1, 5, 74, 23])
# print(lst)

# first part in the bracket is the index, second is the value ->
# lst.insert(2, 10)
# print(lst)
# # lst.reverse()
# # print(lst)
# # x = lst.index(13)
# # print(x)

# big = 0
# for val in lst:
#     if val > big:
#         big = val
# print(f"the greatest value is {big}")

# small = lst[0]
# for i in lst:
#     if i < small:
#         small = i
# print(f"the smallest value is {small}")

lst.count(11)
print(lst.count(11))
lst.index(11)
print(lst.index(11))