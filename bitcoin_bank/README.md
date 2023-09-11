# Bitcoin Bank



## Description

Bitcoin bank is a python script which gets the current cost of bitcoin in real-time with the request python library and extracts the current price for a bitcoin from the response.json. It then returns the cost for the specified amount of bitcoins the user would like to purchase.
The user specifies the amount of bitcoin he wants as a command line argument.

## Usage

```python
python3 bitcoin_bank.py 100
```

## Libraries
```python 
import sys
import requests

```

## Input Error Checking
Input error checking that has been implemented
1. Correct amount of command line arguments were given
