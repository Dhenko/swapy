"""Thin wall types."""
from enum import IntEnum


class swThinWallType_e(IntEnum):
    """Thin wall feature types in SOLIDWORKS."""

    swThinWallOneDirection = 0
    swThinWallOppDirection = 1
    swThinWallMidPlane = 2
    swThinWallTwoDirection = 3

    def what(self):
        return {
            0: "One direction",
            1: "Opposite direction",
            2: "Mid-plane",
            3: "Two directions",
        }[self.value]
