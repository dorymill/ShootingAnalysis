# Match Class
# Top Level class for a match containing all of the stages
# in a given parent match.

from Stage import Stage
from Shooter import Shooter
from typing import List
import pandas as pd
import json

class Match:

    # File dataframe
    fileName = ""

    # List Stages inside of a match and list for their keys
    stageList = []
    stageKeys = []

    def __init__(self,  file):
        self.fileName = file


    # Populate stages with shooters
    def populateStages(self):

        # Grab the JSON as a pandas dataframe
        print("Reading stage file. . .")
        dataFrame = pd.read_json(self.fileName)
        
        # Grab the stage keys that contain the word "Stage"
        for key in dataFrame.keys():
            if "stage" in key.lower() and 'UUID' not in key:
                self.stageKeys.append(key)
                print(f'Accepted Stage: {key}')

        # Create the stages iteratively
        keyCounter = 1
        for key in self.stageKeys:

            # Iterate over the shooter list by division since overall
            # contains Nxshooters worth of objects, N = stages
            stage = Stage (key)

            count = 0
            totalShooters = 0
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
                shooterList = dataFrame[key][keyCounter][divCounter][divString]
                totalShooters += len(shooterList)
                print(f'Total Shooters in {key} | {totalShooters}')

                for shooter in shooterList:
                    count += 1
                    # Construct the shooter and add them to the stage!
                    newShooter = Shooter(

                        key,
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
                    # print(f'Add Shooter Functional Calls:\t\t{count}')
                    # print(f'Length of current shooterList:\t\t{len(stage.shooterList)}')

            
            self.stageList.append(stage)

            keyCounter += 1



if __name__ == "__main__":

    mtch = Match ("../resultsfile.json")

    mtch.populateStages()

    # This is showing 375, implying that everyone is being added 6x to every stage
    # albeit there being only ~63 calls to addShooter on any given stage
    stage = mtch.stageList[1]

    print(len(stage.shooterList))

    #stage1.showHitFactors ()

