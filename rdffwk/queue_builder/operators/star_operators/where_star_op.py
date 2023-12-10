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
                return self._case_2(self.args[0], self.args[1])
            
            case 3:
                return self._case_3(self.args[0], self.args[1], self.args[2])
            
            case 4:
                return self._case_4(self.args[0], self.args[1], self.args[2], self.args[3])
          
    def add_to_model(self, model):
        model.add_triple(self.__repr__(model))
        
    def _case_2(self, arg0, arg1):
        is_star = self._is_star_operation(arg0)
                
        arg0 = self._split_if_triple(arg0, is_star)
        
        arg1_list = []
        for x in arg1:
            parsed_args = self._parse_quoted_triples(x)
            arg1_list.append(f"{parsed_args[0]} {parsed_args[1]}")
        
        res_str = f"{arg0} "
        res_str += " {| " if is_star else ""
        res_str += "; ".join(arg1_list)
        res_str += " |}" if is_star else ""
        
        return res_str
    
    def _case_3(self, arg0, arg1, arg2):
        arg0 = self._wrap_if_triple(arg0)       
        if self._is_iterable(arg2):
            return f"{arg0} {arg1} {', '.join([str(x) for x in self._parse_quoted_triples(arg2)])}"
        
        arg2 = self._wrap_if_triple(arg2)
        if self._is_iterable(arg1):
            return f"{arg0} {'; '.join([f'{x} {arg2}' for x in arg1])}"
        
        return f"{arg0} {arg1} {arg2}"
    
    def _case_4(self, arg0, arg1, arg2, arg3):
        return f"{arg0} {arg1} {arg2} {{| {'; '.join([f'{x} {y}' for x,y in arg3])} |}}"
        
    def _is_star_operation(self, arg):
        return self._is_iterable(arg) and len(arg) == 3
    
    def _is_iterable(self, arg):
        return arg.__class__ == list or arg.__class__ == tuple
    
    def _split_if_triple(self, arg, star):
        return f"{arg[0]} {arg[1]} {arg[2]}" if star else arg
    
    def _wrap_if_triple(self, arg):
        return f"<< {arg[0]} {arg[1]} {arg[2]} >>" if self._is_star_operation(arg) else arg
        
    def _parse_quoted_triples(self, arg):
        if arg.__class__ == str: return arg
        return [self._wrap_if_triple(x) for x in arg]