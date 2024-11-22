import random

from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel


class ExampleState(BaseModel):
    success_flag: bool = False
    
class RouterFlow(Flow[ExampleState]):
    
    @start()
    def start_method(self):
        print("Starting the structured flow")
        random_boolean = random.choice([True,False])
        self.state.success_flag = random_boolean
        
    @router(start_method)
    def second_method(self):
        if self.state.success_flag:
            return "success"
        else:
            return "failure"
        
    @listen("success")
    def third_method(self):
        print("Third method (success) running")
    
    @listen("failure")
    def fourth_method(self):
        print("Fourth method (failure) running")
        
        
flow = RouterFlow()
flow.kickoff()
