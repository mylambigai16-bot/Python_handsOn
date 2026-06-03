def set_intersection_count(sets):
    common_elements = sets[0]
    for s in sets[1:]:
        common_elements = common_elements.intersection(s)
    
    return len(common_elements)

print(set_intersection_count([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]))  
print(set_intersection_count([{'a', 'b'}, {'b', 'c'}, {'c', 'd'}])) 