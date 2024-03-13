def max_subarray(array: list[int | float]) -> int | float:
    """
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    Return the sum of numbers of the subarray with the largest sum. 

    Assumes the array and subarray min length is 2.
    """
    
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


def max_subarray_var1(array: list[int | float]) -> int | float:
    """
    >>> max_subarray_var1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    Return the sum of numbers of the subarray with the largest sum. 

    Assumes the array min length is 2 and subarray min length is 1.
    """
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


def max_subarray_var2(array: list[int | float], bitmask: list[int]=None, bitmask_start_i: int=None) -> int | float:
    """
    Return the sum of numbers of the subarray with the largest sum. 

    Takes a bitmask as additional argument

    >>> max_subarray_var2(
        array=[-2, 1, -3, 4, -1, 2, 1, -5, 4], 
        bitmask=[1, 1, 0, 0],
        bitmask_start_i=3
    )
    3

    In the case above the bitmask is applied starting from index 3 of the array.
    For every respective number with bitmask number 1: keep the number.
    For every respective number with bitmask number 0: ignore the 
    number (assume value 0). 
    
    So 4 in max subarray remains 4 because it has bitmask 1, 
    2 in max subarray turns to 0 because it has bitmask 0.


    This implementation assumes the purpose of the bitmask is only to change 
    the value of the final sum number, not affecting the process to determine 
    which subarray has the maximum sum. I.e. the sum returned will be based on
    the same subarray regardless of which bitmask is applied.

    Assumes the array min length is 1 and subarray min length is 1.
    """
    i = 0
    j = 0 # var 1: j can be same pos as i
    
    # Can't set to 0; as updating mechanism wouldn't work properly if array
    # would be only negative numbers. 
    max_subarray_sum = None
    max_subarray = None
    max_subarray_i = None # var2

    while i <= len(array) - 1: # var 1: i can now be last pos
        subarray = array[i:j + 1]

        subarray_sum = sum(subarray)
        if not max_subarray:
            max_subarray = subarray
            max_subarray_sum = subarray_sum
            max_subarray_i = i # var2
        
        # Don't need to nest under else
        if subarray_sum > max_subarray_sum:
            max_subarray = subarray
            max_subarray_sum = subarray_sum
            max_subarray_i = i # var2

        if j == len(array) - 1:
            i += 1
            j = i # var 1: j can be same pos as i
        else:
            j += 1
          
    if bitmask: # var 2
        max_subarray_len = len(max_subarray)

        def apply_bitmask(array: list[float|int], bitmask: list[int], bitmask_start_i:int) -> list[int|float]:
            """
            >>> apply_bitmask([2, 10, 2, 3, 6], [0, 0, 1], 1)
            [2, 0, 0, 3, 6]
            """

            # Get the version of the bitmask with same length as array
            head = array[:bitmask_start_i]
            tail = array[bitmask_start_i + len(bitmask):]
            normalized_bitmask = [1] * len(head) + bitmask + [1] * len(tail)

            result = []
            for i, num in enumerate(array):
                if normalized_bitmask[i] == 1:
                    result.append(num)
                elif normalized_bitmask[i] == 0:
                    result.append(0)
                else: 
                    raise ValueError('Bitmask can only contain 0 or 1')

            return result 
        
        bitmasked_array = apply_bitmask(
            array=array, 
            bitmask=bitmask, 
            bitmask_start_i=bitmask_start_i
        )

        bitmasked_max_subarray = (bitmasked_array[max_subarray_i : max_subarray_i + len(max_subarray)])
        return sum(bitmasked_max_subarray)

    return max_subarray_sum