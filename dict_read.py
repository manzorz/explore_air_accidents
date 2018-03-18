with open('AviationData.txt', 'r') as file:
    lines = file.readlines()

file = [row.split(' | ') for row in lines]
header = file[0]
aviation_data = file[1:]

aviation_dict_list = []
for l in aviation_data:
    d = dict(zip(header, l))
    aviation_dict_list.append(d)

def string_search_list_of_dicts(list_of_dicts, string):
    """
    Iterates through a list of dictionaries and
    through those dictionaries themselves to
    find a specific string in the values

    Exponential time function, two for loops
    """
    for d in list_of_dicts:
        for key,value in d.items():
            if value == string:
                return(d)

lax_dict = string_search_list_of_dicts(aviation_dict_list, 'LAX94LA336')
lax_dict
