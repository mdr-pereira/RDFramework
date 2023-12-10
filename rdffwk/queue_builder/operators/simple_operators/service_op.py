from rdffwk.queue_builder.operators import Operator

class ServiceOperator(Operator):
    
    def __init__(self, endpoint, query):
        super().__init__("service_op")
        self.endpoint = endpoint
        self.block = query
        
    def __repr__(self, model=None) -> str:
        text = f"{self.endpoint} "
        
        if model and self.block.__class__ != str:
            text += self.block.to_model(model.depth + 1).__repr__()
        else:
            text += self.block.__repr__()
        
        return text
    
    def add_to_model(self, model):
        return model.add_service(self.__repr__())