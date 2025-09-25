"""

"""

import win32com.client
import pythoncom
import time
from swapy.sldworks.ISldWorks import ISldWorks


def initialize_sw(Visible=1):
    pythoncom.CoInitialize()
    global swApp
    try:
        # Try to get a running instance of SolidWorks
        swApp = win32com.client.GetActiveObject("SldWorks.Application")
        print("Connected to running SolidWorks instance.")
    except Exception:
        print("No running instance found. Launching new SolidWorks...")
        swApp = win32com.client.Dispatch("SldWorks.Application")
        swApp.Visible = Visible  # Optional: make the SolidWorks window visible
        print("New SolidWorks instance launched.")
    #¶ time.sleep(20)
    sw = ISldWorks(swApp)
    return sw


def close_sw(swApp):
    try:
        swApp.ExitApp
        print("Successfully closed Solidworks")
        return True
    except Exception as e:
        print(f"Could not close Solidworks. Exception: {e}")
        return False