# Shirt Overlay

shirt_overlay.py is a python script that takes in 2 images one being an image of a person and the second being a picture of a shirt and overlays the shirt on top of the person and saves the image to a new file.
The input image of the person is first resized to 600x600 and then the shirt overlay is then applied.


## Usage
Takes 2 arguments the input image of the person that you want to have the shirt overlay and the second argument is the output file where the file should be saved
```python
python3 shirt_overlay.py before.jpg after.jpg
```

## Libraries

```python
import sys
import os
from PIL import ImageOps
from PIL import Image
```

## Input Error Checking
Input error checking that has been implemented
1. Correct number of arguments were given.
2. Correct file type was given.
3. The input file does not have the same name as the output file.
