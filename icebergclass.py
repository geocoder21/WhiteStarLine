# define iceberg class
class Iceberg():
    """Icebergs have coordinates (1m pixel square), height in m, mass if kg, and volume in m3. 
    Those less than 36mil kg mass can be pulled by an iceberg tug"""

    def __init__(self):
        self.corner = corner    # from find_corner function
        
    
# create a method to find iceberg corners
    def find_corner(self):
        for y in range(len(radar)):
            for x in range(len(radar[self.y])):
                if radar[self.y][self.x] >= 100:
                    if radar[self.y+1][self.x] or radar[self.y][self.x+1]<=100:
                        corner==True
                    elif radar[self.y-1][self.x] or radar[self.y][self.x-1]<=100:
                        corner==True
                    else:
                        corner==False
        return(corner)
