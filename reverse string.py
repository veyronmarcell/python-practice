def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))text))
