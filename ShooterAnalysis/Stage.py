# Stage Class
# Mid Level class for a match containing all of the shooters
# for a given parent stage.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, rv_histogram
import math


class Stage:

    # Static class attributes
    classes  = ["G", "M", "A", "B", "C", "D", "U"]

    divisions = ["Carry Optics", "Limited", "Limited Optics", "Open", 
                "PCC", "Production", "Revolver", "Single Stack"]
    
    parameters = ["stagePercent", "stageTimeSecs", "stagePoints", "hitFactor", "points", "penalties"]
    
    # Tracked shooter (statistical highlighting)
    trackedShooter = ""

    # Instace class attribute initialization
    def __init__(self, stageName, trackedShooter):
        
        # Stage name
        self.stageName = stageName

        # List of shooters (list of dictionaries)
        self.shooterList = []
        self.trackedShooter = trackedShooter

        # Dictionaries containing stats for classes and divisions
        # Ex:
        #     classDict:
        #       - GM
        #          - Raw Data (np.array)
        #       - A
        #          - Raw Data (np.array)
        #              .
        #              .
        #              .
        #
        self.classDictionary    = {}
        self.divisionDictionary = {}
        self.overallDictionary  = {}
        self.crossDictionary    = {}

        # Populate the keys for each statistical dictionary
        for sClass in self.classes:
            self.classDictionary[sClass] = {

                'stagePercent'  : [],
                'stageTimeSecs' : [],
                'stagePoints'   : [],
                'hitFactor'     : [],
                'points'        : [],
                'penalties'     : [] 
            }

        for div in self.divisions:
            self.divisionDictionary[div] = {

                'stagePercent'  : [],
                'stageTimeSecs' : [],
                'stagePoints'   : [],
                'hitFactor'     : [],
                'points'        : [],
                'penalties'     : [] 
            }

        self.overallDictionary = {

            'stagePercent'  : [],
            'stageTimeSecs' : [],
            'stagePoints'   : [],
            'hitFactor'     : [],
            'points'        : [],
            'penalties'     : [] 

        }

        self.crossDictionary = {

            'stagePercent'  : [],
            'stageTimeSecs' : [],
            'stagePoints'   : [],
            'hitFactor'     : [],
            'points'        : [],
            'penalties'     : [] 
        }
        
    # Calculate class data
    def loadClassData(self):
        
        # Populate the class dictionary class by class
        for shooter in self.shooterList:
            if shooter.shooterClass == "G":
                self.classDictionary['G']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['G']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['G']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['G']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['G']['points']       .append(shooter.points)
                self.classDictionary['G']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "M":
                self.classDictionary['M']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['M']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['M']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['M']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['M']['points']       .append(shooter.points)
                self.classDictionary['M']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "A":
                self.classDictionary['A']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['A']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['A']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['A']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['A']['points']       .append(shooter.points)
                self.classDictionary['A']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "B":
                self.classDictionary['B']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['B']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['B']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['B']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['B']['points']       .append(shooter.points)
                self.classDictionary['B']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "C":
                self.classDictionary['C']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['C']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['C']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['C']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['C']['points']       .append(shooter.points)
                self.classDictionary['C']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "D":
                self.classDictionary['D']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['D']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['D']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['D']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['D']['points']       .append(shooter.points)
                self.classDictionary['D']['penalties']    .append(shooter.penalties)

            elif shooter.shooterClass == "U":
                self.classDictionary['U']['stagePercent'] .append(shooter.stagePercent)
                self.classDictionary['U']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.classDictionary['U']['stagePoints']  .append(shooter.stagePoints)
                self.classDictionary['U']['hitFactor']    .append(shooter.hitFactor)
                self.classDictionary['U']['points']       .append(shooter.points)
                self.classDictionary['U']['penalties']    .append(shooter.penalties)
            
        for sClass in self.classes:
            self.classDictionary[sClass]['stagePercent']  = np.array(self.classDictionary[sClass]['stagePercent'])
            self.classDictionary[sClass]['stageTimeSecs'] = np.array(self.classDictionary[sClass]['stageTimeSecs'])
            self.classDictionary[sClass]['stagePoints']   = np.array(self.classDictionary[sClass]['stagePoints'])
            self.classDictionary[sClass]['hitFactor']     = np.array(self.classDictionary[sClass]['hitFactor'])
            self.classDictionary[sClass]['points']        = np.array(self.classDictionary[sClass]['points'])
            self.classDictionary[sClass]['penalties']     = np.array(self.classDictionary[sClass]['penalties'])

    # Calculate division data
    def loadDivisionData(self):
        # Populate the class dictionary class by class
        for shooter in self.shooterList:
            if shooter.division == "Carry Optics":
                self.divisionDictionary['Carry Optics']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Carry Optics']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Carry Optics']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Carry Optics']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Carry Optics']['points']       .append(shooter.points)
                self.divisionDictionary['Carry Optics']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Limited":
                self.divisionDictionary['Limited']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Limited']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Limited']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Limited']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Limited']['points']       .append(shooter.points)
                self.divisionDictionary['Limited']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Limited Optics":
                self.divisionDictionary['Limited Optics']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Limited Optics']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Limited Optics']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Limited Optics']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Limited Optics']['points']       .append(shooter.points)
                self.divisionDictionary['Limited Optics']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Open":
                self.divisionDictionary['Open']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Open']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Open']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Open']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Open']['points']       .append(shooter.points)
                self.divisionDictionary['Open']['penalties']    .append(shooter.penalties)

            elif shooter.division == "PCC":
                self.divisionDictionary['PCC']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['PCC']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['PCC']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['PCC']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['PCC']['points']       .append(shooter.points)
                self.divisionDictionary['PCC']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Production":
                self.divisionDictionary['Production']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Production']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Production']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Production']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Production']['points']       .append(shooter.points)
                self.divisionDictionary['Production']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Revolver":
                self.divisionDictionary['Revolver']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Revolver']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Revolver']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Revolver']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Revolver']['points']       .append(shooter.points)
                self.divisionDictionary['Revolver']['penalties']    .append(shooter.penalties)

            elif shooter.division == "Single Stack":
                self.divisionDictionary['Single Stack']['stagePercent'] .append(shooter.stagePercent)
                self.divisionDictionary['Single Stack']['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.divisionDictionary['Single Stack']['stagePoints']  .append(shooter.stagePoints)
                self.divisionDictionary['Single Stack']['hitFactor']    .append(shooter.hitFactor)
                self.divisionDictionary['Single Stack']['points']       .append(shooter.points)
                self.divisionDictionary['Single Stack']['penalties']    .append(shooter.penalties)

        for division in self.divisions:
            self.divisionDictionary[division]['stagePercent']  = np.array(self.divisionDictionary[division]['stagePercent'])
            self.divisionDictionary[division]['stageTimeSecs'] = np.array(self.divisionDictionary[division]['stageTimeSecs'])
            self.divisionDictionary[division]['stagePoints']   = np.array(self.divisionDictionary[division]['stagePoints'])
            self.divisionDictionary[division]['hitFactor']     = np.array(self.divisionDictionary[division]['hitFactor'])
            self.divisionDictionary[division]['points']        = np.array(self.divisionDictionary[division]['points'])
            self.divisionDictionary[division]['penalties']     = np.array(self.divisionDictionary[division]['penalties'])

    # Load overall stage data
    def loadOverallData(self):
        for shooter in self.shooterList:
            self.overallDictionary['stagePercent'] .append(shooter.stagePercent)
            self.overallDictionary['stageTimeSecs'].append(shooter.stageTimeSecs)
            self.overallDictionary['stagePoints']  .append(shooter.stagePoints)
            self.overallDictionary['hitFactor']    .append(shooter.hitFactor)
            self.overallDictionary['points']       .append(shooter.points)
            self.overallDictionary['penalties']    .append(shooter.penalties)

        self.overallDictionary['stagePercent']  = np.array(self.overallDictionary['stagePercent'])
        self.overallDictionary['stageTimeSecs'] = np.array(self.overallDictionary['stageTimeSecs'])
        self.overallDictionary['stagePoints']   = np.array(self.overallDictionary['stagePoints'])
        self.overallDictionary['hitFactor']     = np.array(self.overallDictionary['hitFactor'])
        self.overallDictionary['points']        = np.array(self.overallDictionary['points'])
        self.overallDictionary['penalties']     = np.array(self.overallDictionary['penalties'])

    # Load the class, division, and overall structures in a sigle call
    def loadAll(self):
        self.loadClassData()
        self.loadDivisionData()
        self.loadOverallData()

    # Load Overlap of Class and Division
    def loadCrossData(self, division, sClass):
      for shooter in self.shooterList:
            if shooter.division == division and shooter.shooterClass == sClass:
                self.crossDictionary['stagePercent'] .append(shooter.stagePercent)
                self.crossDictionary['stageTimeSecs'].append(shooter.stageTimeSecs)
                self.crossDictionary['stagePoints']  .append(shooter.stagePoints)
                self.crossDictionary['hitFactor']    .append(shooter.hitFactor)
                self.crossDictionary['points']       .append(shooter.points)
                self.crossDictionary['penalties']    .append(shooter.penalties)

    # Calculate and show Class statistics
    def showClassStats(self, sClass):

        paraBins     = []
        paraBinWidth = []

        for para in self.parameters:

            data = self.classDictionary[sClass][para]

            q75, q25 = np.percentile(data, [75, 25])
            iqr = q75 - q25
            N = data.size

            if(N <= 5):
                print(f'Not enough data for statistics on {para} on {self.stageName}.')
                continue

            binWidth = 2*(iqr) / (N)**(0.3333333)
            bins     = 2*(np.max(data) - np.min(data)) / binWidth

            paraBins    .append(bins)
            paraBinWidth.append(binWidth)
 
             # Overflow handling
            if(not math.isfinite(bins)):
                bins = N

            # Plot the histogram.
            plt.hist(data, bins=int(bins), density=True, alpha=0.6, color='grey', edgecolor='white')

            # Plot a normal distribution over the histogram
            mu, std = norm.fit(data) 
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 1000)
            p = norm.pdf(x, mu, std)
            plt.plot(x, p, 'k', linewidth=1)
 
            # Capture and plot the trackedShooters metric here
            trackedParam = 0.
            for shooter in self.shooterList:
                if shooter.shooterName == self.trackedShooter:
                    if para == "stagePercent":
                        trackedParam = shooter.stagePercent
                    elif para == "stageTimeSecs":
                        trackedParam = shooter.stageTimeSecs
                    elif para == "stagePoints":
                        trackedParam = shooter.stagePoints
                    elif para == "hitFactor":
                        trackedParam = shooter.hitFactor
                    elif para == "points":
                        trackedParam = shooter.points
                    elif para == "penalties":
                        trackedParam = shooter.penalties

            plt.vlines(x = trackedParam, ymin = 0, ymax = norm.pdf(trackedParam, mu, std),
                                colors = 'blue',
                                label = f'{self.trackedShooter} ({trackedParam})')
            
            # Plot parameters
            plt.title(f'{para} Distribution for {self.stageName} ({sClass})')
            plt.legend()
            plt.set_cmap('gray')
            plt.xlabel(para)
            plt.ylabel("Amplitude")
            plt.show()
        
    # Calculate and show Stage Statistics
    def showOverallStats(self):
        
        paraBins     = []
        paraBinWidth = []

        for para in self.parameters:

            data = self.overallDictionary[para]

            # Determine number of bins and width
            q75, q25 = np.percentile(data, [75, 25])
            iqr = q75 - q25
            N = data.size

            if(N <= 5):
                print(f'Not enough data for statistics on {para} on {self.stageName}.')
                continue

            binWidth = 2*(iqr) / (N)**(0.3333333)
            bins     = 2*(np.max(data) - np.min(data)) / binWidth

            # Overflow handling
            if(not math.isfinite(bins)):
                bins = N

            paraBins    .append(bins)
            paraBinWidth.append(binWidth)

            # Plot the histogram.
            plt.hist(data, bins=int(bins), density=True, alpha=0.6, color='grey', edgecolor='white')

            # Plot a normal distribution over the histogram
            mu, std = norm.fit(data) 
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 1000)
            p = norm.pdf(x, mu, std)
            plt.plot(x, p, 'k', linewidth=1)

            # Capture and plot the trackedShooters metric here
            trackedParam = 0.
            for shooter in self.shooterList:
                if shooter.shooterName == self.trackedShooter:
                    if para == "stagePercent":
                        trackedParam = shooter.stagePercent
                    elif para == "stageTimeSecs":
                        trackedParam = shooter.stageTimeSecs
                    elif para == "stagePoints":
                        trackedParam = shooter.stagePoints
                    elif para == "hitFactor":
                        trackedParam = shooter.hitFactor
                    elif para == "points":
                        trackedParam = shooter.points
                    elif para == "penalties":
                        trackedParam = shooter.penalties

            plt.vlines(x = trackedParam, ymin = 0, ymax = norm.pdf(trackedParam, mu, std),
                                colors = 'blue',
                                label = f'{self.trackedShooter} ({trackedParam})')

            
            # Plot parameters
            plt.title(f'{para} Distribution for {self.stageName} (All Classes)')
            plt.set_cmap('gray')
            plt.xlabel(para)
            plt.ylabel("Probability")
            plt.show()
    
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
    