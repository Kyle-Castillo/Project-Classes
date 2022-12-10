# Project - Classes
# Made by Kyle Castillo
# Group: Kyle, Ali, John
# Class 2 and 3

class Facility():

    # This method adds and writes
    # the facility name to the file

    def addFacility(self):
        self.newFacility = input(str("Enter Facility name: \n"))
        return self.newFacility
    
    # This method  writes the facilities 
    # list to facilities.txt

    def writeListOfFacilitiesToFile(self):
        with open('facilities.txt', 'a') as newFaci:
            newFaci.write(self.newFacility + "\n")

    # This displays the list
    # of facilities

    def displayFacility(self):
        with open('facilities.txt') as facilities:
            for line in facilities:
               print (line)



class Laboratory():

    # This asks the user to enter the lab name
    # and costs and forms a Laboratory object
    
    def enterLaboratoryInfo(self):
        self.newLabName = input(str("Enter Laboratory facility:\n"))
        self.newLabCost = input("Enter Laboratry cost:\n")

        return self.newLabName, self.newLabCost
    
    # This formats the laboratory object
    # similar to the laboratories.txt 
    # file

    def formatLabInfo(self):
        self.newLab = self.newLabName + '_' + self.newLabCost
        return self.newLab

    # This adds and writes the lab name to the
    # file in the format of the data that
    # is in the file

    def addLabToFile(self):
        self.addLab = self.formatLabInfo()
        return self.addLab

    # This writes the list of labs into
    # the file laboratories.txt
    
    def writeListOfLabsToFile(self):
        with open('laboratories.txt', 'a') as addLabF:
            addLabF.write(self.addLabToFile() + "\n")

    # This displays the list
    # of laboratories
    
    def displayLabsList(self):
        displayLab = self.readLaboratoriesfile()
        return displayLab

    # This reads the laboratories.txt file and fill its 
    # contents in a list of Laboratory objects

    def readLaboratoriesfile(self):
        with open('laboratories.txt', 'r') as LabList:
            lines = LabList.readlines()
            for F, C in enumerate(lines):
                Facility, Cost = C.strip('\n').split('_')
                print(f'{Facility:15}{Cost}')
