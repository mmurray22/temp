from typing import List


class Media:
    @staticmethod
    def get_defaults() -> List["Media"]:
        ids = [0, 1, 2]
        names = ["Stanford", "Transition", "Doorbell"]
        files = ["stanford.png", "transition.mp4", "doorbell.wav"]
        types = ["image", "video", "audio"]

        return [
            Cameras(i, f"{names[i]}-{media[i][i][i][i]}")
            for i in range(0, 3)
        ]

        def __init__(self, ids: int, name: str, files: str, types: str):
        self.ids = ids
        self.name = name
        self.files = files
        self.types = types

    def __repr__(self):
        return f"Media: <{self.ids}: {self.name}, {self.files}, {self.types}>"
