
class Event:
    def __init__(self):
        self.events = dict()
        self.evID = 0

    def addNewEvent(self, eventYear, eventMonth, eventDay,
                    eventTime, eventType, eventDuration,
                    eventDescription):
        event = [eventYear, eventMonth, eventDay,
                 eventTime, eventType,eventDuration,
                 eventDescription]
        self.events[self.evID] = event
        self.evID += 1


    def printEventsbyMonth(self, eventYear, eventMonth):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('{0} {1}'.format('Events for ', self.getMonthNameByNumber
            (
            month=eventMonth,
            year=eventYear
            )).center(30, '~'))
        for key, evlist in self.events.items():
            if isinstance(evlist, list):
                if evlist[0] == eventYear and evlist[1] == eventMonth:
                    print('Event ID-{0}: {1} on {2}/{3}/{4} at {5} with a duration of {6}.'
                          .format(key, evlist[4],
                                  evlist[0], evlist[1],
                                  evlist[2], evlist[3],
                                  evlist[5]
                                  ))
                    print('Description: {0}'.format(evlist[6]))
                    print('\n')


    def printEventsbyDay(self, eventYear, eventMonth, eventDay):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('{0} {1} {2}'.format('Events for ', self.getMonthNameByNumber
            (
            month=eventMonth, year=eventYear
            ),
                                   eventDay).center(30, '~'))
        for key, evlist in self.events.items():
            if isinstance(evlist, list):
                if evlist[0] == eventYear and evlist[1] == eventMonth and evlist[2] == eventDay:
                    print('Event ID-{0}: {1} on {2}/{3}/{4} at {5} with a duration of {6}.'
                          .format(key, evlist[4],
                                evlist[0], evlist[1],
                                evlist[2], evlist[3],
                                evlist[5]))
                    print('Description: {0}'.format(evlist[6]))
                    print('\n')

    def removeEvent(self, eventYear, eventMonth, eventDay, eventTime, eventDuration):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('Removing Event...')
        for key, evlist in self.events.items():
            if isinstance(evlist, list):
                if evlist[0] == eventYear and evlist[1] == eventMonth and evlist[2] == eventDay:
                    if evlist[3] == eventTime and evlist[5] == eventDuration:
                        self.events.pop(key)
                        print('Removed Successfully!')
                        break

    def removeEventByID(self, eventID):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        if self.events.get(eventID) != None:
            self.events.pop(eventID)
        else:
            print('Event ID Incorrect or doesn\'t exist')

    # Used for updating event in the user interface
    def getEventByID(self, eventID):
        if self.events.get(eventID) == None: return 'Event ID incorrect or doesn\'t exist!'
        return list(self.events.get(eventID))

                
    def updateEvent(self, eventID, evYear, evMonth, evDay, evTime, evType, evDuration, evDescription):
        if len(self.events) == 0:
            print('There are no events!\n')
            return 
        self.events[eventID] = [evYear, evMonth, evDay, evTime, evType, evDuration, evDescription]

    def updateEventByDay(self, eventYear, eventMonth, eventDay, eventTime, eventDuration):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        for key in self.events.keys():
            if isinstance(self.events.get(key), list):
                evList = list(self.events.get(key))
                if evList[0] == eventYear and evList[1] == eventMonth and evList[2] == eventDay:
                    self.printEventsbyDay(eventYear,eventMonth,eventDay)
                    eventID = int(input('Enter event ID: '))
                    if key+1 == eventID:
                        evList[0] = int(input('Update year: '))
                        evList[1] = int(input('Update month: '))
                        evList[2] = int(input('Update day: '))
                        evList[3] = str(input('Update time: '))
                        evList[4] = str(input('Update type: '))
                        evList[5] = str(input('Update duration: '))
                        evList[6] = str(input('Update description: '))

    def getMonthNameByNumber(self, year, month):
        from Calendar import Calendar
        cal = Calendar()
        cal.printMonth(month= month, year= year)
        return cal.months[month]
    
    #Methods to print all events dates in the format YYYY/MM/DD
    def getAllEventsDatesByDay(self):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('All dates with events YYYY/MM/DD')
        months = set()
        for key, evlist in self.events.items():
            months.add((evlist[0], evlist[1], evlist[2]))
        for year, month, day in months:
            print('>> {0}/{1}/{2}\n'.format(year, month, day) )

    def getAllEventsDatesByMonth(self):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('All dates with events YYYY/MM/DD')
        months = set()
        for key, evlist in self.events.items():
            months.add((evlist[0], evlist[1]))
        for year, month in months:
            print('>> {0}/{1}\n'.format(year, month))

    #Method to print all the events of the application
    def printAllEvents(self):
        if len(self.events) == 0:
            print('There are no events!\n')
            return
        print('All Events')
        for key, evlist in self.events.items():
            print('Event ID-{0}: {1} on {2}/{3}/{4} at {5} with a duration of {6}.'
                  .format(key, evlist[4],
                        evlist[0], evlist[1],
                        evlist[2], evlist[3],
                        evlist[5]))
            print('Description: {0}'.format(evlist[6]))
            print('\n')
            
    def isEmpty(self):
        isEmpty = False
        if len(self.events != 0): 
            isEmpty = False 
        else: 
            isEmpty = True
        return isEmpty
    
    def getEvents(self):
        return self.events