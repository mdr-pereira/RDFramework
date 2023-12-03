from rdffwk.create_variables import create_variables
from rdffwk.http_client.sparql_client import SparqlClient
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils import auxiliary_operators as aux

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph", None)

    kb.prefixes = {
        "ex": "http://example.org/",
        "ex2": "http://example.org/2"
    }
    
    s, o, f, s2 = create_variables("s", "o", "f", "s2") 
    
    q1 = kb.query(s, o)\
        .where(s, ":wb1", [o, ":wb5"])\
        .where(s, [(":wb2", o), (":kaf", "?x")])\
        .filter((s != o) | (s == s2))\
        .filter(s > o)\
        .bind(s + 10, s2)\
        .group_by(aux.ASC(f))\
        .having((s2 > 10) | (s != 4))\
            
    #print(q1.cache().query(f).where(f, ":wb3", o).filter(f > o).group_by(o).to_sparql())
     
    #print(q1.to_sparql())
    
    q3 = """PREFIX wd: <http://www.wikidata.org/entity/>
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>
            SELECT ?item ?itemLabel WHERE {
                ?item wdt:P31 wd:Q146.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            } LIMIT 3"""
    
    client = SparqlClient("https://query.wikidata.org", timeout=100)
    
    client.send_and_parse(q3)
    
    
if __name__=="__main__":
    main()