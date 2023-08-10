from robodk import robolink
from datetime import datetime

class Simulation:
    def __init__(self):
        self.RDK= robolink.Robolink()


    def Station_Lathe(self):
        RDK = self.RDK


    def Station_Melling(self):
        RDK = self.RDK


    def Station_Inspection(self):
        RDK = self.RDK


    def Conveyors(self,number):
        RDK = self.RDK

        #Set the travel of the conveyors for each iterations
        PART_ROTATION_ANGLE = -30

        #Declaration of the conveyor object
        Conv_curved = RDK.Item('Curved_Conv_Mech',itemtype=ITEM_TYPE_ROBOT)

        #setSpeed(speed_linear, speed_joints, accel_linear, accel_joints), 
        #Must adjust to match the linear conveyors speed
        Conv_curved.setSpeed(7,7,7,7)

        #If the conveyor exist, move it to the declared value.
        if Conv_curved.Valid():
            Conv_curved.MoveJ(Conv_curved.Joints() + PART_ROTATION_ANGLE)


    def Create_Material(self,Location,Type):
        RDK = self.RDK
        #----- Constante -----
        NEW_REF_OBJECT_NAME = 'BoxRef_12X10'
        NEW_OBJECT_NAME = 'Box_12X10'
        REFERENCE_FRAME = 'Conveyor Box'
        REFERENCE_FRAME_REF = 'New_Box 12X10'


        #------- Program ------
        frame = RDK.Item(REFERENCE_FRAME, robolink.ITEM_TYPE_FRAME)
        frame_ref = RDK.Item(REFERENCE_FRAME_REF, robolink.ITEM_TYPE_FRAME)
        ref_obj = RDK.Item(NEW_REF_OBJECT_NAME, robolink.ITEM_TYPE_OBJECT)

        if frame.Valid() and  ref_obj.Valid():
            ref_obj.Copy()
            new_obj = RDK.Paste()
            new_obj.setVisible(False)
            new_obj.setName(NEW_OBJECT_NAME)
            new_obj.setParent(frame_ref)
            new_obj.setParentStatic(frame)
            new_obj.setVisible(True)

            
    def Clear(self):
        RDK = self.RDK