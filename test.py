from rdffwk.knowledge_base import KnowledgeBase

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph")

    kb.prefixes = {
        "ex": "http://example.org/",
        "ex2": "http://example.org/2"
    }
    
    q1 = kb.query("?s", "?p", "?o")\
        .where("?s", "?p", "?o")
    
    print(str(q1))

    q1.to_sparql()

if __name__=="__main__":
    main()