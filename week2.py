names = ["rashi","sachin","janvi","surya","sarthak","prince","devansh","kartikeya","bob","adam","fisher"]
print(names[0])
print(names[-1])
print(names[2:5])
print(names[::-1])
print(names[7:1:-1])

stu = ("doe","jane","alice","joe","john")
print(stu)
new = "conrad"
stu = stu + (new,)
print(stu)

students_list = list(stu)
students_list.remove("john") 
stu = tuple(students_list)
print(stu)
print(stu[1:4])

students_list = list(stu)
students_list[2] = "Chris" 
stu = tuple(students_list)
print(stu)

friends = {
    "rashi": 20,
    "alice": 19,
    "Charlie": 21,
    "David": 18,
    "Eva": 25
}

for name,age in friends.items():
    if age>20:
        print(name,age)

friends["janvi"]=30
print(friends)

del friends["alice"]
print(friends)

average_age = sum(friends.values()) / len(friends)
print("Average Age:", average_age)

nums = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 1]
duplicates = set([x for x in nums if nums.count(x) > 1])
print("Duplicate elements:", duplicates)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict

anagram_dict = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagram_dict[key].append(word)

print("Anagrams:")
for group in anagram_dict.values():
    if len(group) > 1:
        print(group)