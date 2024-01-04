import re
Input = input("Enter your code: ")
token_specification = {
        'KEYWORD': r'int|float|char|if|else|while|for|return',
        'OPERATOR': r'\+|-|\*|/|=|<|>|!',
        'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'NUMBER': r'\d+(\.\d+)?',
        'SEMICOLON': r';',
        'LPAREN': r'\(',
        'RPAREN': r'\)',
        'LBRACE': r'\{',
        'RBRACE': r'\}',
        'SKIP': r'[\t\n ]+',  # Ignore whitespace
}
words = Input.split()
c=0 #column
r=0 #row
# while words:
for word in words:
    for key , value in token_specification.items():
        if re.match(value,word):
            if word=='/n':
                r=r+1
                c=-2
            else:
                word=word.replace(';',"")
                print(f"  {key} , '{word}' , {r} , {c} ")
    
    c=c+2
