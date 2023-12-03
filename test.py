from rdffwk.create_variables import create_variables
from rdffwk.http_client.sparql_client import SparqlClient
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils import auxiliary_operators as aux

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph", None)

    #kb.prefixes = {
    #    "ex": "http://example.org/",
    #    "ex2": "http://example.org/2"
    #}
    
    human, gender = create_variables("human", "humanlabel", "gender")
    
    q1 = kb.query(human)\
        .where(human, "wdt:P21", gender)\
        .filter("wikibase:isSomeValue(?gender)")\
        .limit(3).to_sparql()\
     
    print(q1)
    
    #q3 = """PREFIX wd: <http://www.wikidata.org/entity/>
    #        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    #        SELECT ?item ?itemLabel WHERE {
    #            ?item wdt:P31 wd:Q146.
    #            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    #        } LIMIT 3"""
    
    client = SparqlClient("https://query.wikidata.org", timeout=100)
    
    client.send_and_parse(query=q1, export_file="test.csv")
    
    
if __name__=="__main__":
    main()