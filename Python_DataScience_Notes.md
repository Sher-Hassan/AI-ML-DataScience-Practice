# Python & Data Science Notes

---

## 1. Environment Setup

It is always a good practice to start with creating a separate environment.

### Three Ways to Create Virtual Environments

#### 1. Using `venv` Module

```bash
python -m venv venv_name
venv_name\Scripts\activate      # Activate
deactivate                       # Deactivate
```

#### 2. Using `virtualenv` (Linux / PowerShell / Git Bash)

```bash
pip install virtualenv
virtualenv -p python3 venv_name
venv_name\Scripts\activate      # Activate
deactivate                       # Deactivate
```

#### 3. Using Anaconda *(Recommended)*

```bash
conda create -p venv_name python==3.14 -y    # Can use other versions
conda activate venv/                          # Activate
conda deactivate                              # Deactivate
```

### Setting Up with Anaconda (Step-by-Step)

- Open command prompt / terminal in VS Code
- Run: `conda create -p venv python==3.14`
- Type `y` to confirm → environment created
- Add a `requirements.txt` file
- Add package names inside `requirements.txt`
- Activate: `conda activate venv/`
- Install packages from file: `pip install -r requirements.txt`
- **Jupyter Notebook** (`.ipynb`) requires two packages: `ipykernel` + Jupyter extension
- Click on "detecting kernels" in `.ipynb` file and select the created environment

---

## 2. Python Modules and Packages

Helps organize and reuse code.

### Importing Modules

```python
# Way 1 — import the whole module
import math
math.sqrt(16)

# Way 2 — import specific functions
from math import sqrt, pi
print(sqrt(16))
print(sqrt(25))
print(pi)

# Importing everything
from math import *
print(sqrt(16))
print(pi)

# Using an alias
import numpy as np     # np is the alias
np.array([1, 2, 3])    # access numpy with np.
```

### Creating Your Own Custom Module / Package

- Make a folder (e.g. `package/`)
- Inside it, create a special file: **`__init__.py`** (makes Python treat the folder as a package)
- Create your module file inside: `package/maths.py`
- Define your functions inside that file

```python
# Calling your custom module
from package.maths import addition
addition(2, 3)

# OR
from package import maths
maths.addition(2, 3)
```

**Syntax:**
```
from folder_name.package_name import function_name
```

> **Note:** For subpackages (nested folders), place an `__init__.py` in each subfolder too.

```python
from folder_name.subpackageFolder_name.packagename import function_name
function_name()
```

---

## 3. Python Standard Library Overview

In Python, the standard library is a big collection of built-in modules that come with Python itself — no extra installs needed. Think of it as Python's **"batteries included"** toolbox.

### `array` — Basic Arrays

```python
import array
arr = array.array('i', [1, 2, 3, 4])
print(arr)
```

### `math` — Mathematical Functions

```python
import math
math.sqrt(16)
```

### `random` — Random Values

```python
import random
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))
```

### `os` — Operating System / IO Operations

```python
import os
print(os.getcwd())
os.mkdir('test_dir')
```

### `shutil` — High-Level File Operations

```python
import shutil
shutil.copyfile('source.txt', 'destination.txt')
```

### `json` — Data Serialization (used in APIs)

```python
import json

data = {'name': 'Sher', 'age': 25}
json_str = json.dumps(data)        # Dict → JSON string
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str) # JSON string → Dict
print(parsed_data)
print(type(parsed_data))
```

> **Result:**
> ```
> {"name": "Sher", "age": 25}
> <class 'str'>
> {'name': 'Sher', 'age': 25}
> <class 'dict'>
> ```

### `csv` — Working with CSV Files

```python
import csv

with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Sher', '20'])

with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### `datetime` — Date and Time

```python
from datetime import datetime, timedelta    # timedelta is used for time changes

now = datetime.now()
print(now)

yesterday = now - timedelta(days=1)
print(yesterday)
```

### `time` — Time / Sleep

```python
import time
print(time.time())
time.sleep(2)          # Program sleeps for 2 seconds
print(time.time())
```

### `re` — Regular Expressions

`re` lets you search, match, split, and replace text using patterns (regex).

```python
import re

pattern = r'\d+'
text = 'There are 212 apples'
match = re.search(pattern, text)
print(match.group())
```

> **Result:**
> ```
> 212
> ```

### F-Strings

```python
x = 10
print(f"my score is {x}")
```

---

## 4. Working with File Paths

### Listing Directory Contents

```python
import os
items = os.listdir('.')
print(items)
```

### Joining Paths

```python
import os

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name, file_name)
full_final_path = os.path.join(os.getcwd(), dir_name, file_name)
print(full_path)
print(full_final_path)
```

### Checking if a File Exists

```python
import os

