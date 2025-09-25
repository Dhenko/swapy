from enum import IntEnum


class swEndConditions_e(IntEnum):
    """Feature end conditions."""

    swEndCondBlind = 0
    swEndCondThroughAll = 1
    swEndCondThroughNext = 2
    swEndCondOffsetFromSurface = 5
    swEndCondMidPlane = 6
    swEndCondUpToBody = 7
    swEndCondThroughAllBoth = 9
    swEndCondUpToSelection = 10
    swEndCondUpToNext = 11

    def what(self):
        return {
            0: "Blind end condition",
            1: "Through all",
            2: "Through next",
            5: "Offset from surface",
            6: "Mid-plane",
            7: "Up to body",
            9: "Through all both directions",
            10: "Up to selection",
            11: "Up to next",
        }[self.value]