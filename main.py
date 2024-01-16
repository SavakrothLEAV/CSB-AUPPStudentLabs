from schoolfilesystem import *

def main():
    Options = input("Enter Number: 1=URL / 2=Filename: ")

    if Options == "1":
        url = input("Enter the URL:")
        data = SchoolAssessmentSystem.fetch_web_data(url=url)
    elif Options == "2":
        filename = input("Enter the filename: ")
        data = SchoolAssessmentSystem.process_file(filename=filename)
        SchoolAssessmentSystem.transfer_data(data, filename=filename)
        SchoolAssessmentSystem.analyze_content(data=data,filename=filename)
        SchoolAssessmentSystem.generate_summary(data=data, filename=filename)
    else:
        print("Invalid")

main()
