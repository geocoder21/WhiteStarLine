# IMPORTS

import pandas

# *********************************************************************************************************************************************
# FUNCTIONS

"""
    read_data
    Pulls in csv data from url using pandas library.  Reads into a DataFrame
    and then converts to a 2D list.  Returns data as a list of lists with
    integer values.

    write_data
    Writes out specified end data to a new file.  Data strings are
    separated by line breaks.
    """
# used instead of requests module + csv reader as more efficient code


# Read in csv data

def read_data(url_name):

    lst = []  # initiate variable

    data = pandas.read_csv(url_name)    # get data
    lst = data.values.tolist()          # covert to 2D list
    return(lst)


# Write out data to a new file

def write_data(filename, end_data):
    data_out = open(filename, "w")
    for i in range(len(end_data)):
        data_out.write(end_data[i])
        data_out.write("\n")
    data_out.close()
# writes data out
