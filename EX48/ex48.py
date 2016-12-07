def scan(userinput):
    words = userinput.split()
    result = []
    for word in words:
        result.append(classify(word))
    return result

def classify(word):
    if word in ['north', 'south', 'east']:
        return ('direction', word)
    elif word in ['go', 'kill', 'eat']:
        return ('verb', word)
    elif word in ['the, 'in', 'of']:
        return ('stop', word)
    elif word in ['bear', 'princess']:
        return ('noun', word)
    elif word in ['', '', '']:
        return ('number', word)
    else:
#program reacts to error instead of just error
        try:
            thenumber = int(word)
            return('number', thenumber)
        except ValueError:
            # word is not a number
            return('error', word)
