## Add elements
.add() method 

## Remove elements
- .remove() method
    - raises a key error if element is not present
- .discard() method
    - doesn't raise a key error if element is not present
- .clear() method
    - removes all elements
- .pop() method
    - return and remove a random element

## Check if element is in set
```
if 'elementA' in mySet:
    print('yes')
```

## Iterating
```
for element in mySet:
    print(element)
```
Order is not important

## Union and intersection 
- .union() method
- .intersection() method

## Difference of sets
### Difference
- .difference() method
- returns a set with all the elements from the setA that are not in setB

### Symmetric difference
- .symmetric_difference() method
- all elements that are in setA and setB except for those in intersection
- Hence, A.symmetric_difference(B) = B.symmetric_difference(A)

## Updating sets
- .update()
    - update the set by adding elements from another list
    - doesn't add duplicate elements 
- .intersection_update()
    - update the set by keeping only the elements in intersection
- .difference_update()
    - update the set by keeping only the elements in difference
    - hence, removing elements in intersection
- .symmetric_difference_update()
    - update the set by keeping all the elements in the two sets except for those in intersection

## Copying
.copy()

## Subset, superset, disjoint
- .issubset()
    - returns True if setA contains setB
- .issuperset()
    - returns True if setB contains setA
- .isdisjoint()
    - returns True if both sets have a null intersection (no same elements)

## Frozenset
- immutable version of normal set 
- remains the same after creation
- in other words, no addition, removal, discard, clearing, or update is allowed
- however, other set operations such as union, intersection and difference work  
- `my_frozenset = frozenset(iterable)`