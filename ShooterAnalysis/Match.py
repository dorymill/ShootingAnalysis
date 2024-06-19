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

    # Possible Shooter Divisions
    divisions = ["Carry Optics", "Limited", "Limited Optics", "Open", 
                "PCC", "Production", "Revolver", "Single Stack"]

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
                divCounter = 1
                for div in self.divisions:
                    try:

                        # Grab the list of dicts for the shooters
                        shooterList = []
                        shooterList = self.dataFrame[stage.stageName][keyCounter][divCounter][div]

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

                        divCounter += 1
                
                    except KeyError:
                        print(f'Division "{div}" not present on {stage.stageName}.')

                keyCounter += 1

        stop = time.time()    
        print(f'Done! ({stop - start:0.3f}s)')


if __name__ == "__main__":


    mtch = Match ("match3.json", "Miller, Doryan")

    mtch.populateStages()
    mtch.fillStages()

    for stage in mtch.stageList:
        stage.loadAll()
        stage.showClassStats("C")
        # stage.showOverallStats()


