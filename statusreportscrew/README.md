# Statusreportscrew Crew

Welcome to the Statusreportscrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/statusreportscrew/config/agents.yaml` to define your agents
- Modify `src/statusreportscrew/config/tasks.yaml` to define your tasks
- Modify `src/statusreportscrew/crew.py` to add your own logic, tools and specific args
- Modify `src/statusreportscrew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
cd statusreportscrew
```
make sure venv is active
```
c:\code\crewai\statusreportscrew> .\venv\Scripts\activate
$ crewai run
```

This command initializes the statusReportsCrew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The statusReportsCrew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Statusreportscrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


# Running the flow

```
python c:\Code\CrewAI\statusreportscrew\src\statusreportscrew\main.py
```
or

```
goto PS C:\Code\crewai\statusreportscrew
.venv\Scripts\activate
crewai run
```
## Flow

get_stock_data
    | 
get_stock_news
    | 
get_stock_report