substitution_mapping = {
    'A': 'N',
    'B': 'J',
    'C': 'A',
    'D': 'B',
    'E': 'Y',
    'F': 'O',
    'G': 'F',
    'H': 'W',
    'I': 'L',
    'J': 'Z',
    'K': 'M',
    'L': 'P',
    'M': 'X',
    'N': 'I',
    'O': 'K',
    'P': 'U',
    'Q': 'V',
    'R': 'C',
    'S': 'D',
    'T': 'E',
    'U': 'G',
    'V': 'R',
    'W': 'Q',
    'X': 'S',
    'Y': 'T',
    'Z': 'H'
}

def encipher_text(text):
    def get_substitution(c):
        upper = c.isupper()
        substitution = substitution_mapping.get(c.upper(), c)
        return substitution.upper() if upper else substitution.lower()
    return "".join(get_substitution(c) for c in text)


print(encipher_text(input()))