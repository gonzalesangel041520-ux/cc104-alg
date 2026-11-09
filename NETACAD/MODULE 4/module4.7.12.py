raw=['10','20','bad','30']
valid=[]
for text in raw:
    try: valid.append(int(text))
    except ValueError: print('Skipped:',text)
print(valid,sum(valid))
