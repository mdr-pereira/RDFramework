from .operator import Operator

class ServiceOperator(Operator):
    
    def __init__(self, endpoint, query):
        self.endpoint = endpoint
        self.query = query
        
    def __repr__(self) -> str:
        return f"{self.endpoint} {{ {self.query} }}"
    
    def add_to_model(self, model):
        return model.add_service(self.__repr__())