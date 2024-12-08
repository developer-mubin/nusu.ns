import re

def tokenize(code):
    tokens = []
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        match = re.match(r'(\w+):\s*(.*)', line)
        if match:
            tokens.append((match.group(1), match.group(2)))
    return tokens
