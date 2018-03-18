import re

with open('AviationData.txt', 'r') as file:
    lines = file.readlines()

file = [row.split(' | ') for row in lines]
header = file[0]
aviation_data = file[1:]

def find_the_right_column(row_of_the_dataset, pattern):
    """
    Use a regex pattern to find the index within common lists
    """
    for i in range(len(row_of_the_dataset)):
        if re.match(pattern=pattern, string=row_of_the_dataset[i]) is not None:
            return(i)

def get_entire_column(list_of_lists, column_index):
    """Get column from a list of lists and an index"""
    return [col[column_index] for col in list_of_lists]

weird_codes = get_entire_column(aviation_data, 2)

def get_specific_airport_code(data, string_youre_after):
    """
    Find the row(s) of data where a specific string occurs
    using an exponential time algorithm.
    """
    #Note: Below is a geometric algorithm to find the specified string.
    #   This approach is ideal for short lists. However, in this case
    #   it does not maximize efficieny, since the user risks
    #   iterating through the entire dataset before finding the string.
    str_found = []
    for row in data:
        if string_youre_after in row:
            str_found.append(row)
    return(str_found)

#linear time algorithm to search for string 'LAX94LA336'
def linear_find_str(data, string_youre_after):
    """
    Find the row(s) of data where a specific string occurs
    using a linear time algorithm.

    Unlike the exponential algorithm, this linear one saves
    time by only searching one column (column at index 2),
    thereby using only one for loop instead of 2 (or the in
    function).

    To use this function, the user must only search this one
    column, limiting the scope of the function.
    """
    str_found = []
    for row in data:
        if row[2] == string_youre_after:
            str_found.append(row)
    return(str_found)

def binary_search_str(data, string_youre_after):
    """
    Search for the string using a binary approach.

    Algorithm jumps between midpoints of the upper
    and lower bounds of the dataset, minimizing
    the number of iterations necessary.

    The speed of this function is determined by
    O(log(n)).

    Note: Unfortunately, this function returns
    the index of a sorted list of strings, so
    it cannot return the entire row, just the
    position of the string in a sorted list.
    """
    col_index = find_the_right_column(data[0], pattern='[A-Z]{3}[0-9]{2}[A-Z]{2}[0-9]{3}.*')
    #sort that column (now list named correct_column)
    #set upper bound
    #set lower bound
    #set index at midpoint of upper & lower bounds
    #test row at 👆 index for presence of string_youre_after
    #set guess to string in row at index
    #while string is not in that row and lower bound hansn't met or crossed upper bound
    #   if string_youre_after < guess:
    #       set upper limit to index-1
    #   else:
    #       set lower limit to index+1
    #set index of subsequent guess
    #set guess equal to string at 👆 index
    #if string_youre_after == guess:
    #   return index
    #else:
    #   print('The string ' + string_youre_after + ' is not in in this dataset.')
    #   return -1
