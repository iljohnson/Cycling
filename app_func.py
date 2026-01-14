
import getpass
import pandas as pd


Username = getpass.getuser()


def convert_strings_to_floats(input_array):
    output_array = []
    for element in input_array:
        converted_float = float(element)
        output_array.append(converted_float)
    return output_array


def save_me(a):
    global file_name
    file_name = "C:\\Users\\" + Username + "\\Downloads\\RaceSettings.xlsx"
    with pd.ExcelWriter(file_name) as writer:
        a.to_excel(writer, sheet_name='RaceData', index=False)
    return
