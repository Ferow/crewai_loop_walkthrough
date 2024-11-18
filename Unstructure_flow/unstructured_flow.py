from crewai.flow.flow import Flow, listen, start

class UnstructuredExampleFlow(Flow):
    @start()
    def first_method(self):
        print("Starting flow")
        print(f"State before first method:\n{self.state}")
        self.state["message"] = "Hello from unstructured flow"
        self.state["counter"] = 0
        
    @listen(first_method)   
    def second_method(self):
        print("Second method")
        print(f"State before second method:\n{self.state}")
        self.state["message"] += " - updated"
        self.state["counter"] += 1
        
    @listen(second_method)
    def third_method(self):
        print(f"State before third method:\n {self.state}")
        self.state["message"] += " - updated again"
        self.state["counter"] += 1
        print(f"State after third method: {self.state}")

flow = UnstructuredExampleFlow()
flow.kickoff()

print(f"Final state:\n{flow.state}")