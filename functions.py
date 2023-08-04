
def jaccard_index(text_a,text_b):  #reference: https://en.wikipedia.org/wiki/Jaccard_index  I should use the multiset version. 
    list_a =  list(text_a.strip(" "))
    list_b =  list(text_b.strip(" "))

    ordinary_intersection = list(set(list_a) & set(list_b))

    multiset_intersection_cardinality = 0
    for word in ordinary_intersection:  
       multiset_intersection_cardinality += min( list_a.count(word),list_b.count(word))  #This is just how multiset intersection is defined 

    multiset_union_cardinality = len(list_a) + len(list_b) 

    return multiset_intersection_cardinality/multiset_union_cardinality