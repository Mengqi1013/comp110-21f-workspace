"""Utility functions."""

__author__ = "730485647"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-;ine
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to firee its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(data_cols: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    count_list: list[list[str]] = []
    for key in data_cols:
        count_list.append(data_cols[key])
    num_rows: int = len(count_list[0])
    if rows >= num_rows:
        return data_cols 

    for key in data_cols:
        i: int = 0
        result[key] = []
        new_list: list[str] = []
        while i < rows:
            new_list.append(data_cols[key][i])
            i += 1
        result[key] = new_list
    
    return result


print(head({"Name": ["Kaki", "Kris", "Mandy"], "Age": ["23", "36", "19"]}, 2))


def select(data_cols: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Returns a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = data_cols[item]
    
    return result


def concat(data_cols_head: dict[str, list[str]], addtional_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in data_cols_head:
        result[key] = data_cols_head[key]
    
    for key in addtional_table:
        if key in result:
            result[key] = result[key] + addtional_table[key]
        else:
            result[key] = addtional_table[key]
    
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appeared in the input list."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result