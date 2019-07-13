# PasswordGenerator

Created this for fun to make quick and easy passwords for myself. It works by loading the words into a dictionary
from a `.json` file. I know better solutions exist, but I was bored.

## Future Plans

- [x]  Add command line options
- [ ]  Word count and length validation
- [ ]  Simple GUI

## Usage

### Python Version:

`Python 3.7.0`

### Required Files:

`words_dictionary.json` for the words.

### To Run:

Optional flags:
-w, --words - Number of words <br>
-l, --letters - Number of letters <br>
-p - if this flag is set, the script will copy the result to the clipboard instead of printing to the console. <br>

### Examples:

```
python password_generator.py -w=4 -l=6
```

```
python password_generator.py -w=3 -l=7 -p
```

### Example Output:

`shptilexhockdaza2`  
`murrshahstimaddu7`  
`oradcolycawlheir5`
