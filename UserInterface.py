from Calendar import Calendar
from Event import Event
import os

class UserInterface:

    def __init__(self):
        self.events = Event()
        self.calendar = Calendar()
        self.year = int()
        self.month = int()
        self.day = int()
        self.eventID = int()


    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def mainMenu(self):
        print('\n~~~~Welcome to your personal agenda~~~~\n')
        print('~~~ 1 - Print yearly calendar  (1921 - 2100)')
        print('~~~ 2 - Print monthly calendar (1 - 12)')
        print('~~~ 3 - Print All Events')
        print('~~~ 4 - Print Month with Events')
        print('~~~ 5 - Print Days with Events')
        print('~~~ 6 - Exit')

        option = int(input('\nEnter option number: '))

        if option == 1:
            self.printYear()
        elif option == 2:
            self.printMonth()
        elif option == 3:
            self.printAllEvents()
        elif option == 4:
            self.printMonthEvent()
        elif option == 5:
            self.printDayEvent()
        elif option == 6:
            return
        else:
            self.clearConsole()
            self.mainMenu()

    def eventMenu(self):
        print('>> 1 - Add New Event?')
        print('>> 2 - Update Event?')
        print('>> 3 - Remove Event?')
        print('>> 0 - Back to main menu')
        option = int(input('\n Choose option by number: '))
        if option == 1:
            self.addNewEvent()
        elif option == 2:
            self.updateEvent()
        elif option == 3:
            self.removeEvent()
        elif option == 0:
            self.mainMenu()

    def eventsMenu(self):
        print('>> 1 - Modify events?')
        print('>> 0 - Back to main menu')
        opt = int(input('\nPlease choose an option by number: '))
        if opt == 0:
            self.mainMenu()
        elif opt == 1:
            self.eventMenu()
        else:
            print('Wrong choice! Please check carefully and retry!')
            self.eventsMenu()

    def printYear(self):
        year = int(input('\nInsert year (1921 - 2100): \n'))
        self.calendar.printYear(int(year))
        self.backToMainMenu()

    def printMonth(self):
        year = int(input('\nInsert year (1921 - 2100): \n'))
        month = int(input('\nInsert month (1 - 12): \n'))
        self.calendar.printMonth(int(year), int(month))
        self.backToMainMenu()

    def printDayEvent(self):
        self.events.getAllEventsDatesByDay()
        self.year = int(input('\nInsert year (1921 - 2100): \n'))
        self.month = int(input('\nInsert month (1 - 12): \n'))
        self.day = int(input('\nInsert day: \n'))
        self.events.printEventsbyDay(int(self.year),int(self.month),int(self.day))
        self.eventsMenu()

    def printMonthEvent(self):
        self.events.getAllEventsDatesByMonth()
        self.year = int(input('\nInsert year (1921 - 2100): \n'))
        self.month = int(input('\nInsert month (1 - 12): \n'))
        self.events.printEventsbyMonth(int(self.year), int(self.month))
        self.eventsMenu()
        self.eventMenu()
    
    def addNewEvent(self):
        year = int(input('\nInsert year of new event (1921 - 2100): \n'))
        month = int(input('\nInsert month of new event (1 - 12): \n'))
        day = int(input('\nInsert day of new event: \n'))
        time = str(input('\nInsert time of new event: \n'))
        type = str(input('\nInsert type of new event: \n'))
        duration = str(input('\nInsert duration of new event: \n'))
        descr = str(input('\nInsert description of new event: \n'))
        self.events.addNewEvent(eventYear=int(year),eventMonth=int(month),
                                eventDay=int(day), eventTime= str(time),eventType=str(type),
                                eventDuration=str(duration),eventDescription=str(descr))
        print('Event added successfully!\n')
        self.backToMainMenu()
    
    def updateEvent(self):
        eventID = int(input('\nPlease select an event ID: '))
        eventList = list(self.events.getEventByID(eventID))
        print('>> 1 - Update year, month and day?')
        print('>> 2 - Update time?')
        print('>> 3 - Update type?')
        print('>> 4 - Update duration?')
        print('>> 5 - Update description?')
        print('>> 6 - Update all event details?')
        print('>> 0 - Back to main menu')
        option = int(input('\nChoose an option by number: '))
        if option == 1:
            year = int(input('\nPlease insert the updated year (1921 - 2100): '))
            month = int(input('\nPlease insert the updated month (1 - 12): '))
            day = int(input('\nPlease insert the updated day: '))
            self.events.updateEvent(eventID=eventID,evYear=year, evMonth=month,
                                    evDay=day, evType=eventList[4], evTime=eventList[3],
                                    evDuration=eventList[5], evDescription=eventList[6])
            print('Event updated successfully!')
            self.backToMainMenu()
        elif option == 2:
            time = str(input('\nPlease insert the updated time: '))
            self.events.updateEvent(eventID=eventID,evYear=eventList[0], evMonth=eventList[1],
                                    evDay=eventList[2], evType=eventList[4], evTime=time,
                                    evDuration=eventList[5], evDescription=eventList[6])
            print('Event updated successfully!')
            self.backToMainMenu()
        elif option == 3:
            type = str(input('\nPlease insert the updated type: '))
            self.events.updateEvent(eventID=eventID,evYear=eventList[0], evMonth=eventList[1],
                                    evDay=eventList[2], evType=type, evTime=eventList[3],
                                    evDuration=eventList[5], evDescription=eventList[6])
            print('Event updated successfully!')
            self.backToMainMenu()
        elif option == 4:
            duration = str(input('\nPlease insert the updated duration: '))
            self.events.updateEvent(eventID=eventID,evYear=eventList[0], evMonth=eventList[1],
                                    evDay=eventList[2], evType=eventList[4], evTime=eventList[3],
                                    evDuration=duration, evDescription=eventList[6])
            print('Event updated successfully!')
            self.backToMainMenu()
        elif option == 5:
            description = str(input('\nPlease insert the updated description: '))
            self.events.updateEvent(eventID=eventID,evYear=eventList[0], evMonth=eventList[1],
                                    evDay=eventList[2], evType=eventList[4], evTime=eventList[3],
                                    evDuration=eventList[5], evDescription=description)
            print('Event updated successfully!')
            self.backToMainMenu()
        elif option == 6:
            year = int(input('\nPlease insert the updated year (1921 - 2100): '))
            month = int(input('\nPlease insert the updated month (1 - 12): '))
            day = int(input('\nPlease insert the updated day: '))
            time = str(input('\nPlease insert the updated time: '))
            type = str(input('\nPlease insert the updated type: '))
            duration = str(input('\nPlease insert the updated duration: '))
            description = str(input('\nPlease insert the updated description: '))
            self.events.updateEvent(eventID=eventID,evYear=year, evMonth=month, evDay=day,
                                    evDescription=description, evDuration=duration,
                                    evTime=time, evType=type)
            print('Event updated successfully!')
            self.backToMainMenu()
        else:
            self.backToMainMenu()

    def printAllEvents(self):
        if len(self.events.getEvents()) == 0:
            print('There are no events in the system yet!')
            print('Do you want to add a new event?')
            print('\n >> 1 - Yes'
                  '\n >> 2 - No'
                  '\n >> 0 - Back to main menu')
            option = int(input('\n Please choose an option: '))
            if option == 0:
                return self.mainMenu()
            elif option == 1:
                return self.addNewEvent()
            else:
                self.backToMainMenu()
        else:
            self.events.printAllEvents()
            self.backToMainMenu()

    def removeEvent(self):
        self.events.printAllEvents()
        eventID = int(input('Please select an event ID to remove: '))
        self.events.removeEventByID(eventID)
        self.backToMainMenu()

    def backToMainMenu(self):
        print('Press 0 then Enter to turn back to main menu')
        userIn = int(input('\n >> 0 = Return to main menu\n'))
        if userIn == 0:
            self.clearConsole()
            self.mainMenu()
        else:
            print('Wrong choice!\n')
            self.backToMainMenu()
