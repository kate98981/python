str_type = "hello"
int_type = 1
float_type = 2.05
bytes_type = bytes("Катя", encoding="UTF-8")
list_type = ['hi', 12, 2.0]
type_turp = ("Kate", 23, 8 + 8j)
set_type = {1, 2, 3, type_turp, float_type}
frozenset_type = frozenset({'a', 'b', 'c'})
dict_type = {1: 'cat', 2: 'dog'}

print("str_type = ", str_type, type(str_type))
print("int_type = ", int_type, type(int_type))
print("float_type = ", float_type, type(float_type))
print("bytes_type = ", bytes_type, type(bytes_type))
print("list_type = ", list_type, type(list_type))
print("type_turp = ", type_turp, type(type_turp))
print("set_type = ", set_type, type(set_type))
print("frozenset_type = ", frozenset_type, type(frozenset_type))
print("dict_type = ", dict_type, type(dict_type))

str1 = "hello "
str2 = "world"
str_res = str1 + str2
print(str_res)

str3 = "age"
age = 23
print(str3 + "," + str(age))

str4 = "world "
year = 2022
print(str4 + str(year))
