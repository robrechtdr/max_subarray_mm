# Maximum subarray problem

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