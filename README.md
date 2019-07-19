# PasswordGenerator

Created this for fun to make quick and easy passwords for myself. It works by loading the words into a dictionary
from a `.json` file. I know better solutions exist, but I was bored.

## Future Plans

- [x]  Add command line options
- [ ]  Add word count and length validation
- [ ]  Add password storage and manager
- [ ]  Add simple GUI

## Usage

### Python Version:

`Python 3.7.0`

### Required Files:

`words_dictionary.json` for the words.

### To Run:

`python main.py [-h] [-r] [-p] [words] [letters]`

#### positional arguments:  
* words
  * number of words in the password
  * requires letters  
* letters
  * number of letters in each word
  * requires words  

#### optional arguments:  
  * -h, --help     
    * show this help message and exit  
  * -r, --random   
    * produce a random password
  * -a, --alpha    
    * produce a random alpha numeric password  
  * -p, --private  
    * do not print password to console  

### Usage Examples:

* Basic Password Generation: 
  * `python main.py 4 4`
* Random Password: 
  * `python main.py -r`
* Random Alpha Numeric: 
  * `python main --alpha`
* Using Private Flag: 
  * `python main.py 4 4 -p` 
  * `python main.py -p --random`
* Help: 
  * `python main.py -h`

### Example Output:

```
Your password has been copied to your clipboard!
Password: thoodipsthowbaftkoko4
```
