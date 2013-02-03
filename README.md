Chives
======

A personal butler for your computer, always listening in the background and ready to serve your needs. Heavily
inspired by Github's Hubot.

Scripts
=======

You can add scripts for Chives to run by adding the script to the 'scripts' folder. The script itself must be
in a class named 'ScriptHandler' with a list of regular expressions which the script will respond to named
'commands'. Finally, the class must have a method named 'runScript' which will respond to the request. 