#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from statusreportscrew.crew import Statusreportscrew
from statusreportscrew.hr_crew import HRCrew
from statusreportscrew.tools.vacation_tool import VacationTool, VacationToolInput
from crewai.flow.flow import Flow, listen, start
# from statusreportscrew.my_flow import ExampleFlow
from statusreportscrew.stock_flow import StockFlow
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {"current_month": "February", "current_year": str(datetime.now().year)}
    _vacation_input = {
        "employee_name": ""
    }

    try:
       # Statusreportscrew().crew().kickoff(inputs=inputs)
       # HRCrew().crew().kickoff(inputs = _vacation_input)
        stock_flow = StockFlow()
        stock_flow.kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

 