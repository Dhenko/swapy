"""
Wrapper for ISketch in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html

Allows access to sketch entities and to extract information about sketch elements, the sketch orientation, and so on.
"""


from swapy.sldworks.IFeature import IFeature


class ISketch(IFeature):
    def __init__(self, comm_object):
        """
        Creates an instance of the ISketch wrapper from the Solidworks API
        :param comm_object: COM object representing ISketch instance from Solidworks API\n
        """
        super().__init__(comm_object)
        self.__comm_object = comm_object
        pass
