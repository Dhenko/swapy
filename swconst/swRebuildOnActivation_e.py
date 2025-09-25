from enum import IntEnum


class swRebuildOnActivation_e(IntEnum):
    """Rebuild options during document activation."""
    swUserDecision = 0
    swDontRebuildActiveDoc = 1
    swRebuildActiveDoc = 2

    def what(self):
        return {
            0: "prompt the user whether to rebuild the activated document",
            1: "do not rebuild the activated document",
            2: "rebuild the activated document"
        }[self.value]
