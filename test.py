from rdffwk.create_variables import create_variables
from rdffwk.http_client.sparql_client import SparqlClient
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils import *

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph", None)
    
    human, gender = create_variables("human", "gender")
    
    q1 = kb.query(DISTINCT(human))\
        .where(human, "wdt:P21", gender)\
        .service("wikibase:label", 'bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"')\
        .filter("wikibase:isSomeValue(?gender)")\
        .limit(3)\
     
    print(q1.to_sparql())
    
    #client = SparqlClient("https://query.wikidata.org", timeout=100)
    
    #client.send_and_parse(query=q1, export_file="test.csv")
    
    b1 = kb.block()\
        .where(gender, "wdt:Q21", ":woman")\
        
    b2 = b1.cache().where("wd:Q6581072", "wdt:P31", human)
        
    #q2 = q1.minus(b1).order_by(DESC(human)).values(human, [":Q6581072", ":Q5"])
    
    print(b1.to_sparql())
    print(b2.to_sparql())
    
    print(IN(human, [gender, "b"]))
    
    
if __name__=="__main__":
    main()