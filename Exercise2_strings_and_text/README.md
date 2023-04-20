# Strings and Text

While you have been writing strings, you still do not know what they do. In this exercise we create
a bunch of variables with complex strings so you can see what they are for. First an explanation
of strings.
A string is usually a bit of text you want to display to someone or “export” out of the program you are
writing. Python knows you want something to be a string when you put either " (double-quotes) or '
(single-quotes) around the text. You saw this many times with your use of print when you put the text
you want to go inside the string inside " or ' after the print to print the string.
Strings can contain any number of variables that are in your Python script. Remember that a variable
is any line of code where you set a name = (equal) to a value. In the code for this exercise,
types_of_people = 10 creates a variable named types_of_people and sets it = (equal) to 10.
You can put that in any string with {types_of_people}. You also see that I have to use a special type
of string to “format”; it’s called an “f-string” and looks like this:

* f"some stuff here {avariable}"
* f"some other stuff {anothervar}"

Python also has another kind of formatting using the .format() syntax, which you see on line 17. You’ll
see me use that sometimes when I want to apply a format to an already-created string, such as in a loop.
We’ll cover that more later.
We will now type in a whole bunch of strings, variables, and formats, and print them. We will also practice
using short, abbreviated variable names. Programmers love saving time at your expense by using
annoyingly short and cryptic variable names, so let’s get you started reading and writing them early on.