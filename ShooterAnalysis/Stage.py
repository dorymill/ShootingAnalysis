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
        self.shooterList.append(shooter)
        self.count += 1
        #print(f'{shooter.shooterName} ({shooter.shooterClass})\n\t\t\t added to {self.stageName} (#{self.count})')

    def showHitFactors(self):

        print(f'Stage {self.stageName} Hit Factors\n')

        for shooter in self.shooterList:
            print(f'{shooter.shooterName} ({shooter.shooterClass}) \tHF: {shooter.hitFactor}')

    def getTotalShooters(self):
        print(f'\n{self.stageName} has {len(self.shooterList)} shooters.')
        return len(self.shooterList)