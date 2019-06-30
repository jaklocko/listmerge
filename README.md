# listmerge
## A simple python module to combine/merge two lists together.
##### This is what I pictured python doing in my head when I first encountered the zip() function.
##### Thankfully for the world at large, this was not how zip() worked.

------
This python module merges two lists together differently than zip().
It iterates from 0 to the length of the longer list, adding the value from list1 to merged, then the value from list2 to merged.
Finally, once the shorter list's values have been exhausted, it adds the remaining values from the longer list to the merged list.
It then returns the merged list.

------

Example 1:

```python
import listmerge as l

evens = [i for i in range(20) if i % 2 == 0]
odds = [i for i in range(20) if i % 2 != 0]

print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"Merged: {l.merge(evens,odds)}")
```
outputs: 

```python
Evens: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Odds: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Merged: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```



Example 2:

```python
import listmerge as l

evens = [i for i in range(25) if i % 2 == 0]
odds = [i for i in range(20) if i % 2 != 0]

print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"Merged: {l.merge(evens,odds)}")
```

outputs:

```python
Evens: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
Odds: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Merged: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24]
```