path = 'example1.txt'
if os.path.exists(path):
    print(f"The path '{path}' exists")
else:
    print(f"The path '{path}' does not exist")
```

### Checking if Path is a File or Directory

```python
import os

path = 'Notes.txt'
if os.path.isfile(path):
    print(f"'{path}' is a file")
elif os.path.isdir(path):
    print(f"'{path}' is a directory")
else:
    print(f"'{path}' is neither a directory nor a file")
```

### Getting the Absolute Path

```python
relative_path = 'Notes.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
```

> **Note:** This is better than manually joining with `os.path.join(os.getcwd(), ...)`.

---

## 5. Exception Handling

### Basic `try-except` Block

```python
try:
    a = b
except:
    print("Variable not assigned")
```

### Displaying the Error Type

```python
try:
    a = b
except NameError as ex:
    print(ex)
```

**Syntax:**
```python
try:
    # code
except ErrorType as alias:
    print(alias)
```

### Catching Specific Exceptions

```python
# ZeroDivisionError
try:
    result = 1 / 0
except ZeroDivisionError as err:
    print("Enter denom greater than 0")
```

### Multiple `except` Blocks

> **Note:** All error types derive from the base `Exception` class — always put `Exception` **last**.

```python
try:
    numb = int(input("Enter a value: "))
    res = 10 / numb
except ValueError:
    print("Enter valid value")
except ZeroDivisionError:
    print("Enter greater than 0")
except Exception as ex:
    print(ex)
```

### `try`, `except`, and `else`

`else` executes **only if** `try` runs successfully without triggering any `except` block.

```python
try:
    numb = int(input("Enter a value: "))
    res = 10 / numb
except ValueError:
    print("Enter valid value")
except ZeroDivisionError:
    print("Enter greater than 0")
except Exception as ex:
    print(ex)
else:
    print(f"The value is {res}")
```

### `try`, `except`, `else`, and `finally`

`finally` executes **no matter what** — whether the `try` succeeded or an exception was caught.

```python
try:
    numb = int(input("Enter a value: "))
    res = 10 / numb
except ValueError:
    print("Enter valid value")
except ZeroDivisionError:
    print("Enter greater than 0")
except Exception as ex:
    print(ex)
else:
    print(f"The value is {res}")
finally:
    print("Execution completed")
```

---

## 6. NumPy

NumPy is a fundamental library for scientific computing in Python. It provides support for arrays and matrices, along with a collection of mathematical functions to operate on these data structures.

```python
import numpy as np
```

### Creating Arrays

#### 1D Array

```python
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))       # Not a list!
print(arr1.shape)       # (5,) — no rows/columns in 1D
```

#### Reshaping a 1D Array to 2D

```python
arr2 = np.array([1, 2, 3, 4, 5])
arr2.reshape(1, 5)      # 1 row, 5 columns → array([[1, 2, 3, 4, 5]])
```

> Two `[[]]` brackets = 2D array, three `[[[]]]` = 3D array.

#### 2D and 3D Arrays

```python
arr3 = np.array([[1, 2, 3, 4, 5]])           # 2D — one row
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # 2D — two rows
print(arr4.shape)    # (2, 4) → 2 rows, 4 columns
```

#### Inbuilt Array Creation Functions

```python
np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
np.arange(0, 10, 2).reshape(5, 1)  # Reshape to 5 rows, 1 column

np.ones((3, 4))    # 3x4 array of 1s
np.eye(3)          # 3x3 identity matrix
```

### Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)
print("Shape:", arr.shape)                    # (2, 3)
print("Number of dimensions:", arr.ndim)      # 2
print("Size (number of elements):", arr.size) # 6
print("Data type:", arr.dtype)                # int64
print("Item size (in bytes):", arr.itemsize)  # 8
```

### Vectorized Operations

```python
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
# Similarly: multiplication, division, etc.
```

### Universal Functions

Functions that apply to the **entire array** at once.

```python
arr = np.array([2, 3, 4, 5, 6])

print(np.sqrt(arr))   # Square root
print(np.exp(arr))    # Exponential
print(np.sin(arr))    # Sine
print(np.log(arr))    # Natural log
```

