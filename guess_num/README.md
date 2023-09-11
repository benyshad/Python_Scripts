# Guess The Number Game

Guess The Number Game is a python script game that prompts the user for a level any number above 0 is valid.
A number between 0 and the level chosen by the user will be chosen at random (if the user chose 100, a number between 0 - 100 will be chosen at random). The user is then prompted to guess the number. After each attempt the computer will inform the user whether the correct number is larger or smaller than the users answer.



## Usage
```python
python3 guess_num.py
```

## Libraries

```python
import random
import sys

```

## Input Error Checking
Input error checking that has been implemented
1. Level must be a positive number