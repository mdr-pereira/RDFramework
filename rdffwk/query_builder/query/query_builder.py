from rdffwk.query_builder.abc_builder import AbstractBuilder

class QueryBuilder(AbstractBuilder):

    def __init__(self, model) -> None:
        super().__init__(model)
   
    def build(self) -> str:
        query = ""
        
        query += "" if self.model.depth != 0 else self.prefixes()
        
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
        variables = self.model.variables
        var_str = "SELECT "
        
        if(variables.__class__ != tuple):
            var_str += f"{variables}"
        else:    
            for var in variables:
                var_str += f"{var} "
                    
        return var_str + "\n"
    
    def where(self) -> str:
        where_str = f"{self.OFF_WOP}WHERE {{\n"
        where_str += self.triples()
        where_str += self.filters()
        where_str += self.sub_queries()
        where_str += self.values()
        where_str += self.bind()
        where_str += self.services()
        where_str += f"{self.OFF_WOP}}}\n"
        return where_str
    
    def group_by(self) -> str:
        if(self.model.grouping == None): return ""
    
        return f"{self.OFF_WOP}GROUP BY {self.model.grouping}\n"
    
    def order_by(self) -> str:
        if(self.model.ordering == None): return ""
        
        return f"{self.OFF_WOP}ORDER BY {self.model.ordering}\n"
    
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
    
    def limit(self) -> str:
        if(self.model.limit == None): return ""
        
        return f"{self.OFF_WOP}LIMIT {self.model.limit}\n"
    
    def offset(self) -> str:
        if(self.model.offset == None): return ""
        
        return f"{self.OFF_WOP}OFFSET {self.model.offset}\n"