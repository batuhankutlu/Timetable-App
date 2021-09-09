# Timetable-App

This is an activity recommendation app to use it in daily routines
------------------------------------------------------------------------
For accessing the same information and some screenshots please click [here](https://github.com/batuhankutlu/Timetable-App/files/7138950/How.to.use.pdf)
------------------------------------------------------------------------
First of all, thanks a lot for choosing that program to create timetables 😊

# Minimum System Requirements

Operating System: Any operating system<br>
CPU: Any CPU<br>
RAM: 7 MB<br>
Disk: 7 KB

# Installation
  To install Timetable app, you need to install Python 3 first.

## Installation of Python

  You can install Python, using that website: https://realpython.com/installing-python/<br>
  But make sure that, at the end of the installation you click the “Add Python 3.x to Path” button or add your Python installation to path.<br>

  If you already installed Python, you don’t need anything else to run the Timetable app.

# Usage of the program

## Configuring the Files
  
  That program uses JSON format (If you don’t know what JSON is, see: https://www.w3schools.com/whatis/whatis_json.asp) to save activities and contents (In that application, I used contents term instead of sub-activities.). There are two JSON file named “Activities.json” and “Log.json” (You may not see Log.json if the program runs first time).<br>
  
  In “Activities.json” file, there is an JSON array in an object named “Activites”, and that array has JSON objects. In these objects, there are four values; name, type, frequency, and contents. Name is a string value to save name of the activity. Type is a string value for splitting activities as work and free. Type must be “Work Time” or “Free Time”. Frequency is an integer value to save how often you want to take on with that activity. Lastly, contents are a JSON array, and it takes contents of that activity. Contents array has objects which has two values named name and frequency. Name and frequency of contents array object has the same meaning with Activities object.<br>
  
  In “Log.json” file, there is a JSON Object named “Log” and in that object there is a JSON array value which includes activity usage of the program (Don’t be scared, the program will refresh Log.json file when that file reaches (Total activity frequencies)^2 log entries.) (Program uses that data for not giving same activity recommendation consecutively). In that history objects, there are two values named “Activity” and “Content” and they keeps activity and content names respectively.<br>
  
  In initial case, you just need to configure Activities.json file and start the program. To configure, you can change activity names, types, frequencies, and contents or even you can add or delete any activity or content. But be careful, when adding or deleting activities or contents, you need to add or delete curly bracelets and commas. If you forget that, the program will crash.<br>
  
## Launching the application

### Launching the app on Windows

  You can launch the app just double clicking to “Launch.bat” file. It opens a Command Prompt window, and, in that window, you can see which activity and content recommended by application.<br>
  
  In that step you can press any key to close the program. That’s it 😊<br>
 
### Launching the app on Mac OS or Linux

  First, you need to open a terminal in that folder and type “./file.sh” and you see that an information like in the “Launching the app on Windows” title.<br>

# For Any Problem and Suggestions…
  You can use issues page in the GitHub repository.
