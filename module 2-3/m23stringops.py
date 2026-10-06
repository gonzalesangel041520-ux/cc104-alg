s = "hello world"

# O(1) access - strings are arrays of chars
print("First char:", s[0]) # 'h' - instant

# O(n) traversal - visits each char
for c in s:
    print(c, end=" ") # h e l l o w o r l d

# O(n) concatenation - creates a brand new string
s2 = s + "!!!" # has to copy 11 chars + 3 new = 14 ops
print("\nConcatenated:", s2) # hello world!!!

# O(n) substring search - scans for "world"
print("Contains 'world'?", "world" in s) # True