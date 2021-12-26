# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import fire


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


#Trying to move this function here - fail - commenting out for now
'''
def save_csv(qualifying_loans_list):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!

    #creates a header for the csv file for the information related to the qualifying loan(s)
    header = ["Lender", "Max Loan", "Max LTV", "Max DTI", "Min Credit", "Interest Rate"]

    #sets a path for where to save the csv output file
    output_path = Path("./data/qualifying_loans.csv")

    #writes each qualifying loan to a row in the output csv file
    with open(output_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        for row in qualifying_loans_list:
            csvwriter.writerow([row])

'''            