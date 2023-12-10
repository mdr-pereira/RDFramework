from rdffwk.queue_builder.operators import Operator

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
                if self._is_iterable(self.args[2]):
                    return f"{self.args[0]} {self.args[1]} {','.join([str(x) for x in self.args[2]])}"
                
                if self._is_iterable(self.args[1]):
                    return f"{self.args[0]} {'; '.join([f'{x} {self.args[2]}' for x in self.args[1]])}"
                
                return f"{self.args[0]} {self.args[1]} {self.args[2]}"
                
    def add_to_model(self, model):
        model.add_triple(self.__repr__(model))
    
    def _is_iterable(self, arg):
        return arg.__class__ == list or arg.__class__ == tuple
        