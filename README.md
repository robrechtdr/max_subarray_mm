# Maximum subarray problem

## Problem description

Write a function that takes a list of integers as input and returns the largest sum of a consecutive subsequence. 

For example, for the input `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` the solution is `6` (the sum of the consecutive subsequence `[4, -1, 2, 1]`).

Variations:

1. A subarray with a maximum length K. For an array of length N, it holds that 0 < K < N with N ≥ 2. The value of K is variable.
2. "Bitmask" over the subsequence. Modify the function so that it can take a "bitmask" as an argument. This argument is an arbitrary list of the digits 1 and 0 with a length < the length of the entire input. The length of the bitmask is also the length of the subsequence K. Here, each element is not counted if it is under the digit 0 and is counted if it is under the digit 1. 
For example: the sum of the subsequence `[4, -1, 2, 1]` with a bitmask `[1, 1, 0, 0]` is then `3`.

## Installation

Ideally create a virtual environment first, then run:

`python3 -m pip install requirements.txt`

> Assumes minimal version of python3.10 to support typing specification with union operator in function definitions.


## Testing 

Run the following:

`pytest`


> 'Soft' type check with `mypy max_subarray.py --implicit-optional --no-strict-optional -v` 
>
> To to be able to run some automated type checking 
> whilst keeping function definition headers not too verbose when they 
> have optional arguments with None as default.