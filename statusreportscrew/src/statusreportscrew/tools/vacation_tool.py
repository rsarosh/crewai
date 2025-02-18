from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class VacationToolInput(BaseModel):
    """Input schema for VacationTool."""
    argument: str = Field(..., description="Name of the employee.")


class VacationTool(BaseTool):
    name: str = "Vacation Tool"
    description: str = (
        "This tool is used to check number of days vacation an employee have."
    )
    args_schema: Type[BaseModel] = VacationToolInput

    def _run(self, argument: str) -> str:
        employees_vacation = [("Alice", 10), ("Bob", 15), ("Charlie", 8), ("Diana", 12)]
        for employee, days in employees_vacation:
            if employee == argument:
                return f"{argument} has {days} days of vacation left."
        return f"{argument} is not in the list of employees."
