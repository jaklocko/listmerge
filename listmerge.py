def merge(list1, list2):
    merged = []
    if len(list1) >= len(list2):
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1
    # longer = list1 if len(list1) >= len(list2) else list2
    # print(f"List1 is longer" if len(list1) >= len(list2) else f"List2 is longer")
    # print(f"List2 is longer" if len(list2) >= len(list1) else f"List1 is longer")
    # print(f"Length of longer list: {len(longer)}")
    for i in range(int(len(longer))):
        # print(f"i: {i}")
        # print(f"{len(all)}")
        try:
            # print(f"Merging list1[{i}]: {list1[i]} into merged")
            merged.append(longer[i])
        except Exception as e:
            # print(f"Exception raised in List1 try block: {e}")
            # print(f"Couldn't add {list1[i]} to merged because {i} is greater than the length of list1: {len(list1)}")
            continue
            # raise e
        
        try:
            # print(f"Merging list2[{i}]: {list2[i]} into merged")
            merged.append(shorter[i])
        except Exception as e:
            # print(f"Couldn't add {list2[i]} to merged because {i+1} is greater than the length of list1: {len(list2)}")
            # print(f"Exception raised in List2 try block: {e}")
            continue
            # raise e
    return merged

# evens = [i for i in range(25) if i % 2 == 0]
# odds = [i for i in range(20) if i % 2 != 0]

# mammals = ["cat", "dog", "mouse", "deer", "dolphin", "whale"]
# reptiles = ["parrot", "snake", "turtle", "alligator"]

# print(evens)
# print(odds)
# print(f"Length of evens: {len(evens)}")
# print(f"Length of odds: {len(odds)}")

# print(merge(evens,odds))
# print(merge(mammals,reptiles))