from rdffwk.create_variables import create_variables
from rdffwk.http_client.sparql_client import SparqlClient
from rdffwk.knowledge_base import KnowledgeBase
from rdffwk.utils import *


kb = KnowledgeBase(prefixes=None)

item, itemLabel, itemDescription, sitelinks = create_variables("item", "itemLabel", "itemDescription", "sitelinks")

q1 = kb.query(DISTINCT(item, itemLabel, itemDescription, sitelinks))\
    .where(item, [
        ("wdt:P31", "wd:Q146"), 
        ("wdt:P19/wdt:P131*", "wd:Q60"), 
        ("wikibase:sitelinks", sitelinks)
        ])\
    .service("wikibase:label", kb.block().where("bd:serviceparam", "wikibase:language", "\"[AUTO_LANGUAGE],en\""))\
        
print(q1.to_sparql())


p, c, pl, dl = create_variables("politician", "cause", "politician_label", "cause_of_death_label")

q2 = kb.query(p, c, pl, dl)\
    .where(p, [
        ("wdt:P106", "wd:Q82955"),
        ("wdt:P509", c)
    ])\
    .where(c, "wdt:P279*", "wd:Q12078")\
    .optional(kb.block().where(p, "rdfs:label", pl).filter(LANG(pl) == '"en"'))\
    .optional(kb.block().where(c, "rdfs:label", dl).filter(LANG(dl) == '"en"'))\
    .order_by(ASC(p))\

print(q2.to_sparql())