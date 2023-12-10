from ast import parse
from rdffwk.queue_builder.operators import Operator

class WhereStarOperator(Operator):
    
    def __init__(self, *args):
        super().__init__("where_star_op")
        self.type = len(args)
        self.args = args
        
    def __repr__(self, model=None):
        match self.type:
            case 1:
                if model and self.args[0].__class__ != str:
                    return self.args[0].to_model(model.depth + 1)
                
                return self.args[0].__repr__()
            
            case 2:
                parsed_arg0 = self._wrap_if_triple(self.args[0])
                
                str_args = []
                for x in self.args[1]:
                    parsed_args = self._parse_quoted_triples(x)
                    str_args.append(f"{parsed_args[0]} {parsed_args[1]}")
               
                return f"{parsed_arg0} " + "; ".join(str_args)
            
            case 3:
                parsed_arg0 = self._wrap_if_triple(self.args[0])
                
                if self.args[2].__class__ == list or self.args[2].__class__ == tuple:
                    parsed_args = self._parse_quoted_triples(self.args[2])
                    return f"{parsed_arg0} {self.args[1]} " + ", ".join([str(x) for x in parsed_args])
                
                parsed_arg2 = self._wrap_if_triple(self.args[2])
                if self.args[1].__class__ == list or self.args[1].__class__ == tuple:
                    return f"{parsed_arg0} " + "; ".join([f"{x} {parsed_arg2}" for x in self.args[1]])
                
                return f"{parsed_arg0} {self.args[1]} {parsed_arg2}"
            
            case 4:
                str_args = "{| "
                
                parsed_arg3 = [f"{x} {y}" for x,y in self.args[3]]
                str_args += "; ".join(parsed_arg3)
                
                str_args += " |}"
                
                return f"{self.args[0]} {self.args[1]} {self.args[2]} {str_args}"
          
    def add_to_model(self, model):
        model.add_triple(self.__repr__(model))
        
    def _parse_quoted_triples(self, arg):
        if arg.__class__ == str:
            return arg
        
        res = []
        for x in arg:
            res.append(self._wrap_if_triple(x))
                
        return res
    
    def _wrap_if_triple(self, arg):
        if (arg.__class__ == list or arg.__class__ == tuple) and len(arg) == 3:
            return f"<< {arg[0]} {arg[1]} {arg[2]} >>"
        
        return arg