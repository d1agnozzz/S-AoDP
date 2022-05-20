

def get_dividers(number):
    result = list()
    for sys in range(2, 10**6):
        first = convert_to_pseudosystem(number, sys)
        for divider in range(2, number):
            second = convert_to_pseudosystem(divider, sys)
            if first % second == 0:
                result.append((sys, divider))

    if len(result)>0:
        return result
    return -1

def convert_to_system(input_number, sys):
    number = input_number
    result = 0

    tens = 1
    while number > 0:
        result += number%sys * tens
        tens *= 10
        number //= sys  

    return result 

print((get_dividers(19)))


