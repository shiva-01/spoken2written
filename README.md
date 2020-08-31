# spoken2written

## Install
a) Download or Clone the repository
b) Install it using pip: pip install spoken_to_written/

## Usage
###### Dependancy:<br>
 word2number to convert number in word format to numerical format

###### Step1: Import<br>
from spoken_to_written import spoken_to_written

###### Step2: Create an object:<br>
stw = spoken_to_written.stw()

stw class is responsible for handling the conversion of spoken to written.

You can also pass your set of rules for parsing text:

stw = spoken_t_written.stw(path_to_rules.json)

As of now only json file is supported for rules.

###### Step3: Parse:<br>
text = "My jersey number is 8"

stw.parse(text)

Output: `'My jersey number is 8'

stw.parse() takes in a string and returns a converted string.

###### Step4: Adding rules<br>
{
  "rules": [
    {
      "search": "YOUR SEARCH REGEX 1",
      "replace": "REPLACEMENT REGEX 1",
      "type": "regex"
    },
    {
      "search": "YOUR SEARCH REGEX 2",
      "replace": "REPLACEMENT REGEX 2",
      "type": "regex"
    },
  ]
}
