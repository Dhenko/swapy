from enum import IntEnum

class swOpenDocOptions_e(IntEnum):
    """SOLIDWORKS OpenDoc options (bitmask), SolidWorks swOpenDocOptions_e (2025)"""

    swOpenDocOptions_Silent = 1
    swOpenDocOptions_ReadOnly = 2
    swOpenDocOptions_ViewOnly = 4
    swOpenDocOptions_RapidDraft = 8
    swOpenDocOptions_LoadModel = 16
    swOpenDocOptions_OverrideDefaultLoadLightweight = 64
    swOpenDocOptions_LoadLightweight = 128
    swOpenDocOptions_DontLoadHiddenComponents = 256
    swOpenDocOptions_LoadExternalReferencesInMemory = 512
    swOpenDocOptions_LDR_EditAssembly = 2048
    swOpenDocOptions_OpenDetailingMode = 1024
    swOpenDocOptions_SpeedPak = 4096
    swOpenDocOptions_AdvancedConfig = 8192

    def what(self):
        """Returns a human-readable description of this open-doc option."""
        return {
            1: "Open document silently",
            2: "Open document read-only",
            4: "Open document in Large Design Review mode only (assemblies only)",
            8: "Convert drawing to Detached format (Rapid Draft)",
            16: "Load detached model when opening a drawing",
            64: "Override default lightweight load setting",
            128: "Open assembly document as lightweight",
            256: "Do not load hidden components when opening an assembly",
            512: "Load external references in memory only",
            1024: "Open document in detailing mode",
            2048: "Open in Large Design Review mode with edit assembly enabled",
            4096: "Open document using SpeedPak option",
            8192: "Open assembly using an advanced configuration",
        }[self.value]