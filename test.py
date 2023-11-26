from rdffwk.create_variables import create_variables
from rdffwk.knowledge_base import KnowledgeBase

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph")

    kb.prefixes = {
        "ex": "http://example.org/",
        "ex2": "http://example.org/2"
    }
    
    s, o, f = create_variables("s", "o", "f") 
    
    q1 = kb.query(s, o)\
        .where(s, ":wb1", o)\
        .where(s, ":wb2", o)\
            .query(f)\

    print(q1.to_sparql())

if __name__=="__main__":
    main()