
class QueryBuilder():

    def __init__(self, model) -> None:
        self.model = model
        self.isSubQuery = model.isSubQuery
    
    def build(self) -> str:
        query = ""
        
        query += "" if self.isSubQuery else self.prefixes()
        
        query += self.select()
        
        query += self.where()
        
        query += self.sub_queries()
        
        query += "}"
        
        return query
    
    def prefixes(self) -> str:
        prefixes = ""
        for prefix, uri in self.model.prefixes.items():
            prefixes += f"PREFIX {prefix}: <{uri}>\n"
        return prefixes
    
    def select(self) -> str:
        variables = self.model.variables
        var_str = "SELECT "
        
        for var in variables:
            var_str += var + " "
            
        return var_str + "\n"
    
    def where(self) -> str:
        where_str = "WHERE\n{\n"
        
        for i in range(len(self.model.triples)):
            where_str += f"{self.model.triples[i]}.\n"
            
        return where_str
    
    def sub_queries(self) -> str:
        sub_queries = ""
        
        for query in self.model.subQueries:
            sub_queries += query.to_sparql() + "\n"
            
        return sub_queries