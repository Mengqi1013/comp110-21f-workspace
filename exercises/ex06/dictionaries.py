"""Practice with dictionaries."""

__author__ = "730485647"


# Define your functions below
def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    new_dict: dict[str, str] = {}
    list_of_keys: list[str] = []
    list_of_values: list[str] = []
    i: int = 0
    j: int = 1
    counter: int = 0
    for item in a:
        list_of_keys.append(item)
    for item in a:
        list_of_values.append(a[item])
    
    while i < len(list_of_values) - 1:
        while j < len(list_of_values):
            if list_of_values[i] == list_of_values[j]:
                counter += 1
            j += 1
        i += 1
    
    if counter > 0:
        raise KeyError
    else:
        for item in a:
            new_dict[a[item]] = item
        return new_dict


def favorite_color(a: dict[str, str]) -> str:
    """Returns the most frequent color appears in the dictionary. Returns the item first occurs in the list if there's a tie."""
    backup_dict: dict[str, int] = {}
    list_of_colors: list[str] = []
    max: int = 1
    new_list: list[str] = []
    
    for item in a:
        list_of_colors.append(a[item])
    
    if len(list_of_colors) == 1:
        return list_of_colors[0]

    for item in list_of_colors:
        if item in backup_dict:
            backup_dict[item] += 1
        else:
            backup_dict[item] = 1
    
    for item in backup_dict:
        if max < backup_dict[item]:
            max = backup_dict[item]
            new_list.append(item)
    
    return new_list[len(new_list) - 1]
    

def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a string appears in a list."""
    new_dict: dict[str, int] = {}
    for item in a:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    return new_dict