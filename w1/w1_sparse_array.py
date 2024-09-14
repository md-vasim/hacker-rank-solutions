strings = ["ab", "ab", "abc"]
queries = ["ab", "abc", "bc"]

def matchStrings_old(strings, queries):
    c = []
    p = []
    for q in queries:
        q_c = 0
        for s in strings:
            if q == s and q not in p:
                q_c += 1 
        c.append(q_c)
        p.append(q)

    return c

def matchStrings(strings, queries):
    
    sdict = dict()
    for s in strings:
        if s in sdict:
            sdict[s] += 1 
        else:
            sdict[s] = 1 
    c = []
    for q in queries:
        c.append(sdict.get(q, 0))
        
    return c


print(matchStrings(strings, queries))

