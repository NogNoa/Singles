usage: standard_editor.py [-h] name

A line editor inspired by Unix ed

In the main command mode, enter an input of the form <action argument>
All actions are single letter. arguments are either an integer, nothing or either of '.' '*' without the apostrophes

Arguments:
Integer - Targets a specific line. Line indeces start at 0.
. -       Targets the line that is in focus.
* -       Targets all lines. 
empty   - Giving no additional argument always act as '.'

Actions:
c - Changes the line that is in focus. 
    . print the current focus.
    * targets the end of the file.

d - Deletes line.

e - Enters an edit mode that let you replace a segment of text with another.
    The syntax is old/new/old/new... Deleting a segment with a final / is possible.

i - Enters an input mode that let you insert text into the file.
    * targets the end of the file. 
    To exit the input mode enter a line consisting only of '.'
    When you do, focus will automatically pass to the end of the inserted text.

m- Moves by copy the line in focus to the target.
    md - deletes the original as well
    * targets the end of the file

p - prints line to the console.

q - Saves the file and exit the program.
    unique argument '!' to not save.

Back to Python's Help message:

positional arguments:
  name        Name of the file you want to edit

optional arguments:
  -h, --help  show this help message and exit
