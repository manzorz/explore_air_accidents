import timeit

with open('AviationData.txt', 'r') as file:
    lines = file.readlines()

file = [row.split(' | ') for row in lines]
header = file[0]
aviation_data = file[1:]

def get_specific_airport_code(data, string_youre_after):
    """
    Find the row(s) of data where a specific string occurs
    using an exponential time algorithm.
    """
    #Note: Below is a geometric algorithm to find the specified string.
    #   This approach is ideal for short lists. However, in this case
    #   it does not maximize efficieny, since the user risks
    #   iterating through the entire dataset before finding the code.
    str_found = []
    for row in data:
        if string_youre_after in row:
            str_found.append(row)
    return(str_found)

lax_code = get_specific_airport_code(data=aviation_data, string_youre_after='LAX94LA336')

#linear time algorithm to search for string 'LAX94LA336'
def linear_find_str(data, string_youre_after):
    """
    Find the row(s) of data where a specific string occurs
    using a linear time algorithm.
    """
