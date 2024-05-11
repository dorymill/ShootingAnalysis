# Match Class
# Top Level class for a match containing all of the stages
# in a given parent match.

from Stage import Stage
from Shooter import Shooter
import pandas as pd
import time

class Match():

    # Tracked shooter (statistical highlighting)
    trackedShooter = ""

    # Initialize instance attritbutes
    def __init__(self,  file, trackedShooter):

        self.fileName = file

        # List Stages inside of a match and list for their keys
        self.stageList = []
        self.stageKeys = []
        self.masterShooterList = []
        self.trackedShooter = trackedShooter

    # Populate stages with shooters
    def populateStages(self):

        # Grab the JSON as a pandas dataframe
        print("\nReading stage file. . .")
        self.dataFrame = pd.read_json(self.fileName)
        
        # Grab the stage keys that contain the word "Stage"
        for key in self.dataFrame.keys():
            if "stage" in key.lower() and 'UUID' not in key:
                self.stageKeys.append(key)
                print(f'Accepted Stage: {key}')

        # Create the stages iteratively
        for key in self.stageKeys:
            self.stageList.append(Stage (key, self.trackedShooter))

    def fillStages(self):
        start = time.time()
        print("\nAdding shooters to stages. . .")
        keyCounter = 1
        for stage in self.stageList:
            for divCounter in range(1,9):

                    divString = ""

                    if divCounter == 1:
                        divString = 'Carry Optics'
                    elif divCounter == 2:
                        divString = 'Limited'
                    elif divCounter == 3:
                        divString = 'Limited Optics'
                    elif divCounter == 4:
                        divString = 'Open'
                    elif divCounter == 5:
                        divString = 'PCC'
                    elif divCounter == 6:
                        divString = 'Production'
                    elif divCounter == 7:
                        divString = 'Revolver'
                    elif divCounter == 8:
                        divString = 'Single Stack'

                    # Grab the list of dicts for the shooters
                    shooterList = []
                    shooterList = self.dataFrame[stage.stageName][keyCounter][divCounter][divString]

                    for shooter in shooterList:
                        # Construct the master shooter list
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
            
            keyCounter += 1

        stop = time.time()    
        print(f'Done! ({stop - start:0.3f}s)')


if __name__ == "__main__":


    mtch = Match ("resultsfile.json", "Miller, Doryan")

    mtch.populateStages()
    mtch.fillStages()

    for stage in mtch.stageList:
        stage.loadAll()
        stage.showClassStats("G")


