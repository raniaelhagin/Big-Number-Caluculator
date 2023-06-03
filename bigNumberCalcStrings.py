def add(op1, op2):
    op1_digits = [int(digit) for digit in op1]
    op2_digits = [int(digit) for digit in op2]

    # check if op2 is greater than op1 and swap if it is 
    if len(op2_digits) > len(op1_digits):
        op1_digits, op2_digits = op2_digits[::-1], op1_digits[::-1]

    carry = 0
    res = []
    for i in range(len(op1_digits)):
        if i > len(op2_digits) - 1:
            summation = op1_digits[i] + carry
        else:
            summation = op1_digits[i] + op2_digits[i] + carry
        res.append(summation % 10)
        carry = summation // 10
    
    if carry:
        res.append(carry)

    res = "".join(str(d) for d in res[::-1])
    return (res)


def subtract(op1, op2):
    op1_digits = [int(digit) for digit in op1]
    op2_digits = [int(digit) for digit in op2]

    # check if op2 is greater than op1 and set negative to true and swap
    if len(op2_digits) > len(op1_digits):
        negative = True
        op1_digits, op2_digits = op2_digits[::-1], op1_digits[::-1]

    borrow = 0
    res = []
    for i in range(len(op1_digits)):
        if i > len(op2_digits) - 1:
            sub = op1_digits[i]
        else:
            if borrow:
                op1_digits[i] -= 1
                borrow = 0

            if op1_digits[i] < op2_digits[i]:
                op1_digits[i] += 10  
                sub = op1_digits[i] - op2_digits[i]
                borrow = 1
            else:
                sub = op1_digits[i] - op2_digits[i]
        res.append(sub)

    res = "".join(str(d) for d in res[::-1])

    if negative: 
        return ("-" + res)
    return (res)


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
        operand1 = (query[1])
        operand2 = (query[2])

        operand1_1 = int(query[1])
        operand2_1 = int(query[2])

        # handle the addition operation 
        if operator == "ADD":
            # check if one of the operands is negative
            is_neg_op1 = operand1[0] == "-"
            is_neg_op2 = operand2[0] == "-"

            if is_neg_op1 and is_neg_op2:
                ans = "-" + add(operand1[1:], operand2[1:])
            elif is_neg_op1:
                ans = subtract(operand2, operand1[1:])
            elif is_neg_op2:
                ans = subtract(operand1, operand2[1:])
            else: 
                ans = add(operand1, operand2)

        # subtraction
        elif operator == "SUB":
            is_neg_op1 = operand1[0] == "-"
            is_neg_op2 = operand2[0] == "-"

            if is_neg_op1 and is_neg_op2:
                ans = subtract(operand2[1:], operand1[1:])
            elif is_neg_op1:
                ans = "-" + add(operand1[1:], operand2)
            elif is_neg_op2:
                ans = add(operand1, operand2[1:])
            else:
                ans = subtract(operand1, operand2)

        # multiplication
        elif operator == "MUL":
            ans = operand1_1 * operand2_1
        # division 
        elif operator == "DIV":
            ans = operand1_1 / operand2_1
            ans = f"{ans:.20f}"
        # power
        elif operator == "POW":
            ans = operand1_1 ** operand2_1

    with open("output.txt", 'a') as outputFile:
        outputFile.write(str(ans))
        outputFile.write('\n')
