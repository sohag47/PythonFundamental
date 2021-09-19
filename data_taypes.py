"""
! python Data types
1. text: string
2. numeric : int, float, complex
3. sequence: list, tuple, range
4. mapping: dict
5. set: set, frozenset
6. boolean : bool
7. binary: bytes, bytearray, memoryview
8. empty value: None
"""

#? 1. text type: string
text_type = "Minhazul Islam Sohag"
print(text_type , type(text_type))

#? 2. numeric : int, float, complex
int_type = 24
print(int_type, type(int_type))

float_type = 20.5
print(float_type, type(float_type))

complex_type = 1j
print(complex_type, type(complex_type))

#? 3. sequence: list, tuple, range
list_type = ["apple", "banana", "cherry"]
print(list_type, type(list_type))

tuple_type = ("apple", "banana", "cherry")
print(tuple_type, type(tuple_type))

range_type = range(6)
print(range_type, type(range_type ))

#? 4. mapping: dict
dict_type = {"name" : "John", "age" : 36}
print(dict_type, type(dict_type ))

#? 5. set: set, frozenset
set_type = {"apple", "banana", "cherry"}
print(set_type, type(set_type ))

frozenset_type = frozenset({"apple", "banana", "cherry"})
print(frozenset_type, type(frozenset_type ))

#? 6. boolean : bool
bool_type = True
print(bool_type, type(bool_type))

#? 7. binary: bytes, bytearray, memoryview
byte_type = b"Hello"
print(byte_type, type(byte_type))

bytearray_type = bytearray(5)
print(bytearray_type, type(bytearray_type))

memoryview_type = memoryview(bytes(5)) 
print(memoryview_type, type(memoryview_type))

empty_value = None
print(empty_value, type(empty_value))