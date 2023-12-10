from rdffwk.queue_builder.operators import Operator


class OffsetOperator(Operator):
    def __init__(self, offset: int) -> None:
        super().__init__("OFFSET")
        self.offset = offset
        
    def __repr__(self) -> str:
        return str(self.offset)
    
    def add_to_model(self, model):
        return model.set_offset(self.__repr__())