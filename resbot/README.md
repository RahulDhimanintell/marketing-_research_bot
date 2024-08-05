# Resbot Crew

## Installation

Ensure you have Python 3.11 installed on your system. This project uses [Poetry](https://python-poetry.org/).

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/resbot/config/agents.yaml` to define your agents
- Modify `src/resbot/config/tasks.yaml` to define your tasks
- Modify `src/resbot/crew.py` to add your own logic, tools and specific args
- Modify `src/resbot/main.py` to add custom inputs for your agents and tasks

## Running the Project

Activate the poetry shell
```bash
poetry shell
```


To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run resbot
```

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Resbot Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Resbot Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)


