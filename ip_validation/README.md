# IP Validation

ip_validation.py is a python script that validates that the given ip address is formatted correctly to be a valid ip address which is a #.#.#.# where each # is represented by a number between 0 - 255 and prints out valid or invalid.


## Usage
Takes an ip address as a command line argument
```python
python3 ip_validation.py 65.59.102.39
```

## Libraries

```python
import re
import sys
```

## Pytest
Pytest script has also been included
```python
pytest test.py
```