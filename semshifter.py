import csd, pollex, prototai, clics, stedt


def semshift(search_term):
    meanings = csd.semshift(search_term) + pollex.semshift(search_term) + prototai.semshift(search_term) + \
               clics.semshift(search_term) + stedt.semshift(search_term)
    return list(set(map(str.lower, meanings)))