### Array Slicing and Indexing

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

arr[0][0]          # Single element → 1
arr[1:, 2:]        # Pick 7, 8, 11, 12
arr[0:2, 2:4]      # Pick 3, 4, 7, 8
```

### Modifying Array Elements

```python
arr[0, 0] = 100        # Modify single element
arr[1:] = 99           # Set all rows from index 1 to 99
arr[1:3, 2:4] = 34     # Modify a slice
```

### Statistical Concepts — Normalization

```python
data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)
std_dev = np.std(data)
normalized_data = (data - mean) / std_dev

print(normalized_data)
```

### Statistical Operations

```python
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
```

### Logical Operations

```python
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

data[(data >= 5) & (data <= 8)]    # Elements between 5 and 8
# Any logical operation can be used: &, |, ~
```

---

## 7. Pandas — Data Manipulation Library

Pandas is a powerful data manipulation library in Python, widely used for data analysis and cleaning. It provides two primary data structures:

- **Series** — One-dimensional array-like object
- **DataFrame** — Two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns)

```python
import pandas as pd
```

---

### 7.1 Pandas Series

A Pandas Series is a one-dimensional array-like object that can hold any data type. Similar to a column in a table.

#### From a List

```python
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series \n", series)
print(type(series))
```

> **Result:**
> ```
> 0    1
> 1    2
> 2    3
> 3    4
> 4    5
> dtype: int64
> <class 'pandas.core.series.Series'>
> ```

#### From a Dictionary

```python
data = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data)
print(series_dict)
```

> **Result:**
> ```
> a    1
> b    2
> c    3
> dtype: int64
> ```

> Keys become the index, values are the series values.

#### With a Custom Index

```python
data = [10, 20, 30]
index = ['a', 'b', 'c']
pd.Series(data, index=index)
```

> **Result:**
> ```
> a    10
> b    20
> c    30
> dtype: int64
> ```

---

### 7.2 Pandas DataFrame

A Pandas DataFrame is a two-dimensional, size-mutable, tabular data structure with labeled axes.

#### Reading Data

| Method | Use |
|---|---|
| `pd.read_csv()` | CSV or delimited text files |
| `pd.read_excel()` | `.xlsx` / `.xls` files (supports multiple sheets) |
| `pd.read_json()` | Web-based JSON data |
| `pd.read_sql()` | SQL databases (PostgreSQL, MySQL, SQLite) |

#### Creating a DataFrame from a Dictionary of Lists

```python
data = {
    'Name': ['Sher', 'Hassan', 'Khan'],
    'Age':  [18, 19, 20],
    'City': ['Quetta', 'Islamabad', 'Zhob']
}
df = pd.DataFrame(data)
print(df)
```

> **Result:**
> ```
>      Name  Age       City
> 0    Sher   18     Quetta
> 1  Hassan   19  Islamabad
> 2    Khan   20       Zhob
> ```

#### Creating a DataFrame from a List of Dictionaries

```python
data1 = [
    {'Name': 'Sher',   'Age': 20, 'City': 'Quetta'},
    {'Name': 'Hassan', 'Age': 20, 'City': 'Islamabad'},
    {'Name': 'Khan',   'Age': 20, 'City': 'Zhob'},
    {'Name': 'Ali',    'Age': 20, 'City': 'Karachi'}
]
df1 = pd.DataFrame(data1)
print(df1)
```

> **Result:**
> ```
>      Name  Age       City
> 0    Sher   20     Quetta
> 1  Hassan   20  Islamabad
> 2    Khan   20       Zhob
> 3     Ali   20    Karachi
> ```

#### Reading a CSV File

```python
df = pd.read_csv('sales_data.csv')
print(df.head(5))    # First 5 rows
print(df.tail(5))    # Last 5 rows
```

---

### 7.3 Accessing Data from a DataFrame

```python
df['Name']              # Access a column (returns Series)
df.loc[0]               # Access row by label/index
df.iloc[0]              # Access row by position
df.loc[0, 'Name']       # Specific element by label
df.iloc[0, 2]           # Specific element by position
df.at[1, 'Age']         # Element with .at (label-based)
df.iat[1, 2]            # Element with .iat (position-based)
```

---

### 7.4 Data Manipulation with DataFrame

#### Adding a New Column

```python
df['Salary'] = [50000, 60000, 70000, 80000]
```

#### Removing a Column

```python
df.drop('Salary', axis=1)             # axis=1 for columns
df.drop(columns=['Salary'])           # Alternative
df = df.drop(columns=['Salary'])      # Save changes
df.drop('Salary', axis=1, inplace=True)  # In-place
```

> **Note:** Default `axis=0` removes rows, not columns!

#### Modifying Column Values

```python
df['Age'] = df['Age'] + 1
```

#### Removing a Row

```python
df.drop(3, inplace=True)    # Remove row at index 3
```

#### Statistical Summary

```python
df.describe()
```

> **Result:**
> ```
>          Age    Salary
> count    3.0     3.0
> mean    21.0  60000.0
> std      1.0  10000.0
> min     20.0  50000.0
> 25%     20.5  55000.0
> 50%     21.0  60000.0
> 75%     21.5  65000.0
> max     22.0  70000.0
> ```

---

### 7.5 Data Manipulation and Analysis

#### Checking Data Types

```python
df.dtypes
```

#### Handling Missing Values

```python
df.isnull()               # True where entries are missing
df.isnull().any(axis=1)   # Which rows have missing values
df.isnull().sum()         # Count of missing values per column
```

> **Result:**
> ```
> Unit Price    4
> ...all others: 0
> ```

#### Filling Missing Values

```python
df.fillna(0)    # Fill all NaN with 0

