a_list_of_dictionary,values = [{'a':1},{'a':4},{'a':7,}]
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """
    sum = 0
    for i in a_list_of_dictionary:
        sum += i[column_name] if type(i[column_name]) == int else int(i[column_name])
        
    
    return sum

print(sum)