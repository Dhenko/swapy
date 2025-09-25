"""
Wrapper for ISketchSegment in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html

Provides access to functions that are common among sketch entities.
"""


class ISketchSegment:
    def __init__(self, comm_object):
        """
        A SketchSegment can represent a sketch arc, line, ellipse, parabola or spline.\n

        ISketchSegment provides functions that are generic to every type of sketch segment. For example, every sketch
        segment has an ID and can be programmatically selected
        :param comm_object: COM object representing ISketchSegment instance from Solidworks API
        """
        self.__comm_object = comm_object
        self.Color = self.__comm_object.Color
        self.ConstructionGeometry = self.__comm_object.ConstructionGeometry
        self.Layer = self.__comm_object.Layer
        self.LayerOevrride = self.__comm_object.LayerOverride
        self.Status = self.__comm_object.Status
        self.Style = self.__comm_object.Style
        self.Width = self.__comm_object.Width

    def GetID(self):
        """
        Gets the for this sketch segment.
        :return: Array with two longs or integers (see Long vs. Integer) identifying this sketch segment ID
        """
        return self.__comm_object.GetID

    def GetName(self):
        """
        Gets the name of this sketch segment.
        :return: Sketch segment name
        """
        return self.__comm_object.GetName
