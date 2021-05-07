# define iceberg class
class Iceberg():
    """Icebergs have coordinates (pixel square), height in m, mass if kg, and volume in m3. 
    Those less than 36mil kg mass can be pulled by an iceberg tug"""

    def __init__(self, ymin=none, ymax=none, xmin=none, xmax=none, height, volume, pull):
        self.y = pass           # from ice yes_or_no function
        self.x = pass           # from ice yes_or_no function
        self.height = pass      # from lidar data
        self.volume = volume    # maths
        self.pull = pass        # bool.  If mass less than 36 million kg = True.
    
    def volume(self):
        return(area*height)     # area of each ice pixel = 