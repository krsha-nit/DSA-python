num1 = 11
num2 = num1
print("Before: ",num1,num2)
num1 = 20
print("After: ",num1,num2)


#But in case of dictionary
dict1 = {"k1": 40}
dict2 = dict1
print("Before: ", dict1, dict2)
dict1['k1'] = 100
print("After: ", dict1, dict2)