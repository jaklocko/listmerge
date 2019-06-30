def merge(list1, list2):
    merged = []

    if len(list1) >= len(list2):
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1

    # Perform the merge by iterating through the values of the lists, adding the values of each list to the merged list.
    # Once the shorter list has been entirely added, continue adding the remaining values from the longer list to the merged list.
    for i in range(int(len(longer))):
        try:
            merged.append(longer[i])
        except Exception as e:
            continue
        
        try:
            merged.append(shorter[i])
        except Exception as e:
            continue
    
    return merged
