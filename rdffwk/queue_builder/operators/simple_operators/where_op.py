from rdffwk.queue_builder.operators.operator import Operator


class WhereOperator(Operator):
    
    def __init__(self, *args):
        super().__init__("where_op")
        self.type = len(args)
        self.args = args
        
    def __repr__(self, model=None):
        match self.type:
            case 1:
                if model and self.args[0].__class__ != str:
                    return self.args[0].to_model(model.depth + 1)
                
                return self.args[0].__repr__()
            case 2:
                str_args = [f"{x} {y}" for x, y in self.args[1]]
                
                return f"{self.args[0]} " + "; ".join(str_args)
            case 3:
                if self.args[2].__class__ == list:
                    return f"{self.args[0]} {self.args[1]} " + ", ".join([str(x) for x in self.args[2]])
                
                return f"{self.args[0]} {self.args[1]} {self.args[2]}"
                
    def add_to_model(self, model):
        model.add_triple(self.__repr__(model))
        
        