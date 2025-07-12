from pydantic import BaseModel

class TrafficNode (BaseModel):
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.northEast = None
        self.northWest = None
        self.southEast = None
        self.southWest = None
        self.toNorthcount = 0
        self.toSouthCount = 0
        self.toEastCount = 0
        self.toWestCount = 0
        self.signal = False
    

trafficNode1 = TrafficNode()
trafficNode1.toNorthcount = 100
trafficNode1.toSouthCount = 50
trafficNode1.toEastCount = 30
trafficNode1.toWestCount = 20

trafficNode2 = TrafficNode()
trafficNode2.toNorthcount = 40
trafficNode2.toSouthCount = 40
trafficNode2.toEastCount = 30
trafficNode2.toWestCount = 20

trafficNode2.south = trafficNode1
trafficNode1.north = trafficNode2

trafficNode3 = TrafficNode()
trafficNode3.toNorthcount = 40
trafficNode3.toSouthCount = 20
trafficNode3.toEastCount = 0
trafficNode3.toWestCount = 0

trafficNode2.east = trafficNode3
trafficNode1.northEast = trafficNode3
trafficNode3.southWest = trafficNode1
trafficNode3.west = trafficNode2

trafficNode4 = TrafficNode()
trafficNode4.toNorthcount = 0
trafficNode4.toSouthCount = 0
trafficNode4.toEastCount = 0
trafficNode4.toWestCount = 20

trafficNode4.south = trafficNode3
trafficNode3.north = trafficNode4