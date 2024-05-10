# Stage Class
# Mid Level class for a match containing all of the shooters
# for a given parent stage.

class Stage:

    # Instace class attribute initialization
    def __init__(self, stageName):
        # Stage name
        self.stageName = stageName

        # List of shooters (list of dictionaries)
        self.shooterList = []

        # This shall be a list of tuples, (mean, std.dev) for each parameter, 
        # ordered by ranks, high to low
        self.divisonHFStats = []
        self.classHFStats   = []

        self.divisonTimeStats = []
        self.classTimeStats   = []

        self.divisonPenStats = []
        self.classPenStats   = []

        self.divisonPointStats = []
        self.classPointStats   = []

        self.divisonStagePointsStats = []
        self.classStagePointsStats   = []
        

    # Run through the classs and populate the statistics
    def classStatistics(self):
        pass


    def divisionStatistics(self):
        pass

    def addShooter(self, shooter):
        if(shooter.parentStage == self.stageName):
            self.shooterList.append(shooter)

    def showHitFactors(self):

        print(f'Stage {self.stageName} Hit Factors\n')

        for shooter in self.shooterList:
            print(f'{shooter.shooterName} ({shooter.shooterClass}) \t\t\tHF: {shooter.hitFactor}')

    def getTotalShooters(self):
        print(f'\n{self.stageName} has {len(self.shooterList)} shooters.')
        return len(self.shooterList)
    