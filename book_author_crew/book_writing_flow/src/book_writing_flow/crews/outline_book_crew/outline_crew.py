from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
#from langchain_openai import ChatOpenAI
from book_writing_flow.types import BookOutline
@CrewBase
class OutlineCrew():
	"""Book Outline Crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
    
#	llm = ChatOpenAI(
#		model="ollama/llama3.1:latest",
#		base_url="http://localhost:11434",
#		api_key="NA"
#	 )
 
	@agent
	def researcher(self) -> Agent:
		search_tool = SerperDevTool()
		return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool],
            verbose=True,
        )

	@agent
	def outliner(self) -> Agent:
		return Agent(
            config=self.agents_config["outliner"],
            verbose=True,
        )

	@task
	def research_topic(self) -> Task:
		return Task(
            config=self.tasks_config["research_topic"],
        )

	@task
	def generate_outline(self) -> Task:
		return Task(
            config=self.tasks_config["generate_outline"], output_pydantic=BookOutline
        )

	@crew
	def crew(self) -> Crew:
		"""Creates the Book Outline Crew"""
		return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )