class TestCase:
    def __init__(self, name, priority, status):
        self.name = name
        self.priority = priority
        self.status = status
    

    def __repr__(self):
        return f"Test Name: {self.name}\n Test Priority: {self.priority}\n Test Status: {self.status}"


    def run(self):
        raise NotImplementedError
    
