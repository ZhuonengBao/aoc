def sum_multiplications(s: list) -> int:
    mulc = list('mul(')
    a_int = 0
    b_int = 0
    a = []
    b = []
    total = 0

    step1 = 0
    step2 = 0
    step3 = 0
    step4 = 0

    for i in range(4, len(s)):
        # Find the start 'mul('
        if not step1:
            if mulc == s[i - 4:i]:
                step1 = 1
                step2 = 1

        # Find the first integer a.
        if step2:
            if s[i] in list('0123456789'):
                a.append(s[i])
            elif s[i] == ',':
                resulting_string = ''.join(a)
                final_integer = int(resulting_string)
                a_int = final_integer
    
                a = []
                step2 = 0
                step3 = 1
                continue
            else:
                a = []
                step1 = step2 = step3 = 0

        # Find the second integer b.
        if step3:
            if s[i] in list('0123456789'):
                b.append(s[i])
            elif s[i] == ')':
                resulting_string = ''.join(b)
                final_integer = int(resulting_string)
                b_int = final_integer

                b = []
                step3 = 0
                step4 = 1
                continue
            else:
                step1 = step3 = step4 = 0
                b = []

        # Multiply integers a and b. 
        if step4:
            total += a_int * b_int
            a_int = b_int = step4 = step1 = 0

    return total


sum_total = 0
with open("input.txt", "r") as file:
    for line in file:
        input_lst = list(line)
        sum_total += sum_multiplications(input_lst)
        

print(sum_total)
