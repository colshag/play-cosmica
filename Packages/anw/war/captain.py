# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# captain.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This represents a starship captain
# ---------------------------------------------------------------------------
from anw.func import root, globals

class Captain(root.Root):
    """A StarShip Captain runs a starship, his rank/experience gives his starship bonuses"""
    def __init__(self, args):
        # Attributes
        self.id = str() # Unique Game Object ID
        self.name = str() # captains name
        self.myShipID = str() # current ship captain is on (id or '')
        self.empireID = str() # current empire captain is a part of
        self.experience = float() # captains experience points
        self.rankID = int() # captains rankID
        self.rank = str() # captains rank:('rookie','cadet','ensign','lieutenant','captain','commander','admiral')
        self.defaultAttributes = ('id', 'name', 'myShipID','empireID','experience', 'rank', 'rankID')
        self.setAttributes(args)
        
        self.myEmpire = None # Actual Empire object this Captain created by
        self.fullName = ''
        self.setRank()
        self.alive = 1
        
    def addExperience(self, amount):
        """When a captain destroys a starship his experience is increased"""
        self.experience += amount
        self.setRank()
        # change image if in shipbattle mode
        ##if self.myEmpire.myGalaxy.__module__ == 'anw.war.shipsimulator' and self.alive == 1:
            ##imageFileName = '%szcaptain%d.png' % (self.myEmpire.myGalaxy.game.app.genImagePath, self.rankID)
            ##self.setImage(imageFileName)
    
    def destroyMe(self):
        """Destroy Captain"""
        if self.alive == 1:
            self.alive = 0
    
    def promoteMe(self):
        """Special temporary promotion to next rank level if captain is a top captain in the galaxy"""
        return
    
    def resetData(self):
        """Reset Captain Data"""
        self.setRank(1)
    
    def setExperience(self, amount):
        """Set the Captain Experience"""
        self.experience = amount
        self.setRank()
    
    def setMyEmpire(self, empireObject):
        """Set the Ship Empire Owner"""
        self.empireID = empireObject.id
        self.myEmpire = empireObject
        self.myEmpire.myGalaxy.captains[self.id] = self

    def setMyShip(self, shipID):
        """Set the Ship captain is currently using"""
        self.myShipID = shipID
    
    def setMyName(self, name):
        """Set the captains new name"""
        self.name = name
        self.fullName = '<%s> %s' % (self.rank, self.name)
    
    def setRank(self, reset=0):
        """Set the Rank"""
        # experience is used to decide the rank of a starship captain
        if self.rank == globals.shipRank7 and reset == 0:
            pass
        elif self.experience < 100:
            self.rank = globals.shipRank0
            self.rankID = 0
        elif self.experience < 500:
            self.rank = globals.shipRank1
            self.rankID = 1
        elif self.experience < 1000:
            self.rank = globals.shipRank2
            self.rankID = 2
        elif self.experience < 2000:
            self.rank = globals.shipRank3
            self.rankID = 3
        elif self.experience < 4000:
            self.rank = globals.shipRank4
            self.rankID = 4
        elif self.experience < 10000:
            self.rank = globals.shipRank5
            self.rankID = 5
        else:
            self.rank = globals.shipRank6
            self.rankID = 6
        
        self.fullName = '<%s> %s' % (self.rank, self.name)
    
    def setMyPosition(self, myShip):
        """Set My Position"""
        width = myShip.graphicsObject.sourceObject.w
        height = myShip.graphicsObject.sourceObject.h
        self.posX = myShip.posX + width
        self.posY = myShip.posY + height
        
    def update(self, interval, world):
        """maintain captain position in world"""
        myShip = self.myEmpire.myGalaxy.ships[self.myShipID]
        self.setMyPosition(myShip)
        world.move(self, self.posX, self.posY, self.facing)
        self.graphicsObject.setState(self.posX, self.posY, self.facing)
        return self.alive
        