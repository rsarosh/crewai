#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from statusreportscrew.crew import Statusreportscrew
from statusreportscrew.hr_crew import HRCrew
from statusreportscrew.tools.vacation_tool import VacationTool, VacationToolInput

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
        "user": "Diana"
    }

    try:
        # Statusreportscrew().crew().kickoff(inputs=inputs)
        HRCrew().crew().kickoff(inputs = _vacation_input)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# def main():
#     run()

# if __name__ == "__main__":
#     main()
