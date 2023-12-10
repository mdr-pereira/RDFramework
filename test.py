from rdffwk.http_client.sparql_client import SparqlClient
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils.auxiliary_operators import *

def main():
    kb = KnowledgeBase(prefixes={"dbpp": "http://dbpedia.org/property/"})
    
    #This could have been added above, but it is here to show that you can add prefixes after the knowledge base is created.
    kb.add_prefix("dbpr", "http://dbpedia.org/resource/")
    
    m, a, mc, ac, aw = kb.create_variables("movie", "actor", "movie_count", "actor_country", "award")
    
    query = kb.query("*")\
        .get_from("http://dbpedia.org")\
        .where(m, "dbpp:starring", a)\
        .optional(kb.block().where(a, "dbpp:academyAward", aw))\
        .query(DISTINCT(m), AS(COUNT((DISTINCT(aw))), mc))\
            .where(a, [("dbpp:birthPlace", ac), ("^dbpp:starring", m)])\
            .filter(ac == "dbpr:United_States")\
            .group_by(a)\
            .having(COUNT(DISTINCT(mc)) >= 50) # type: ignore
    
    print(query.to_sparql())
    
    #Or equivalently:
    
    main_query = kb.query("*")\
        .get_from("http://dbpedia.org")\
        .where(m, "dbpp:starring", a)\
        .optional(kb.block().where(a, "dbpp:academyAward", aw))\
    
    subquery = kb.query(DISTINCT(m), AS(COUNT((DISTINCT(aw))), mc))\
            .where(a, [("dbpp:birthPlace", ac), ("^dbpp:starring", m)])\
            .filter(ac == "dbpr:United_States")\
            .group_by(a)\
            .having(COUNT(DISTINCT(mc)) >= 50) # type: ignore
            
    main_query = main_query.query(subquery)
    
    print(query.to_sparql())
    
    
if __name__=="__main__":
    main()