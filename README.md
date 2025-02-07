## Python Basic Programming Exercises

### Overview
Welcome to my Data Analytics Portfolio! This repository showcases fundamental Python programming exercises designed to sharpen problem-solving and data manipulation skills. The exercises cover numerical operations, control structures, user-defined functions (UDFs), list manipulations, and more.

These foundational concepts are essential for data analytics, enabling efficient data processing and transformation. Recruiters and data enthusiasts can explore my work to understand my approach to coding, logic-building, and problem-solving in Python.

---

## 📌 Project Highlights
### 1️⃣ Arithmetic Operations in Python
**Question:** What is the output of the following expression?
```python
5 + 4 * 9 % (3 + 1) / 6 - 1
```
**Solution:**
```python
result = 5 + 4 * 9 % (3 + 1) / 6 - 1
print(result)  # Output: ??
```
---

### 2️⃣ Checking Odd or Even Number
**Question:** Write a program to check if a number is odd or even.
```python
num = int(input("Enter the number here: "))
print(num, "is even") if num % 2 == 0 else print(num, "is odd")
```
---

### 3️⃣ Multiplication Table Generator
**Question:** Write a program to display the multiplication table of a given number.
```python
num = int(input("Enter your number here: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
```
---

### 4️⃣ Finding Numbers Divisible by 7 but Not by 5
**Question:** Find all numbers between 2000 and 3200 that are divisible by 7 but not multiples of 5.
```python
result = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(",".join(map(str, result)))
```
---

### 5️⃣ Counting Data Types in a List
**Question:** Count the elements of each data type in a given list.
```python
l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
types_count = {"int": 0, "float": 0, "str": 0, "bool": 0}

for item in l:
    if isinstance(item, int):
        types_count["int"] += 1
    elif isinstance(item, float):
        types_count["float"] += 1
    elif isinstance(item, str):
        types_count["str"] += 1
    elif isinstance(item, bool):
        types_count["bool"] += 1

print(types_count)
```
---

### 6️⃣ Summing Numeric Values in a List
**Question:** Sum all numeric values (int and float) in a given list.
```python
l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
total = sum(i for i in l if isinstance(i, (int, float)))
print(total)
```
---

### 7️⃣ Concatenating String Elements
**Question:** Concatenate all string elements in a list with a hyphen.
```python
l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
result = "-".join(str(i) for i in l if isinstance(i, str))
print(result)
```
---

### 8️⃣ User-Defined Function (UDF) for List Operations
**Question:** Create a function that returns the sum of all numeric values and counts all string elements in a list.
```python
def process_list(l):
    num_sum = sum(i for i in l if isinstance(i, (int, float)))
    str_count = sum(1 for i in l if isinstance(i, str))
    return {"Sum": num_sum, "Count_of_Strs": str_count}

l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
print(process_list(l))
```
---

### 🔢 More Exercises Covered:
✔️ Odd Number Extraction Using Loop, List Comprehension & Lambda Functions
✔️ UDF for Statistical Summary (Sum, Count, Min, Mean, Max)
✔️ Area Calculation for Different Shapes (Square, Rectangle, Circle)
✔️ List Reconciliation (Find Common & Unique Elements in Two Lists)
✔️ Prime Number Checker Using UDF
✔️ Factorial Calculation Using Recursion
✔️ Generating Dictionary of Squares
✔️ Converting Comma-Separated Inputs into List & Tuple
✔️ Sorting Words Alphabetically & Removing Duplicates
✔️ Counting Uppercase & Lowercase Letters in a Sentence



## 🎯 Key Takeaways
✅ Strong foundation in Python programming
✅ Logical thinking and problem-solving skills
✅ Essential programming concepts for data analytics

---


