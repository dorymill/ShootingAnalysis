# Shooter Class
# Lowest Level class for a match containing the metrics
# for an individual shooters on a given parent stage.


class Shooter:

    # Attributes that we care about
    # Strings
    shooterName  = ""
    division     = ""
    shooterClass = ""
    parentStage  = ""


    # Numbers
    place         = -1
    stagePercent  = -1
    stageTimeSecs = -1
    stagePoints   = -1
    hitFactor     = -1
    points        = -1
    penalties     = -1

    def __init__(self,
                 parentStage,
                 shooterName,
                 division,
                 shooterClass,
                 place,
                 stagePercent,
                 stageTimeSecs,
                 stagePoints,
                 hitFactor,
                 points,
                 penalties):
        
        # Set string attributes
        self.parentStage  = parentStage
        self.shooterName  = shooterName
        self.division     = division
        self.shooterClass = shooterClass

        # Cast and set numeric attributes
        self.place         = int(place)
        self.stagePercent  = float(stagePercent)
        self.stageTimeSecs = float(stageTimeSecs)
        self.stagePoints   = float(stagePoints)
        self.hitFactor     = float(hitFactor)
        self.points        = float(points)
        self.penalties     = float(penalties)
