# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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

def save_csv(csvpath, qualified_loan_data):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        qualified_loan_data: This is the filtered loan data we want to write to the new csv

    """
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Setting the header. This information comes from the oringal list of loans in the csv provided data/daily_sheet_rate.csv
        header = ["Lender","Max Loan Size","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
        # Writes the first row as the header in the new csv file of quilified loans
        csvwriter.writerow(header)

        # Now that the header is set, we write each row of qualified loan data into the new csv.

        csvwriter.writerows(qualified_loan_data)
    return csvwriter
        

