class Player:
    def __init__(self, name, position, rushAttempts, rushYards, targets, receivingYards):
        self.name = name;
        self.position = position;
        self.rushAttempts = rushAttempts;
        self.rushYards = rushYards;
        self.targets = targets;
        self.receivingYards = receivingYards;
        self.rushingVolume = '0';
        self.rushingProduction = '0';
        self.receivingVolume = '0';
        self.receivingProduction = '0';
        self.scrimmageVolume = 0;
        self.scrimmageProduction = 0;
        self.scrimmageDelta = '0';
    
    def getName(self):
        return self.name;

    def getPosition(self):
        return self.position;

    def getRushingVolume(self):
        return str(self.rushingVolume);

    def getRushingProduction(self):
        return str(self.rushingProduction);

    def getRushingDelta(self):
        return str(round(self.rushingProduction - self.rushingVolume, 2));

    def getReceivingVolume(self):
        return str(self.receivingVolume);

    def getReceivingProduction(self):
        return str(self.receivingProduction);
    
    def getReceivingDelta(self):
        return str(round(self.receivingProduction - self.receivingVolume, 2));

    def getScrimmageVolume(self):
        return str(self.scrimmageVolume);

    def getScrimmageProduction(self):
        return str(self.scrimmageProduction);

    def getScrimmageDelta(self):
        return str(round(self.scrimmageProduction - self.scrimmageVolume, 2));

    #TODO turn these into their own functions. Format output in a table
    def __str__(self):
        return self.getName() + ' ' + self.getPosition() + ' ' +  self.getRushingVolume() + ' ' + self.getRushingProduction() + ' ' + self.getRushingDelta() + ' ' + self.getReceivingVolume() + ' ' + self.getReceivingProduction() + ' ' + self.getReceivingDelta() + ' ' + self.getScrimmageVolume() + ' ' + self.getScrimmageProduction() + ' ' + self.getScrimmageDelta();