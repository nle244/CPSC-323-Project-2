input1 = '(a+a)*a$'
input2 = 'a*(a/a)$'
input3 = 'a(a+a)$'
input4 = '(a+a)e$'

current_input = input4
state_stack = ['E','$']
input_stack = list(current_input)
output_stack = []
parse_check = True

def parse(state_stack,input_stack,output_stack,parse_check):
    state_char = state_stack[0]
    input_char = input_stack[0]

    match state_char:
        case 'E':
            output_stack.insert(0,state_char)
            state_stack = state_stack[1:]
            match input_char:
                case 'a':
                    #E -> TQ
                    state_stack.insert(0,'Q')
                    state_stack.insert(0,'T')
                case '(':
                    #E -> TQ
                    state_stack.insert(0,'Q')
                    state_stack.insert(0,'T')
                case _:
                    parse_check = False
        case 'Q':
            output_stack.insert(0,state_char)
            match input_char:
                case '+':
                    #Q -> +TQ
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'Q')
                    state_stack.insert(0,'T')
                    state_stack.insert(0,'+')
                case '-':
                    #Q -> -TQ
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'Q')
                    state_stack.insert(0,'T')
                    state_stack.insert(0,'-')
                case ')':
                    #Q -> epsilon
                    state_stack = state_stack[1:]
                case '$':
                    #Q -> epsilon
                    state_stack = state_stack[1:]
                case _:
                    parse_check = False
        case 'T':
            output_stack.insert(0,state_char)
            match input_char:
                case 'a':
                    #T -> FR
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'R')
                    state_stack.insert(0,'F')
                case '(':
                    #T -> FR
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'R')
                    state_stack.insert(0,'F')
                case _:
                    parse_check = False
        case 'R':
            output_stack.insert(0,state_char)
            match input_char:
                case '+':
                    #R -> epsilon
                    state_stack = state_stack[1:]
                case '-':
                    #R -> epsilon
                    state_stack = state_stack[1:]
                case '*':
                    #R -> *FR
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'R')
                    state_stack.insert(0,'F')
                    state_stack.insert(0,'*')
                case '/':
                    #R ->/FR
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'R')
                    state_stack.insert(0,'F')
                    state_stack.insert(0,'/')
                case ')':
                    #R -> epsilon
                    state_stack = state_stack[1:]
                case '$':
                    #R -> epsilon
                    state_stack = state_stack[1:]
                case _:
                    parse_check = False
        case 'F':
            output_stack.insert(0,state_char)
            match input_char:
                case 'a':
                    #F -> a
                    state_stack = state_stack[1:]
                    state_stack.insert(0,'a')
                case '(':
                    #F -> (E)
                    state_stack = state_stack[1:]
                    state_stack.insert(0,')')
                    state_stack.insert(0,'E')
                    state_stack.insert(0,'(')
                case _:
                    parse_check = False
        case _:
            parse_check = False

    if state_stack[0] == '$' and input_stack[0] == '$':
        output_stack.insert(0,'$')
        input_stack = []
    else:
        if state_stack[0] == input_stack[0]:
            state_stack = state_stack[1:]
            input_stack = input_stack[1:]
            output_stack = []

    return state_stack, input_stack, output_stack, parse_check


print(f'Input: {current_input}')
while len(input_stack) > 0 and parse_check:
    state_stack, input_stack, output_stack, parse_check = parse(state_stack,input_stack,output_stack,parse_check)
# print(f'Stack: {output_stack}')
# print(f'states: {state_stack}')
if parse_check:
    print(f'Stack: {output_stack}')
    print('Output: String is accepted / valid.')
else:
    state_stack.reverse()
    print(f'Stack: {state_stack}')
    print('Output: String is not accepted / invalid.')

