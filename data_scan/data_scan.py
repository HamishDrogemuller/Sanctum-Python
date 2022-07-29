"""
Scans a csv file redirected into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
import argparse
import math
import csv

#Exercise 0 - 
# 1. Look at the python "argparse", 
#    Describe how to set up arguments, 
#    Explain how it is set up - see code under "if __name__ == "__main__:"
# 2. Write out a description of how scan works, 
def scan(has_header=False):
    result = [] # list of dictionaries
    values = [] # list of values
    do_header = has_header # boolean
    header_names = {} # dictionary
    try:
        for aline in sys.stdin: # read in the lines of standard input
                this_line = aline.strip().split(',') # format line into list of values
                if do_header: # declare if
                    header_names = this_line # set header names
                    do_header = False # set do_header to False
                else: # else of if
                    a_dict = {} # create a dictionary
                    for i in range(0,len(this_line)): # for each value in the line
                        if has_header : # if a header is present
                            a_dict[header_names[i]]= this_line[i] # set the value of the dictionary to the value of the line
                        else: # else of if
                            a_dict[i]= this_line[i] # set the value of the dictionary to the value of the line

                    result += [a_dict] # add the dictionary to the list of dictionaries
                    values += [this_line] # add the values to the list of values
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return result,values

    return result,values

# Exercise one
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """



#Exercise Two
def multiple_cols(column_names,a_list_of_dictioinary):
    """
    Return a new list of "rows" (dictionary)
    That multiples the values of the named columns
    
    """
    pass

#Exercise Three
# - fix display_table so that the columns all line up
def display_table(a_list_of_dictionary):
    lines = ""
    # Get a header line
    a_dictionary = a_list_of_dictionary[0]
    header_line = ""
    for key in a_dictionary:
        header_line += f'{key}\t'
    header_line = header_line.strip()

    # Make up the table
    lines += header_line 

    for a_dictionary in a_list_of_dictionary:
        a_line = ''
        for key,value in a_dictionary.items():
            a_line += f'{value}\t'
        a_line = a_line.strip()
        lines += f'\n{a_line}'
    print(lines)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
   parser.add_argument('--header',action='store_true',help='The first row is a header row.')
   args = vars(parser.parse_args())
   print(f'The args are {args}')
   #args = sys.argv
   #print(f'The args are {args}')
   dict_lst,values_lst = scan(args['header'])
   display_table(dict_lst)
