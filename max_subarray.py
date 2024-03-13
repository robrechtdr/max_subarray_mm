def max_subarray(array):
    # Assuming a subarray is min length of 2
    # Keep iterating over array until i == len(array) - 2 (penultimate)
    # per iter:
    #   Check subarray sum if not larger then latest largest
    
    i = 0
    j = 1
    
    # Can't set to 0; as updating mechanism wouldn't work properly if array
    # would be only negative numbers. 
    max_subarray_sum = None
    max_subarray = None

    while i <= len(array) - 2:
        pass

        subarray = array[i:j + 1]

        subarray_sum = sum(subarray)
        if not max_subarray:
            max_subarray = subarray
            max_subarray_sum = subarray_sum
        
        # Don't need to nest under else
        if subarray_sum > max_subarray_sum:
            max_subarray = subarray
            max_subarray_sum = subarray_sum

        if j == len(array) - 1:
            i += 1
            j = i + 1
        else:
            j += 1
          
    return max_subarray_sum


def max_subarray_var1(array):
    i = 0
    j = 0 # var 1: j can be same pos as i
    
    # Can't set to 0; as updating mechanism wouldn't work properly if array
    # would be only negative numbers. 
    max_subarray_sum = None
    max_subarray = None

    while i <= len(array) - 1: # var 1: i can now be last pos
        pass

        subarray = array[i:j + 1]

        subarray_sum = sum(subarray)
        if not max_subarray:
            max_subarray = subarray
            max_subarray_sum = subarray_sum
        
        # Don't need to nest under else
        if subarray_sum > max_subarray_sum:
            max_subarray = subarray
            max_subarray_sum = subarray_sum

        if j == len(array) - 1:
            i += 1
            j = i # var 1: j can be same pos as i
        else:
            j += 1
          
    return max_subarray_sum