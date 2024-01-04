import re

def nfa(i, state):
    ns = state + 1
    return f"{state} --> {i} --> {ns}"

def occurance(state):
    ns = state + 1
    return f"{ns} --> e --> {state}"

def paren(i):
    new_variable = re.sub(r"\(|\)", "", i)
    return new_variable  # Output: "a|b"


def check(re_ip):
    regex = re_ip.split()
    state = 0
    
    for i in regex:
        if "*" not in i and "|" not in i:
            print(nfa(i, state))
            state += 1  
        elif "*" in i:
            startingnode=state
            char = i[:-1]  # Removing the "*" from the character
            ns = state + 1
            print(f"{state} --> e --> {ns}")
            state += 1
            print(nfa(char, state))
            print(occurance(state))
            state += 1 
            ns = state + 1
            print(f"{state} --> e --> {ns}")
            print(f"{startingnode} --> e --> {ns}")
            state+=1
        elif "|" in i:
            char = i.replace("|"," ").replace("("," ").replace(")", " ")
            var = char.split()
            startingnode = state
            for j in var:
                
                ns=state + 1
                print(f"{startingnode} --> e --> {ns}")
                state += 1
                print(nfa(j,state))
                state += 1
            ns = state + 1
            print(f"{state} --> e --> {ns}")
            state -= 2
            print(f"{state} --> e --> {ns}")
        elif "(" and ")" in i:
            id = paren(i)
            print(id)
            print(check(id))
            

            
            

re_ip = input("Enter regular expression: ")
check(re_ip)