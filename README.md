# 🐍 Python Basic Programming Exercises  

## 📌 Project Overview  
This project is a collection of Python programming exercises designed to enhance fundamental coding skills in data analytics. It covers numerical operations, control structures, data handling, and user-defined functions (UDFs), making it an essential component of a **data analytics portfolio**.  

---

## 🛠️ Tools & Techniques  
- **Language**: Python  
- **Libraries**: `pandas`, `numpy`  
- **Concepts Covered**:  
  - Arithmetic & logical operations  
  - Conditional statements & loops  
  - List & dictionary manipulations  
  - String operations  
  - Custom functions & lambda expressions  
  - Data validation & error handling  

---

## 🔍 Key Exercises  

# 1️⃣ Mathematical & Logical Operations
```python
result = 5 + 4 * 9 % (3 + 1) / 6 - 1
print(result)  # Output: 5.0

num = int(input("Enter a number: "))
print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")

num1 = int(input("Enter your number here: "))
for i in range(1, 11):
    print(f"{num1} * {i} = {num1 * i}")

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
```
# 2️⃣ List & Dictionary Operations
```python
l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
integer, string, floatt, boolean = [], [], [], []
for i in l:
    if type(i) == int:
        integer.append(i)
    elif type(i) == float:
        floatt.append(i)
    elif type(i) == str:
        string.append(i)
    else:
        boolean.append(i)
print("Integer:", integer, "Float:", floatt, "String:", string, "Boolean:", boolean)

ass = sum(i for i in l if isinstance(i, (int, float)))
print("Sum of numeric values:", ass)

strt = "-".join([i for i in l if isinstance(i, str)])
print("Concatenated string:", strt)

def summarize_list(l1):
    num, string = 0, 0
    for i in l1:
        if isinstance(i, (int, float)):
            num += i
        elif isinstance(i, str):
            string += 1
    return {"Sum": num, "Count_of_Strs": string}
print(summarize_list(l))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print([i for i in li if i % 2 != 0])
print(list(filter(lambda x: x % 2 != 0, li)))
```

# 3️⃣ Function Implementations
```python
def get_descriptives(lis):
    return {"Sum": sum(lis), "Count": len(lis), "Min": min(lis), "Max": max(lis), "Mean": np.mean(lis)}
print(get_descriptives([5, 7, 22, 97, 54, 62, 77, 23, 73, 61]))

def calculate_area(shape, **kwargs):
    if shape == "square" and "side" in kwargs:
        return kwargs["side"] ** 2
    elif shape == "rectangle" and "length" in kwargs and "width" in kwargs:
        return kwargs["length"] * kwargs["width"]
    elif shape == "circle" and "radius" in kwargs:
        return 3.14 * kwargs["radius"] ** 2
    else:
        return "Invalid input"
print(calculate_area("square", side=5))

def reconcile_lists(l1, l2):
    s1, s2 = set(l1), set(l2)
    return {"Matched": list(s1 & s2), "Only in l1": list(s1 - s2), "Only in l2": list(s2 - s1)}
print(reconcile_lists(['January', 'February', 'March', 'May'], ['January', 'February', 'April', 'June']))

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) and n > 1
print(is_prime(7))

def factorial(n):
    return 1 if n in [0, 1] else n * factorial(n - 1)
print(factorial(8))

def generate_squared_dict(n):
    return {i: i ** 2 for i in range(1, n + 1)}
print(generate_squared_dict(8))

num = input("Enter numbers separated by commas: ")
list_nums = num.split(",")
tuple_nums = tuple(list_nums)
print(list_nums, tuple_nums)

csv = input("Enter words separated by commas: ")
print(",".join(sorted(csv.split(","))))

words = "hello world and practice makes perfect and hello world again"
print(" ".join(sorted(set(words.split()))))

sent = input("Enter a sentence: ")
uppercase, lowercase = sum(1 for i in sent if i.isupper()), sum(1 for i in sent if i.islower())
print("UPPER CASE", uppercase, "LOWER CASE", lowercase)
```
