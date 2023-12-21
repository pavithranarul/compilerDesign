import re
patterns =[
    ('IMPORTS',r'<stdio.h>|<conio.h>|<stdlib.h>'),
    ('KEYWORD',r'#include|if|else|for|break|int|float|String|char|double|printf|scanf|getch\(\)|while|do'),
    ('FLOAT',r'\d+\.\d+'),
    ('INT',r'\d+'),
    ('OPERATOR',r'[\+-/\*=]'),
    ('OPERATOR',r'\+?\+|-|\*|/|=|==|<|>'),
    ('ID',r'[a-zA-z_][a-zA-Z0-9_]*'),
    ('LPARAN',r'\('),
    ('RPARAN',r'\)'),
    ('SEPRATOR',r'[;:,\{\}]'),
    ("STRING",r'\"[a-zA-z0-9]*\"')

]

def lexier(source_code):
    tokens = []
    lines = source_code.split('\n')
    for line in lines:
        code = line.split(' ')
        for word in code:
            for token_type,pattern in patterns:
                match = re.match(pattern,word)
                if match:
                    tokens.append((token_type,match.group()))
                    break
            else:
                raise Exception(f"Invalid syntax : {code}")
    return tokens
file = open('text.cpp')
tokens = lexier(file.read())
for token in tokens:
    print(token)