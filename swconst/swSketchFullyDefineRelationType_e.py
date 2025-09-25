from enum import IntEnum


class swSketchFullyDefineRelationType_e(IntEnum):
    """Sketch fully define relation types."""

    swSketchFullyDefineRelationType_Coincident = 512
    swSketchFullyDefineRelationType_Colinear = 32
    swSketchFullyDefineRelationType_Concentric = 64
    swSketchFullyDefineRelationType_Equal = 1
    swSketchFullyDefineRelationType_Horizontal = 2
    swSketchFullyDefineRelationType_Midpoint = 256
    swSketchFullyDefineRelationType_Parallel = 128
    swSketchFullyDefineRelationType_Perpendicular = 16
    swSketchFullyDefineRelationType_Tangent = 8
    swSketchFullyDefineRelationType_Vertical = 4

    def what(self):
        return {
            512: "Coincident relation",
            32: "Colinear relation",
            64: "Concentric relation",
            1: "Equal relation",
            2: "Horizontal relation",
            256: "Midpoint relation",
            128: "Parallel relation",
            16: "Perpendicular relation",
            8: "Tangent relation",
            4: "Vertical relation",
        }[self.value]