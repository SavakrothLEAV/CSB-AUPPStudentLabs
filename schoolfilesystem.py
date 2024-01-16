import csv, collections, dictionary
import pandas as pd
import openpyxl
from urllib.request import *
from urllib.error import *

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = []

    def process_file(filename):
        data = []
        if filename.endswith(".csv"):
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(dict(row))
                print("File is successfully Processed!")
            return data
        elif filename.endswith(".txt"):
            with open(filename, 'r') as txtfile:
                reader = txtfile.read()
                print("File is successfully Processed!")
            return reader
        elif filename.endswith(".xlsx"):
            data = pd.read_excel(filename)
            print("File is successfully Processed")
            return data
        else:
            print("Error: File not found.")
            return None

    def transfer_data(data, filename):

        if data is None:
            print("Error: Unable to transfer data")
            return None
        
        if filename.endswith(".csv"):
            with open(("Copied_File"+".csv"), "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
                print("File is successfully Transfered to Copied_File.csv!")
        elif filename.endswith("txt"):
            with open("Copied_File", "w") as txtfile:
                for row in data:
                    txtfile.write(str(row))
                print("File is successfully Transfered to Copied_File.txt!")
        elif filename.endswith("xlsx"):
            writer = pd.DataFrame(data)
            writer.to_excel(("Copied_File"+".xlsx"), index=False)
            print("File is successfully Transfered  to Copied_File.xlsx!")
        else:
            print("An Error Occur")
            return None

    def fetch_web_data(url):
        try:
            with urlopen(url) as response:
                data = response.read().decode('utf-8')
            return data
        except HTTPError:
            print("HTTP Error!")
        except URLError:
            print("URL Error!")
        except Exception:
            print("Error fetching web data!")

    def analyze_content(data, filename):
        
        if filename.endswith(".csv"):
            Pass = 0
            Fail = 0
            for i in range(len(data)):
                if float(data[i]["Overall"])>50:
                    Pass +=1
                else:
                    Fail +=1
            print(f"{Pass} students have Passed the Overall scores. {Fail} students have Failed the Overall scores.")
            print("Successfully analyzed the contents!")
        else:
            print("The Progammer do not know how to analyze this file.")

    def generate_summary(data, filename):
        if filename.endswith(".csv"):
            for i in range(len(data)):
                print(f"""{data[i]["Last Name"]} {data[i]["First Name"]} Withnan ID of {data[i]["ID"]} has an Overall of {data[i]["Overall"]} and
                      need improvements on {data[i]["Improvement"]}.""")
            print("Successfully Generated a summary!")
        else:
            print("The Progammer do not know how to generate a summary for this file.")
