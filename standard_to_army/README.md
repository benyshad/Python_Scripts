# Standard To Army

standard_to_army.py is a python script that prompts the user for there working hours in 12h or standard format and outputs the corresponding time in 24h format or army time.
The script will automatically add leading zero's after the time is converted to 24h format (example: 09:00)

The user input can be in either caps (example: PM) or lowercase
A space is not required between the numbers and am or pm (example: 8:54am or 8:54 am)




## Usage
The user is prompted for his / her working hours
```python
python3 standard_to_army.py
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