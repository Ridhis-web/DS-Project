# Reverse string
t = "ridhima"
print(t[::-1])

#Check for Palindrome 
def is_palindrome(string):
    return string == string[::-1]
word = "madam"
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")

#Find Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1) 
num = 5
print("Factorial of", num, "is", factorial(num))

#Generate Fibonacci Series (Iterative)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(5)

#Check if a Number is Prime
num = 7  
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")

#Find GCD of Two Numbers
a = 20
b = 28
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD of", a, "and", b, "is", gcd)

#Count Vowels in a String
string = "hello world"
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#Find Duplicate Elements in a List
my_list = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements are:", duplicates)

#Check if Two Strings are Anagrams
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")

#Merge Two Sorted Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = sorted(list1 + list2)
print("Merged Sorted List:", merged_list)

#Find Missing Number in Range 1 to n
num = [1, 2, 3, 4, 5, 6, 8, 9, 10]
n = 10 
expected_sum = n * (n + 1) // 2
actual_sum = sum(num)
missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)

#Check if a Number is an Armstrong Number
num = 259
num_digits = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")

#Check if a String is a Pangram
text = "The quick brown fox jumps over the lazy dog"
text = text.lower()
count = 0
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char in text:
        count += 1
if count == 26:
    print("Pangram")
else:
    print("Not a Pangram")

#Remove Duplicates from a List
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)

#Find the Second Largest Number in a List in easy
numbers = [10, 20, 40, 30, 40]
largest = second = float('-inf')
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest number is:", second)

#Count Occurrences of Elements in a List
my_list = [1, 2, 2, 3, 1, 4, 2, 3]
count_dict = {}

for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Element counts:", count_dict)

#Transpose a Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])
transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)
print("Transposed Matrix:")
for row in transpose:
    print(row)

#Implement Linear Search
numbers = [10, 20, 30, 40, 50]
target = 30
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found")

#Implement Binary Search
numbers = [10, 20, 30, 40, 50]
target = 30
low = 0
high = len(numbers) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Element found at index:", mid)
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")

#Find Intersection of Two List
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
a = []
for item in list1:
    if item in list2:
        a.append(item)
print("Intersection:", a)

#Flatten a Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Flattened List:", flat_list)

#Count Number of Words in a String
text = "Python is very easy to learn"
words = text.split()
print("Number of words:", len(words))

#Implement String Compression (a3b2c2)
text = "aaabbcc"
result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)  # last character
print("Compressed string:", result)

#Print Pascal’s Triangle up to n Rows
def pascal_triangle(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()
pascal_triangle(5)

#Find the Majority Element in a List in easy
nums = [1, 2, 1, 1, 3, 1, 1]
n = len(nums)

for num in nums:
    if nums.count(num) > n // 2:
        print("Majority element is:", num)
        break
else:
    print("No majority element")

#Move All Zeros to End of List
nums = [0, 1, 0, 3, 12]
new_list = []
for num in nums:
    if num != 0:
        new_list.append(num)
for num in nums:
    if num == 0:
        new_list.append(num)
print("After moving zeros:", new_list)

#Implement a Stack using List
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)
popped = stack.pop()
print("Popped:", popped)
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")
print("Is stack empty?", len(stack) == 0)

#Rotate a List by k Elements
nums = [1, 2, 3, 4, 5]
k = 2
k = k % len(nums)
rotated = nums[-k:] + nums[:-k]
print("Rotated List:", rotated)

#Check if a List is Sorted
a = [1, 2, 3, 4, 5]
if a== sorted(a):
    print("List is sorted")
else:
    print("List is not sorted")
