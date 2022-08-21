from hexicapi.save import save, load
from PIL import Image

defaultName = """Discord Activity Factory"""
defaultDesc1 = """Messing with discord"""
defaultDesc2 = """Making an activity"""

class template:
    def __init__(self, img:str='icon', icon:str='icon', description1:str=defaultDesc1, description2:str=defaultDesc2, typeD:str="playing", start:int=None):
        self.img = img
        self.icon = icon
        self.desc1 = description1
        self.desc2 = description2
        self.type = typeD
        self.start = start
