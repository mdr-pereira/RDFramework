
class QueryBuilder():

    def __init__(self, model) -> None:
        self.model = model
    
    def build(self) -> str:
        return self.build_prefixes() + self.build_select() + self.build_where()
    
    def build_prefixes(self) -> str:
        prefixes = ""
        for prefix, uri in self.model.prefixes.items():
            prefixes += f"PREFIX {prefix}: <{uri}>\n"
        return prefixes
    
    def build_select(self) -> str:
        variables = self.model.query.variables
        var_str = "SELECT "
        for var in variables:
            var_str += f"?{var} "
            
        return var_str + "\n"
    
    def build_where(self) -> str:
        where_str = "WHERE {\n"
        
        for triple in self.model.queue:
            where_str += f"    {triple}\n"
            
        return where_str + "}"