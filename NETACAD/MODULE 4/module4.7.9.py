try:
    with open('missing_practice_file.txt','r',encoding='utf-8') as file: print(file.read())
except FileNotFoundError: print('File was not found')
