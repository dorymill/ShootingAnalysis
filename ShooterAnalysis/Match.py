# Match Class
# Top Level class for a match containing all of the stages
# in a given parent match.

from Stage import Stage
from Shooter import Shooter
import pandas as pd

class Match():

    # File dataframe
    fileName = ""

    # List Stages inside of a match and list for their keys
    stageList = []
    stageKeys = []
    masterShooterList = []

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
            stage = Stage (str(key))

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
                shooterList = dataFrame[key][keyCounter][divCounter][divString]

                for shooter in shooterList:
                    # Construct the master shooter list
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

                    if stage.stageName == newShooter.parentStage:
                        stage.addShooter(newShooter)

            self.stageList.append(stage)

            keyCounter += 1
                




if __name__ == "__main__":

    mtch = Match ("resultsfile.json")

    mtch.populateStages()

    # This is showing 375, implying that everyone is being added 6x to every stage
    # albeit there being only ~63 calls to addShooter on any given stage
    # for stage in mtch.stageList:
    #     stage.prune() 


    stage = mtch.stageList[0]
    stage.prune()

    for shooter in stage.shooterList:
        print(f'{shooter.parentStage}')


    print(f'\nStage 1 has {len(stage.shooterList)} shooters.')

    # for shooter in stage.shooterList:
    #     print(f'Stage 1 Shooter parentStage: {shooter.parentStage}')
    #     print(f'Stage Name: {stage.stageName}')

