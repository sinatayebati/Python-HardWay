# Reading Files

You know how to get input from a user with input or argv. Now you will learn about reading from a file. You may have to play with this exercise the most to understand what’s going on, so do the exercise carefully and remember your checks. Working with files is an easy way to erase your work if
you are not careful. This exercise involves writing two files. One is the usual ex15.py file that you will run, but the other is named ex15_sample.txt. This second file isn’t a script but a plain text file we’ll be reading in our script. Here are the contents of that file:

* This is stuff I typed into a file.
* It is really cool stuff.
* Lots and lots of fun to have in here.

What we want to do is open that file in our script and print it out. However, we do not want to just hard code the name ex15_sample.txt into our script. “Hard coding” means putting some bit of information that should come from the user as a string directly in our source code. That’s bad because we want it to load other files later. The solution is to use argv or input to ask the user what file to open instead of hard coding the file’s name.

A few fancy things are going on in this file, so let’s break it down real quickly:

* Lines 1–3 use argv to get a filename. Next we have line 5, where we use a new command, open. Right now, run pydoc open and read the instructions. Notice how, like your own scripts and input, it takes a parameter and returns a value you can set to your own variable. You just opened a file.

* Line 7 prints a little message, but on line 8 we have something very new and exciting. We call a function on txt named read. What you get back from open is a file, and it also has commands you can give it. You give a file a command by using the . (dot or period), the name of the command, and parameters, just like with open and input. The difference is that txt.read() says, “Hey txt! Do your read command with no parameters!”