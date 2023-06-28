# Cresting an empty set
b = set()
print(type(b))


#Adding values to an empty set
b.add(4)
b.add(4)
b.add(5) 
b.add(5)
b.add(5)
# b.add([4,5,6])  # We cannot add list in a set because it is non hashable. The items of list can be changed.
b.add((4,5,6))  # We can add tupple in a set.
# b.add({4:5})  # we cannot add a dictionary in set because it is not hashable.
print(b)


# There is no way to change items in sets.


# Length of the set
len(b)
print(len(b))   # Prints the length of the set


# Removal of an Item
b.remove(5)    # Remove 5 from the set p\b
# b.remove(15)   # throws an error while trying to remove 15 (which is not present in the set)
print(b)


# Removes a random element from the set.
print(b.pop)   
print(b)


# Empties the entire set 
print(b.clear)
print(b)


# Union and Intersection of two sets
c = {1, 2, 3, 4}
print(b.union(c)) # or print(b.union({1, 2, 3, 4}))
print(b.intersection({1, 2, 3, 4}))