class ClientProgram:
    def __init__(self, client, program, id=None):
        self.client = client
        self.program = program
        self.id = id
    
    def __str__(self):
        return f"Program {self.program.title} allocated to {self.client.first_name}."
        