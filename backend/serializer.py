from cue_list import CueList
from cue import Cue
from delta import Delta
from typing import Dict, Any, Optional


def serialize(cues: CueList) -> dict:
    data: Dict[str, Any] = {
        "cameras": [],
        "media": [],
        "cues": [],
    }

    for cameras in cues.cameras:
        data["cameras"] += [
            {
                "id": cameras.id,
                "name": cameras.name,
            }
        ]
    for media in cues.media:
        data["media"] += [
            {
                "name": media.name,
                "id": media.id,
                "file": media.file,
                "type": media.type,
            }
        ]

    for cue in cues.cues:
        data["cues"] += [
            {
                "number": cue.number,
                "name": cue.name,
                "changes": [
                    {
                        "type": changes.type,
                        "time": changes.time,
                        "media_id": changes.media_id,
                        "action": [
                            {
                                "type": action.type,
                                "config": [
                                    {
                                        "view": [
                                            {
                                                "top": view.top,
                                                "right": view.right,
                                                "bottom": view.bottom,
                                                "left": view.left,
                                                "z": view.z,
                                            }
                                        ],
                                        "playback": [
                                            {
                                                "volume": playback.volume,
                                                "playing": playback.playing,
                                                "done": playback.done,
                                            }
                                        ],
                                    }
                                ],

                            }
                        ]
                    },
                    {
                        "type": changes.type,
                        "time": changes.time,
                        "camera_id": changes.camera_id,
                        "action": [
                            {
                                "type": action.type,
                                "config": [
                                    {
                                        "view": [
                                            {
                                                "top": view.top,
                                                "right": view.right,
                                                "bottom": view.bottom,
                                                "left": view.left,
                                                "z": view.z,
                                            }
                                        ],
                                    }
                                ],

                            }
                        ]
                    },
                    {
                            "type": changes.type,
                            "cue_type": changes.cue_type,
                            "cue_number": changes.cue_number,
                    },
                ]
            }
        ]
    return data


def deserialize(data: dict) -> Optional[CueList]:
    _ = data.get("cameras", [])  # Can't change this
    _ = data.get("media", [])  # Can't change this
    cues = data.get("cues", [])
    lst = CueList()
    cameras = {c.id: c for c in lst.cameras}
    media = {c.id: c for c in lst.media}
    numbers = set()
    
    for cue in cues:
        name = cue.get("name", "")
        number = cue.get("number")
        if change is None:
            return None
        if number is None:
            return None
        if number in numbers:
            return None
        numbers |= {number}
        changes = cue.get("changes", [])
        change_final = []
        for c in changes:
            types = c.get("type")
            time = c.get("time")
            media_id = d.get("media_id")
            action = d.get("action")
            if types is None or media_id is None or time is None or action is None:
                return None
            changes += [Changes(types, media_id, time, action)]
        lst.cues += [Cue(number, name, change_final)]
    return lst
