from rdffwk.query_builder.abstracts import AbstractBuilder

class QueryBuilder(AbstractBuilder):

    def __init__(self, model) -> None:
        super().__init__(model)
   
    def build(self) -> str:
        query = "" if self.model.depth > 0 else self.prefixes()
        
        query += self.select()
        
        query += self.where()
        
        query += self.group_by()
        
        query += self.order_by()
        
        query += self.having()
        
        query += self.limit()
        
        query += self.offset()
        
        return query
    
    def prefixes(self) -> str:
        prefixes = ""
        for prefix, uri in self.model.prefixes.items():
            prefixes += f"PREFIX {prefix}: <{uri}>\n"
        return prefixes
    
    
    def select(self) -> str:
        var_str = "SELECT "
        for var in self.model.variables:
            var_str += f"{var} "
        var_str += "\n"
        return var_str
    
    def where(self) -> str:
        block = f"{self.OFF_WOP}WHERE {self._inner_block_builder()}"
    
        if block.count("\n") <= 3:
            block = block.replace("\n", "")
        
        return block
    
    def group_by(self) -> str:
        return self._solve_if_exists(self.model.grouping, "GROUP BY")
    
    def order_by(self) -> str:
        return self._solve_if_exists(self.model.ordering, "ORDER BY")
    
    def limit(self) -> str:
        return self._solve_if_exists(self.model.limit, "LIMIT")
    
    def offset(self) -> str:
        return self._solve_if_exists(self.model.offset, "OFFSET")
        
    def having(self) -> str:
        if(self.model.having == []): return ""
        
        if(self.model.grouping == None):
            raise SystemExit("HAVING clause without GROUP BY clause")
        
        having_str = f"{self.OFF_WOP}HAVING ("
        
        for i in range(len(self.model.having)):
            if(i != 0): having_str += " && "
            having_str += f"{self.model.having[i]}"
            
        having_str += ").\n"
        return having_str
    
    def _solve_if_exists(self, var, prefix) -> str:
        if(var == None): return ""
        return f"{self.OFF_WOP}{prefix} {var}\n"
    
