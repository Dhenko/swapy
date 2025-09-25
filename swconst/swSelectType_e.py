from enum import IntEnum


class swSelectType_e(IntEnum):
    """Selection types for SOLIDWORKS objects (subset starting at swSelANNOTATIONTABLES)."""

    swSelANNOTATIONTABLES = 98
    swSelANNOTATIONVIEW = 139
    swSelARROWS = 49
    swSelATTRIBUTES = 8
    swSelBLOCKDEF = 99
    swSelBLOCKINST = 93
    swSelBODYFEATURES = 22
    swSelBODYFOLDER = 118
    swSelBOMFEATURES = 97
    swSelBOMS = 54
    swSelBOMTEMPS = 64
    swSelBorder = 254
    swSelBREAKLINES = 31
    swSelBROWSERITEM = 69
    swSelCAMERAS = 136
    swSelCENTERLINES = 103
    swSelCENTERMARKS = 28
    swSelCENTERMARKSYMS = 100
    swSelCOMMENT = 127
    swSelCOMMENTSFOLDER = 126
    swSelCOMPONENTS = 20
    swSelCOMPPATTERN = 37
    swSelCOMPSDONTOVERRIDE = 72
    swSelCONFIGURATIONS = 47
    swSelCONNECTIONPOINTS = 66
    swSelCOORDSYS = 61
    swSelCOSMETICWELDS = 220
    swSelCTHREADS = 39
    swSelCUSTOMSYMBOLS = 60
    swSelDATUMAXES = 5
    swSelDATUMLINES = 62
    swSelDATUMPLANES = 4
    swSelDATUMPOINTS = 6
    swSelDATUMTAGS = 36
    swSelDCABINETS = 42
    swSelDETAILCIRCLES = 17
    swSelDIMENSIONS = 14
    swSelDISPLAYSTATE = 148
    swSelDOCSFOLDER = 125
    swSelDOWELSYMS = 86
    swSelDRAWINGVIEWS = 12
    swSelDTMTARGS = 40
    swSelEDGES = 1
    swSelEMBEDLINKDOC = 123
    swSelEMPTYSPACE = 72
    swSelEQNFOLDER = 55
    swSelEVERYTHING = -3
    swSelEXCLUDEMANIPULATORS = 111
    swSelEXPLLINES = 45
    swSelEXPLSTEPS = 44
    swSelEXPLVIEWS = 43
    swSelEXTSKETCHPOINTS = 25
    swSelEXTSKETCHSEGS = 24
    swSelEXTSKETCHTEXT = 88
    swSelFABRICATEDROUTE = 70
    swSelFACES = 2
    swSelFRAMEPOINT = 77
    swSelFTRFOLDER = 94
    swSelGENERALTABLEFEAT = 142
    swSelGTOLS = 13
    swSelHELIX = 26
    swSelHOLESERIES = 83
    swSelHOLETABLEAXES = 105
    swSelHOLETABLEFEATS = 104
    swSelIMPORTFOLDER = 57
    swSelINCONTEXTFEAT = 29
    swSelINCONTEXTFEATS = 32
    swSelJOURNAL = 124
    swSelLEADERS = 84
    swSelLIGHTS = 73
    swSelLOCATIONS = -2
    SwSelMAGNETICLINES = 225
    swSelMANIPULATORS = 79
    swSelMATEGROUP = 30
    swSelMATEGROUPS = 33
    swSelMATES = 21
    swSelMATESUPPLEMENT = 138
    swSelMIDPOINTS = 59
    swSelNOTES = 15
    swSelNOTHING = 0
    swSelOBJGROUP = 155
    swSelOBJHANDLES = 48
    swSelOLEITEMS = 7
    swSelPICTUREBODIES = 80
    swSelPLANESECTIONS = 219
    swSelPOINTREFS = 41
    swSelPOSGROUP = 68
    swSelPUNCHTABLEFEATS = 234
    swSelREFCURVES = 23
    swSelREFEDGES = 51
    swSelREFERENCECURVES = 26
    swSelREFFACES = 52
    swSelREFSILHOUETTE = 53
    swSelREFSURFACES = 27
    swSelREVISIONCLOUDS = 240
    swSelREVISIONTABLE = 113
    swSelREVISIONTABLEFEAT = 119
    swSelROUTECURVES = 63
    swSelROUTEPOINTS = 65
    swSelROUTESWEEPS = 67
    swSelSECTIONLINES = 16
    swSelSECTIONTEXT = 18
    swSelSELECTIONSETFOLDER = 258
    swSelSELECTIONSETNODE = 259
    swSelSFSYMBOLS = 35
    swSelSHEETS = 19
    swSelSILHOUETTES = 46
    swSelSIMELEMENT = 102
    swSelSIMULATION = 101
    swSelSKETCHBITMAP = 85
    swSelSKETCHCONTOUR = 96
    swSelSKETCHES = 9
    swSelSKETCHHATCH = 56
    swSelSKETCHPOINTFEAT = 71
    swSelSKETCHPOINTS = 11
    swSelSKETCHREGION = 95
    swSelSKETCHSEGS = 10
    swSelSKETCHTEXT = 34
    swSelSOLIDBODIES = 76
    swSelSOLIDBODIESFIRST = 81
    swSelSUBATOMFOLDER = 121
    swSelSUBSKETCHDEF = 154
    swSelSUBSKETCHINST = 114
    swSelSUBWELDFOLDER = 107
    swSelSURFACEBODIES = 75
    swSelSURFBODIESFIRST = 78
    swSelSWIFTANNOTATIONS = 130
    swSelSWIFTFEATURES = 132
    swSelSWIFTSCHEMA = 159
    swSelTITLEBLOCK = 192
    swSelTITLEBLOCKTABLEFEAT = 206
    swSelUNSUPPORTED = -1
    swSelVERTICES = 3
    swSelVIEWERHYPERLINK = 58
    swSelWELDBEADS = 122
    swSelWELDMENT = 106
    swSelWELDMENTTABLEFEATS = 116
    swSelWELDS = 38
    swSelWIREBODIES = 74
    swSelZONES = 50

    def what(self):
        return {
            98: "Annotation tables",
            139: "Annotation view",
            49: "Arrows",
            8: "Attributes",
            99: "Block definition",
            93: "Block instance",
            22: "Body features",
            118: "Body folder",
            97: "BOM features",
            54: "BOMs",
            64: "Temporary BOMs",
            254: "Drawing border",
            31: "Break lines",
            69: "Browser item",
            136: "Cameras",
            103: "Centerlines",
            28: "Center marks",
            100: "Center mark symbols",
            127: "Comment",
            126: "Comments folder",
            20: "Components",
            37: "Component pattern",
            72: "Components that don't override",
            47: "Configurations",
            66: "Connection points",
            61: "Coordinate systems",
            220: "Cosmetic welds",
            39: "Cosmetic threads",
            60: "Custom symbols",
            5: "Datum axes",
            62: "Datum lines",
            4: "Datum planes",
            6: "Datum points",
            36: "Datum tags",
            42: "Design check cabinets",
            17: "Detail circles",
            14: "Dimensions",
            148: "Display states",
            125: "Documents folder",
            86: "Dowel symbols",
            12: "Drawing views",
            40: "Datum target symbols",
            1: "Edges",
            123: "Embedded link document",
            72: "Empty space",
            55: "Equation folder",
            -3: "Everything",
            111: "Exclude manipulators",
            45: "Exploded view lines",
            44: "Exploded steps",
            43: "Exploded views",
            25: "External sketch points",
            24: "External sketch segments",
            88: "External sketch text",
            70: "Fabricated route",
            2: "Faces",
            77: "Frame point",
            94: "Feature folder",
            142: "General table feature",
            13: "Geometric tolerances",
            26: "Helix/spiral",
            83: "Hole series",
            105: "Hole table axes",
            104: "Hole table features",
            57: "Import folder",
            29: "In-context feature",
            32: "In-context features",
            124: "Journal",
            84: "Leaders",
            73: "Lights",
            -2: "Locations",
            225: "Magnetic lines",
            79: "Manipulators",
            30: "Mate group",
            33: "Mate groups",
            21: "Mates",
            138: "Mate supplement",
            59: "Midpoints",
            15: "Notes",
            0: "Nothing",
            155: "Object group",
            48: "Object handles",
            7: "OLE objects",
            80: "Picture bodies",
            219: "Plane sections",
            41: "Point references",
            68: "Position group",
            234: "Punch table features",
            23: "Reference curves",
            51: "Reference edges",
            26: "Reference curves (duplicate value)",
            52: "Reference faces",
            53: "Reference silhouette",
            27: "Reference surfaces",
            240: "Revision clouds",
            113: "Revision table",
            119: "Revision table feature",
            63: "Route curves",
            65: "Route points",
            67: "Route sweeps",
            16: "Section lines",
            18: "Section text",
            258: "Selection set folder",
            259: "Selection set node",
            35: "Surface finish symbols",
            19: "Sheets",
            46: "Silhouettes",
            102: "Simulation element",
            101: "Simulation feature",
            85: "Sketch bitmap",
            96: "Sketch contour",
            9: "Sketches",
            56: "Sketch hatch",
            71: "Sketch point feature",
            11: "Sketch points",
            95: "Sketch region",
            10: "Sketch segments",
            34: "Sketch text",
            76: "Solid bodies",
            81: "First solid body",
            121: "Sub-atom folder",
            154: "Sub-sketch definition",
            114: "Sub-sketch instance",
            107: "Sub-weld folder",
            75: "Surface bodies",
            78: "First surface body",
            130: "SWIFT annotations",
            132: "SWIFT features",
            159: "SWIFT schema",
            192: "Title block",
            206: "Title block table feature",
            -1: "Unsupported",
            3: "Vertices",
            58: "Viewer hyperlink",
            122: "Weld beads",
            106: "Weldment feature",
            116: "Weldment table features",
            38: "Welds",
            74: "Wire bodies",
            50: "Zones",
        }[self.value]