import re
import math

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
    #currently hard-coding regex for strings like LAX94LA336. Future developments could detect such a pattern
    #and dynamically produce a regex
    correct_column = get_entire_column(data, col_index)
    correct_column.sort()
    upper = len(correct_column)-1
    lower = 0
    index = math.floor((upper+lower)/2)
    #use of floor is arbitrary (could also be ceil) but consistent throughout the function
    guess = correct_column[index]
    while string_youre_after != guess and lower < upper:
      if string_youre_after < guess:
          upper = index-1
      else:
          lower = index+1
      index = math.floor((upper+lower)/2)
      guess = correct_column[index]
    if string_youre_after == guess:
        return(index)
    else:
        print('The string ' + string_youre_after + ' is not in in this dataset.')
        return(-1)

def subset_by_country(data, country):
    in_the_right_country = []
    for row in data:
        if row[5] == country:
            in_the_right_country.append(row)
    return(in_the_right_country)

def accident_subset(data, string='Accident'):
    is_accident = []
    for row in data:
        if row[1] == string:
            is_accident.append(row)
    return(is_accident)

def count_accidents_by_state(data):
    us_only = subset_by_country(data, 'United States')
    accidents_in_us_only = accident_subset(us_only, 'Accident')
    locations = [loc[4] for loc in accidents_in_us_only]
    states = [state[-2:] for state in locations]
    dict_of_state_counts = {}
    for state in states:
        if state in dict_of_state_counts:
            dict_of_state_counts[state] += 1
        else:
            dict_of_state_counts[state] = 1
    return(dict_of_state_counts)

state_accident_counts = count_accidents_by_state(aviation_data)

def get_max_value(dictionary):
    """
    Returns the key for the dictionary item with the greatest value
    """
    max = 0
    highest = ''
    for key, value in dictionary.items():
        if value > max:
            max = value
            highest = key
    return(highest)

get_max_value(state_accident_counts)

header[23:25]

aviation_data[85][3]

def count_by_unique_colname_value(data, colname):
    """
    Takes an item from the header list and returns
    a ditionary of each item in that column and
    the counts of times it occurs.
    """
    counts = {}
    index = header.index(colname)
    for row in data:
        col_val = row[index]
        if col_val in counts:
            counts[col_val] += 1
        else:
            counts[col_val] = 1
    return(counts)
