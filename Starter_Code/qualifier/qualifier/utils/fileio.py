# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary

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

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    save = questionary.confirm(
        "Would you like to save your list of qualified loans?"
    ).ask()
    # Indicate headers
    header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

    if save:
        name = questionary.text("Name your save file:").ask()
        with open(f'data/{name}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(qualifying_loans)
            print("Saving file...")