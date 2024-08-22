from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from resbot.tools.custom_tool import MyCustomTool, SearchTools

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ResbotCrew():

	"""Resbot crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	
	@agent
	def news_reporter(self) -> Agent:
		return Agent(
			config=self.agents_config['news_reporter'],
			tools=[SearchTools.search_internet, SearchTools.search_news], # Example of custom tool, loaded on the beginning of file
			verbose=True, #logs
			# max_iter = 2
		)

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SearchTools.search_internet], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			# max_iter = 2,
			allow_delegation = True
		)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True,
	# 		# max_iter = 2,
	# 		allow_delegation = True
	# 	)
	
	
	
	@task
	def news_reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['news_reporting_task'],
			agent=self.news_reporter(),
			output_file='newsreport.md'
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher(),
			output_file='report1.md'
		)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		agent=self.reporting_analyst(),
	# 		output_file='report.md'
	# 	)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the Resbot crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)