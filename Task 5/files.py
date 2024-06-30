with open('example.bin', 'wb') as file:
    file.write(b'This is a byte string')


with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('This is a Unicode string')

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)