"""Function writing practice for quizzes."""


def dict_transform(new_dict: dict[int, list[int]]) -> dict[int, list[int]]:
    """Question 13."""
    result: dict[int, list[int]] = {}
    for key in new_dict:
        new_list: list = []
        for item in new_dict[key]:
            item = item * key
            new_list.append(item)
            result[key] = new_list
            
    return result


print(dict_transform({2: [1, 2], 5: [3, 4]}))


def average_grades(new_dict: dict[str, list[int]]) -> dict[str, float]:
    """Question 14."""
    