def sum_list(the_list):
    somma=0
    for number in the_list:
        somma+= number
    return somma
        
the_list = [4, 34, 7, 2, 12]

print(sum_list(the_list))