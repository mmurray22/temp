from typing import List


class Cameras:
    @staticmethod
    def get_defaults() -> List["Cameras"]:
        ids = [0, 1]
        names = ["Close Up", "Wide Angle"]
        return [
            Cameras(i, f"{names[i]}-{cameras[i][i]}")
            for i in range(0, 2)
        ]

    def __init__(self, ids: int, name: str):
        self.ids = ids
        self.name = name

    def __repr__(self):
        return f"Cameras: <{self.ids}: {self.name}>"
