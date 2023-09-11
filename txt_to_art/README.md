# Text To Art



## Description

Text to art is a python script which prompts the user for a line of text and outputs the text in an art form using the pyfiglet library

## Usage
text to art expects either 0 or 2 arguments.
If 0 arguments are given the default font will be used.
You can also specify the font with -f or --font


```python
python3 txt_to_art.py -f slant
```

## Libraries
```python
import pyfiglet
import sys
```
## Input Error Checking
Input error checking that has been implemented
1. Correct number of arguments were given.
2. Valid command line argument was given (-f or --font)
3. Valid font name was given
