# Stage Class
# Mid Level class for a match containing all of the shooters
# for a given parent stage.

class Stage:

    # Stage name
    stageName = ""

    # List of shooters (list of dictionaries)
    shooterList = []

    # This shall be a list of tuples, (mean, std.dev) for each parameter, 
    # ordered by ranks, high to low
    divisonHFStats = []
    classHFStats   = []

    divisonTimeStats = []
    classTimeStats   = []

    divisonPenStats = []
    classPenStats   = []

    divisonPointStats = []
    classPointStats   = []

    divisonStagePointsStats = []
    classStagePointsStats   = []

    count = 0

    def __init__(self, stageName):
        self.stageName = stageName;
        

    # Run through the classs and populate the statistics
    def classStatistics(self):
        pass


    def divisionStatistics(self):
        pass

    def addShooter(self, shooter):
        if(shooter.parentStage == self.stageName):
            self.shooterList.append(shooter)
            self.count += 1
            #print(f'{shooter.parentStage} == {self.stageName}')

    def showHitFactors(self):

        print(f'Stage {self.stageName} Hit Factors\n')

        for shooter in self.shooterList:
            print(f'{shooter.shooterName} ({shooter.shooterClass}) \t\t\tHF: {shooter.hitFactor}')

    def getTotalShooters(self):
        print(f'\n{self.stageName} has {len(self.shooterList)} shooters.')
        return len(self.shooterList)
    
    def prune(self):
        # For some reason shooters from all of the other stages make it
        # into the individual shooterLists. Pruning the ones that don't belong.

        for shooter in self.shooterList:
            if str(shooter.parentStage) != str(self.stageName):
                self.shooterList.remove(shooter)