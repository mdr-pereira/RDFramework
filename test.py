from rdffwk.create_variables import create_variables
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils import auxiliary_operators as aux
from rdffwk.utils.variable import Variable

def main():
    kb = KnowledgeBase("http://example.org/graph", "http://example.org/graph", None)

    kb.prefixes = {
        "ex": "http://example.org/",
        "ex2": "http://example.org/2"
    }
    
    s, o, f, s2 = create_variables("s", "o", "f", "s2") 
    
    q1 = kb.query(s, o)\
        .where(s, ":wb1", o)\
        .where(s, ":wb2", o)\
        .filter(s != o)\
        .bind(s, s2)\
        .group_by(aux.ASC(f))\
            

    print(q1.cache().query(f).where(f, ":wb3", o).filter(f > o).group_by(o).to_sparql())
     
    print(q1.to_sparql())

if __name__=="__main__":
    main()