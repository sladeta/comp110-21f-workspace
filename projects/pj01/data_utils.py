"""Utility functions."""

__author__ = "730236019"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
  
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
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


def seeker(row_table: list[dict[str, str]], points: str, column: str, value_1: str, value_2: str) -> dict[str, int]:
    """Returns a new dict with a count of number."""
    result: dict[str, int] = {}
    result[value_1] = 0
    result[value_2] = 0
    for row in row_table:
        if row[column] == value_1:
            result[value_1] += int(row[points])
        if row[column] == value_2:
            result[value_2] += int(row[points])
    return result


def calc(final: dict[str, int], key_1: str, key_2: str, pop_1: int, pop_2: int) -> dict[str, float]:
    """Returns the final proportion of oh visits per student."""
    result: dict[str, float] = {}
    for key in final:
        if key == key_1:    
            result[key] = final[key_1] / pop_1
        if key == key_2:
            result[key] = final[key_2] / pop_2
    return result


def rounded(final: dict[str, float], number_digits: int) -> dict[str, float]:
    """Rounds float values within a dict to a specified number of digits."""
    result: dict[str, float] = {}
    for key in final:
        item: float = final[key] 
        rounded: float = round(item, number_digits)
        result[key] = rounded
    return result


def head(column_table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Produces a column-based table with only a n # of rows for each colunn."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        values: list[str] = []
        i: int = 0 
        item: str
        if n_rows > len(column_table[column]):
            result = column_table
            return result
        while i < n_rows:
            item = column_table[column][i]
            values.append(item)
            i += 1 
        result[column] = values 
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a column-based table with only a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        value: str = column
        for value in column_table:
            items: list[str] = column_table[column]
            result[column] = items
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    list_one: list[str] = []
    list_two: list[str] = []
    for column in table_one:
        list_one = table_one[column]
        result[column] = list_one
    for column in table_two:
        if column in result:
            same: list[str] = table_two[column]
            result[column] += same
        else:    
            list_two = table_two[column]
            result[column] = list_two
    return result


def count(value: list[str]) -> dict[str, int]:
    """Returns unique values in a list with the count of the number of times it appears."""
    result: dict[str, int] = {}
    for string in value:
        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result