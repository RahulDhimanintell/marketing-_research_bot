#!/usr/bin/env python
import sys
from resbot.crew import ResbotCrew
from tqdm import tqdm
from pathlib import Path
import os
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(userinput):
    """
    Run the crew.
    """
    for companyName in tqdm(userinput.split(',')):
            
        inputs = {
            'topic': f'{companyName}'
        }
        
            
        ResbotCrew().crew().kickoff(inputs=inputs)

        # with open('report.md','r') as generatedEmail:
        #     emailReport = generatedEmail.read()
        #     generatedEmail.close()
        #     exportedReport =  open(f'C://Users//lenovo//Downloads//{userinput}_report.md','a')
        #     # exportedReport.seek(0)
        #     exportedReport.write(f'\n  ## Email for {companyName}  \n {emailReport} \n')
        #     exportedReport.close()

        with open('report1.md','r') as report:
            researchReport = report.read()
            report.close()
            exportedReport =  open(f'{path_to_download_folder}/{companyName}_report.md','a')
            # exportedReport.seek(0)
            exportedReport.write(f'\n ## Research Report for {companyName} \n {researchReport} \n')
            exportedReport.close()

        with open('newsreport.md','r') as report:
            latestNews = report.read()
            report.close()
            exportedReport =  open(f'{path_to_download_folder}/{companyName}_report.md','a')
            # exportedReport.seek(0)
            exportedReport.write(f'\n ## News report for {companyName} \n {researchReport} \n')
            exportedReport.close()
        
    return  researchReport, latestNews #, emailReport


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ResbotCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResbotCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
