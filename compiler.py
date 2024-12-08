from lexer import tokenize
from parser import parse

# Read input file
with open('examples/test.mylang', 'r') as file:
    code = file.read()

# Tokenize and parse
tokens = tokenize(code)
html = parse(tokens)

# Save output
with open('output.html', 'w') as file:
    file.write(html)

print("HTML generated successfully! Open output.html to view it.")
