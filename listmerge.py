def merge(list1, list2):
    merged = []

    longer = list1 if len(list1) >= len(list2) else list2

    # Perform the merge by iterating through the values of the lists, adding the values of each list to the merged list.
    # Once the shorter list has been entirely added, continue adding the remaining values from the longer list to the merged list.
    for i in range(int(len(longer))):
        try:
            merged.append(list1[i])
        except Exception as e:
            pass
        
        try:
            merged.append(list2[i])
        except Exception as e:
            pass
    
    return merged
