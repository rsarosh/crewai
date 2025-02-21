from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from statusreportscrew.tools.vacation_tool import VacationTool, ask_human
 

@CrewBase
class HRCrew:
    """HRCrew crew"""
    agents_config = "config/hr_agents.yaml"
    tasks_config = "config/hr_tasks.yaml"

    @agent
    def hr_manager(self) -> Agent:
        return Agent(config=self.agents_config["hr_manager"], verbose=True)

    @task
    def hr_task(self) -> Task:
        return Task(
            config=self.tasks_config["hr_task"],
            tools=[VacationTool(), ask_human],
            verbose=True,
            expected_output=" A string with the number of days of vacation left for the employee.",
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HRcrew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
