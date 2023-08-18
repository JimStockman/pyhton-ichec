txt = 'ICHEC Brussels Management School'
counter = 0
for letter in txt:
    if letter == letter.upper() and letter != ' ':
        counter += 1
print(counter)
