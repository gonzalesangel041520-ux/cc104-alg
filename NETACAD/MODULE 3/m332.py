# Example 1:
value = 5
print(value > 0)
print(not (value <= 0))

# Example 2:
value = 0
print(value != 0)
print(not (value == 0))

# De Morgan's laws
p = True
q = False
print(not (p and q) == ((not p) or (not q)))
print(not (p or q) == ((not p) and (not q)))

