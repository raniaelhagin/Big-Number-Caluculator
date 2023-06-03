# clear the output file before writing in
open('output.txt', 'w').close()

# read the input file that contains the quueries 
with open("input.txt") as inputFile:
    queries = inputFile.readlines()

for query in queries:
    query = query.split()    # split the query 
    operator = query[0]

    # check the operator 
    if operator == "SQRT" or operator == "ABS":
        operand1 = int(query[1])
        
        # handle sqrt 
        if operator == "SQRT":
            ans = operand1 * 0.5 
        
        # hadle absolute 
        else:
            if operand1 < 0:
                ans = -1 * operand1
            else:
                ans = operand1
    else:
        operand1 = int(query[1])
        operand2 = int(query[2])

        # handle the addition operation 
        if operator == "ADD":
            ans = operand1 + operand2
        # subtraction
        elif operator == "SUB":
            ans = operand1 - operand2
        # multiplication
        elif operator == "MUL":
            ans = operand1 * operand2
        # division 
        elif operator == "DIV":
            ans = operand1 / operand2
            ans = f"{ans:.20f}"
        # power
        elif operator == "POW":
            ans = operand1 ** operand2

    with open("output.txt", 'a') as outputFile:
        outputFile.write(str(ans))
        outputFile.write('\n')
