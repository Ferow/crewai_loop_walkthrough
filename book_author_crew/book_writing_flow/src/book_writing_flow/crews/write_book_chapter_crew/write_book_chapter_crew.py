from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from book_writing_flow.types import Chapter
#from langchain_openai import ChatOpenAI

@CrewBase
class WriteBookChapterCrew():
	"""Write Book Chapter Crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	#llm = ChatOpenAI(
	#	model="ollama/llama3.1:latest",
	#	base_url="http://localhost:11434",
#		api_key="NA"
#	)
 
	@agent
	def researcher(self) -> Agent:
		search_tool = SerperDevTool()
		return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool],
            verbose=True,
        )

	@agent
	def writer(self) -> Agent:
		return Agent(
            config=self.agents_config["writer"],
            verbose=True,
        )

	@task
	def research_chapter(self) -> Task:
		return Task(
            config=self.tasks_config["research_chapter"],
        )

	@task
	def write_chapter(self) -> Task:
		return Task(config=self.tasks_config["write_chapter"], output_pydantic=Chapter)

	@crew
	def crew(self) -> Crew:
		"""Creates the Write Book Chapter Crew"""
		return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
