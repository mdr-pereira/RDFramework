
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
        variables = self.model.variables
        var_str = "SELECT "
        
        for var in variables:
            var_str += var + " "
            
        return var_str + "\n"
    
    def build_where(self) -> str:
        where_str = "WHERE\n{\n"
        
        for i in range(len(self.model.triples)):
            where_str += f"{self.model.triples[i]}."
            where_str += i == len(self.model.triples) - 2 and "\n" or ""
            
        return where_str + "\n}"