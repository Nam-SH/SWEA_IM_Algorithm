char = 'a_pattern_matching-algorithm'
for i in range(len(char)):
    if char[i] == 'm':
        if char[i-4:i+1] == 'rithm':
            print(char[i-4:i+1])
            print('끝')
    if char[i] == 'h':
        i += 1
    if char[i] == 't':
        i += 2
    if char[i] == 'i':
        i += 3
    if char[i] == 'r':
        i += 4
    else:
        i += 5
