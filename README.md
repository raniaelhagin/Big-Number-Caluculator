# Big Number Calculator

- You have to implement Arithmetic Operations for a very large number (even larger than long long int).

- Basic operations which are needed to be implemented are: Addition, Subtraction, Multiplication and Division.
- Other operations include: square root, Absolute value and power.

- You can use any Programming language.

- You are only allowed to use string and other libraries which inherently don't implement big number library.

- Your input will be a text file ​​(named input.txt) containing the different queries corresponding to each arithmetic operation.

- Query Format: Each line of input file corresponds to a query which is in the format:

    - `<Operator><SPACE> <Operand 1><SPACE> <Operand 2 if required>`
    - Operator can be one of the strings: ADD, SUB, MUL, DIV, SQRT, ABS, POW 
    - Operand will be a String representing a floating point decimal number.

- Your output will be a text file (named output.txt)

- For each query, you have to print a single lined output in the output file which is also a string corresponding to a floating point decimal number.

- You need to handle the cases where the operand or results are negative values.

- For floating point results the precision should be correct up to 20 digits after decimal point.


## Solution: 
- Because python can handle very large numbers directly as it supports "bignum" data type which can work with big numbers which exceeds the boundaries of 32-bit (the inputs are integers only, I used int function to cast-type it)

- We also could use string manipulation and arithmetic operation for every digit to solve this problem 
(I just handled addition and subtraction in this case and the other operation works as before)

### Test cases: 

ADD -5289750928502650285 -25082658640528694865

ADD 5289750928502650285 -25082658640528694865

ADD -5289750928502650285 25082658640528694865

ADD 5289750928502650285 25082658640528694865

SUB -529081526583468459207239457029 -257286823465823658626589146928659

SUB 529081526583468459207239457029 -257286823465823658626589146928659

SUB -529081526583468459207239457029 257286823465823658626589146928659

SUB 529081526583468459207239457029 257286823465823658626589146928659

MUL 2437094578203945348957344889457 234587594

DIV 42750975043957349759 342097520937592437029570954386

POW 49237850942375094237594327 3

ABS -495723097523549750923487059

SQRT 54298709348759327059752345

---

### sample of the output:
---

**With string manipulation** (there is a bug in the subtract function (handled in v1.1))

-30372409569031345150

-19792907712026044580

19792907712026044580

30372409569031345150

256757741939240190167381907471630

257815904992407127085796386385688

-257815904992407127085796386385688

-256757741939240190167381907471630

571712153451308380719393946245913596458

0.00000000012496721674

119370570035291945842202176197289847968040560359834096790392529909347217443783

495723097523549750923487059

2.7149354674379663e+25

----

**Using numbers directly**

-30372409569031345150

-19792907712026044580

19792907712026044580

30372409569031345150

256757741939240190167381907471630

257815904992407127085796386385688

-257815904992407127085796386385688

-256757741939240190167381907471630

571712153451308380719393946245913596458

0.00000000012496721674

119370570035291945842202176197289847968040560359834096790392529909347217443783

495723097523549750923487059

2.7149354674379663e+25
