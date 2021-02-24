from typing import List

from cue import Cue
from cameras import Cameras
from media import Media


class CueList:
    def __init__(self):
        self.cameras = Cameras.get_defaults()
        self.media = Media.get_defaults()
        self.cues = []