# Fill with the column mean
df['Unit_Price_fillNA'] = df['Unit Price'].fillna(df['Unit Price'].mean())
```

#### Renaming Columns — `.rename()`

```python
# Syntax: df.rename(columns={'OldName': 'NewName'})
df = df.rename(columns={'Country': 'Nationality'})
```

#### Changing Data Types — `.astype()`

```python
# Convert Units Sold from int to float
df['New Units Sold'] = df['Units Sold'].astype(float)
```

#### Applying Functions — `.apply()`

```python
df['New Value'] = df['New Units Sold'].apply(lambda x: x * 2)
```

---

### 7.6 Data Aggregation and Grouping

#### Group by One Column

```python
grouped_mean = df.groupby('Region')['Unit Cost'].mean()
print(grouped_mean)
```

> **Result:**
> ```
> Region
> Asia                                 239.587273
> Australia and Oceania                154.744545
> Central America and the Caribbean    157.817143
> Europe                               223.166364
> Middle East and North Africa         152.450000
> North America                        205.293333
> Sub-Saharan Africa                   183.677500
> Name: Unit Cost, dtype: float64
> ```

#### Group by Two Columns

```python
grouped_sum = df.groupby(['Region', 'Item Type'])['Unit Cost'].sum()
print(grouped_sum)
```

#### Aggregate Multiple Functions

```python
grouped_agg = df.groupby('Region')['Unit Cost'].agg(['mean', 'sum', 'count'])
print(grouped_agg)
```

> **Result:**
> ```
>                                         mean       sum  count
> Region
> Asia                               239.587273   2635.46     11
> Australia and Oceania              154.744545   1702.19     11
> Central America and the Caribbean  157.817143   1104.72      7
> Europe                             223.166364   4909.66     22
> Middle East and North Africa       152.450000   1524.50     10
> North America                      205.293333    615.88      3
> Sub-Saharan Africa                 183.677500   6612.39     36
> ```

---

### 7.7 Merging and Joining DataFrames

```python
df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'D'], 'Value1': [4, 5, 6]})
```

#### Inner Join — only matching keys

```python
pd.merge(df1, df2, on="Key", how="inner")
```

> **Result:**
> ```
>   Key  Value1_x  Value1_y
> 0   A         1         4
> 1   B         2         5
> ```

#### Outer Join — all keys, NaN where no match

```python
pd.merge(df1, df2, on="Key", how="outer")
```

> **Result:**
> ```
>   Key  Value1_x  Value1_y
> 0   A       1.0       4.0
> 1   B       2.0       5.0
> 2   C       3.0       NaN
> 3   D       NaN       6.0
> ```

#### Left Join — all keys from left DataFrame

```python
pd.merge(df1, df2, on="Key", how="left")
```

> **Result:**
> ```
>   Key  Value1_x  Value1_y
> 0   A         1       4.0
> 1   B         2       5.0
> 2   C         3       NaN
> ```

#### Right Join — all keys from right DataFrame

```python
pd.merge(df1, df2, on="Key", how="right")
```

> **Result:**
> ```
>   Key  Value1_x  Value1_y
> 0   A       1.0         4
> 1   B       2.0         5
> 2   D       NaN         6
> ```

---

*End of Notes*
