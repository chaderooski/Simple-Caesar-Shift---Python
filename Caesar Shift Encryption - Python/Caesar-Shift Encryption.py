inputText = input("What is the plain text message? ")
inputKey = int(input('What is the key you want to change the letters by? '))

final = []

for letter in inputText:
    if ord(letter) > ord('a') - 1 and ord(letter) < ord('z') + 1:
        letter = ord(letter) + inputKey
        if letter > 122:
            letter = (letter - 123) + 97
        final.append(chr(letter))
    else:
        print(f'''Your letter "{letter}" is not within the given parameters''')

print(''.join(final))