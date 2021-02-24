from delta import Delta
from typing import Optional, List


class Cue:
    def __init__(
        self, number: int, name: str, changes: Optional[List[Changes]]
    ):
        self.number = number
        self.name = name
        self.changes = changes or []
