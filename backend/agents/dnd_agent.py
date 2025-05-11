# Example agent logic for D&D

class DnDAgent:
    def __init__(self, name):
        self.name = name

    def act(self, input_data):
        # Implement agent behavior here
        return f"Agent {self.name} received: {input_data}"
