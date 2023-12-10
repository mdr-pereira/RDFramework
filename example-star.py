from rdffwk.knowledge_base_star import KnowledgeBaseStar
from rdffwk.utils.auxiliary_operators import *

kb = KnowledgeBaseStar(prefixes=None)

item, itemLabel, itemDescription, sitelinks = kb.create_variables("item", "itemLabel", "itemDescription", "sitelinks")
strpl_1 = kb.create_quoted_triple("wd:Q5", "wd:Q4167410", "wd:Q13442814")

q1 = kb.query(DISTINCT(item, itemLabel, itemDescription, sitelinks))\
    .where(
        item, [
        ("wdt:P31", strpl_1), 
        ("wdt:P19/wdt:P131*", "wd:Q60"), 
        ("wikibase:sitelinks", sitelinks)
        ])\
    .service("wikibase:label", kb.block().where("bd:serviceparam", "wikibase:language", STR("[AUTO_LANGUAGE],en")))\
    .query(COUNT(item))\
    .where(item, "wdt:P31", "wd:Q5")\
        
print(q1.to_sparql())

p, c, pl, dl = kb.create_variables("politician", "cause", "politician_label", "cause_of_death_label")
strpl_2 = kb.create_quoted_triple(p, "wdt:P31", pl)

q2 = kb.query(p, c, pl, dl)\
    .where(
        (p, "wdt:P31", pl), [
        ("wdt:P106", "wd:Q82955"),
        ("wdt:P509", c)
    ])\
    .where(c, "wdt:P279*", "wd:Q12078", [("asg", "asfgf"), ("adfgfga", "bhagbfg")])\
    .optional(kb.block().where(p, "rdfs:label", pl).filter(LANG(pl) == STR("en")))\
    .optional(kb.block().where(c, "rdfs:label", dl).filter(LANG(dl) == STR("en")))\
    .order_by(ASC(p))\

print(q2.to_sparql())