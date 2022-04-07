from pgerom.save import save, load
from PIL import Image

defaultDesc1 = """Discord Activity Factory"""

class template:
    def __init__(self, img:Image=None, icon:Image=None, description1=defaultDesc1, type="playing"):
        self.img = img
        self.icon = icon
        self.desc1 = description1
        self.type = type
