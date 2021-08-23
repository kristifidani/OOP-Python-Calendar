# Calendar application using OOP Python Concepts

- This project is about an event-based calendar application. This is implemented in Python programming language with the help of object-oriented programming concepts. Our implementation is a simple calendar that interacts through the console. It doesn’t have a graphical user interface implemented but a simple interface that contains different menus for interacting with the application. The application supports events on the calendar and operations like insert, update and delete. The calendar can print a year or a specific month within a year by not using any library.

- The calendar works with three data structures, two dictionaries, one for the months and one for the days for each month, a list for storing the weekdays (Monday to Sunday). It requires a range of years to define how many years will be built by the calendar and a variable to keep track of the current weekday of each day that is initialized on 5 (0 = Monday to 6 = Sunday) since our range starts with the year 1921 and 1/1/1921 appears to be a Saturday. The calendar can go up to the year 2100 and it can print a year or a month from the built calendar which is built first as a bit complex structure but is easily used in the printing methods. The events are stored inside the calendar application into a dictionary with the key as an event ID and as value a list containing all the event information i.e., event date (YYYY/MM/DD), time, type, duration and description.

- The user interface is mostly made out of printing statements and input prompts. These statements contain the possible actions that can be performed in each method. The methods are linked to each other and other classes as needed. The user interface class provides menus for the user to interact with, within this class we implemented also a method to clear the console screen (output screen). This class is used afterwards in the main file of the program where the class is initialized, and the main menu of the class is called. After the main menu is called, whatever option the user will choose, the menu will use the methods in the user interface class without turning back anymore to the main class. This enables a higher-level programming where the functions of the other classes of the application are not displayed on the main file of the application.
