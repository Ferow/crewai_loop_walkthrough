from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class StructuredExampleFlow(Flow[ExampleState]):
    @start()
    def first_method(self):
        print("Starting Flow")
        print(f"Start before first_method\n {self.state}\n")
        self.state.message = "hello from structured flow"
        self.state.counter = 1
        
    @listen(first_method)
    def second_method(self):
        print(f"State before second method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated "

    @listen(second_method)
    def third_method(self):
        print(f"\nState before third method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated again"
        print(f"\nState after third method:\n{self.state}\n")  
        
flow = StructuredExampleFlow()
flow.kickoff()

print(f"final state:\n{flow.state}")