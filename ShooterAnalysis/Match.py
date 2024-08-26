# Match Class
# Top Level class for a match containing all of the stages
# in a given parent match.

from Stage import Stage
from Shooter import Shooter
import pandas as pd
import time
import sys
import os

class Match():



    # Initialize instance attritbutes
    def __init__(self,  file, trackedShooter):

        self.fileName = file
        

        # List Stages inside of a match and list for their keys
        self.stageList = []
        self.stageKeys = []
        self.masterShooterList = []

        # Tracked shooter (statistical highlighting)
        self.trackedShooter = trackedShooter

        # Possible Shooter Divisions
        self.divisions = ["Carry Optics", "Limited", "Limited Optics", "Open", 
                "PCC", "Production", "Revolver", "Single Stack"]
    
        self.classes = ["G", "M", "A", "B", "C", "D", "U"]

    # Populate stages with shooters
    def populateStages(self):

        # Grab the JSON as a pandas dataframe
        print("\nReading stage file. . .")
        self.dataFrame = pd.read_json(self.fileName)
        shortFileName = self.fileName.split(".")[0]

        # Create the storage folders for artifacts
        os.makedirs(shortFileName, exist_ok=True)

        os.makedirs(shortFileName + "/Overall"   , exist_ok=True)
        os.makedirs(shortFileName + "/Class"     , exist_ok=True)
        os.makedirs(shortFileName + "/Division" , exist_ok=True)

        
        # Grab the stage keys that contain the word "Stage"
        for key in self.dataFrame.keys():
            if "stage" in key.lower() and 'UUID' not in key:
                self.stageKeys.append(key)
                print(f'Accepted Stage: {key}')

        # Create the stages iteratively
        for key in self.stageKeys:
            self.stageList.append(Stage (key, self.trackedShooter, shortFileName))

    def fillStages(self):
        start = time.time()
        print("\nAdding shooters to stages. . .")
        keyCounter = 1
        
        for stage in self.stageList:
            divCounter = 1
            for div in self.divisions:
                try:
                    # Grab the list of dicts for the shooters
                    shooterList = []
                    shooterList = self.dataFrame[stage.stageName][keyCounter][divCounter][div]

                    # Construct the master shooter list
                    for shooter in shooterList:
                        newShooter = Shooter(

                            stage.stageName,
                            shooter.get('shooterName'),
                            shooter.get('division'),
                            shooter.get('shooterClass'),
                            shooter.get('place'),
                            shooter.get('stagePercent'),
                            shooter.get('stageTimeSecs'),
                            shooter.get('stagePoints'),
                            shooter.get('hitFactor'),
                            shooter.get('points'),
                            shooter.get('penalties')
                        )

                        stage.addShooter(newShooter)

                    divCounter += 1
            
                except KeyError:
                    #print(f'Division "{div}" not present on {stage.stageName}.')
                    continue

                except IndexError:
                    # This isn't apparently an issue
                    #print(f'Json has different structure than expected.')
                    continue


            # Add the overall scores too the stage overallShooterList
            # since these %psbl's may differ
            overallList = []
            overallList = self.dataFrame[stage.stageName][keyCounter][0]['Overall']

            for shooter in overallList:
                newShooter = Shooter(
                    stage.stageName,
                    shooter.get('shooterName'),
                    shooter.get('division'),
                    shooter.get('shooterClass'),
                    shooter.get('place'),
                    shooter.get('stagePercent'),
                    shooter.get('stageTimeSecs'),
                    shooter.get('stagePoints'),
                    shooter.get('hitFactor'),
                    shooter.get('points'),
                    shooter.get('penalties')
                )

                stage.addShooterOverall(newShooter)
            
            keyCounter += 1

        stop = time.time()    
        print(f'Done! ({stop - start:0.3f}s)\n')


if __name__ == "__main__":

    # Avaliable Classes and Divisions
    classes = ["G", "M", "A", "B", "C", "D", "U"]
    divisions = ["Carry Optics", "Limited", "Limited Optics", "Open", 
                "PCC", "Production", "Revolver", "Single Stack"]

    # No class/division flag provided, show overall
    if(len(sys.argv) < 3):
        print("\nUsage: python Match.py <match.json> <Tracked Shooter> -<option flag> <option>")
        print("\nAvailable option flags:")
        print("\n\t-o\t\tShows tracked shooter compared to overall statistics.")
        print("\n\t-c <Class>\tShows tracked shooter compared to class. Ex: -c A")
        print("\n\t-d <Division>\tShows tracked shooter compared to division. Ex: -d \"Carry Optics\".")
        exit()

    # Process Overall statistics
    elif (len(sys.argv) == 4):
        if(sys.argv[3] != "-o"):
            print("\nMissing flag option. Did you mean -o?")
            exit()
        elif (sys.argv[3] == "-o"):
            mtch = Match(sys.argv[1], sys.argv[2])

            mtch.populateStages()
            mtch.fillStages()

            for stage in mtch.stageList:
                stage.loadAll()
                stage.showOverallStats()
        else:
            print("\nInvalid flag passed. Run \"python Match.py\" for available options.")

    # Process specific Statistics
    elif (len(sys.argv) == 5):
        if(sys.argv[3] == "-o"):
            print("\nToo many flag options! Did you mean -c or -d?")
            exit()

        # Process Class Statistics
        if (sys.argv[3] == "-c"):
            if(sys.argv[4] not in classes):
                print("\nInvalid Class selected. Options: G, M, A, B, C, D, U.")
            else:
                mtch = Match(sys.argv[1], sys.argv[2])

                mtch.populateStages()
                mtch.fillStages()

                for stage in mtch.stageList:
                    stage.loadAll()
                    stage.showClassStats(sys.argv[4])

        elif (sys.argv[3] == "-d"):
            if(sys.argv[4] not in divisions):
                print("\nInvalid Division selected. Options: Carry Optics, Limited, Limited Optics, Open, PCC, Production, Revolver, Single Stack.")
            else:
                mtch = Match(sys.argv[1], sys.argv[2])

                mtch.populateStages()
                mtch.fillStages()

                for stage in mtch.stageList:
                    stage.loadAll()
                    stage.showDivisionStats(sys.argv[4])

    # Invalid input
    else:
        print("\nInvalid runtime options. Run \"python Match.py\" for available options.")

