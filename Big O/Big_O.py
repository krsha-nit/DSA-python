# 1. O(n) - for loop (n operations)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

## Rule1: drop constants - O(2n) = O(n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

# 2. O(n**2) - nested for loops
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)

## Rule2: This is also O(n**2) and not O(n**3)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(10)

## Rule3: drop Non dominanat terms. O(n**2) + O(n) ~ O(n**2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)

# 3. O(1) - one operation
def add_items(n):
    return n + n + n
 

print(add_items(10))

# 4. Different terms - miscellenanous items
## O(a+b) as we don't know a==b==n
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)

## O(a*b) and not O(n**2) with same reason
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)