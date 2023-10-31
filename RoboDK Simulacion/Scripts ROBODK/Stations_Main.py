def runMellingSection(ID,num):
    OnPickTarget = None
    for item in obj_list6:
        print("\nOn Curve 3")
        endTimeCurve3 = moveCurve(Conv_curved3, PART_ROTATION_ANGLE)
        if item.PoseAbs()[0,3] >= 2700: 
            item.setParentStatic(frame_conv4)
            resetCurve(Conv_curved3, PART_ROTATION_ANGLE)
        FinalTimeCurve3 = endTimeCurve3
        endTimeCurve3 = 0
        print(f"Tiempo acumulado en Curva 3: {FinalTimeCurve3} segundos")

    for item in obj_list7:
        print("\nOn Conveyor 4")
        print(item.PoseAbs()[1, 3])
        endTimeConv4, piezaPosition, OnPickTarget = MoveConveyor4(Conv_mechanism4, PART_TRAVEL_MM4, item)    
        if OnPickTarget:
            print("Estoy en el Target del Melling")
            #Station_Melling.Run(ID,num)
            time.sleep(5)
        if item.PoseAbs()[1, 3] <= 900:
            print("En curva 4!!")
            item.setParentStatic(frame_curve4)
            ResetConveyorPosition(Conv_mechanism4, 0)
  

        FinalTimeConv4 = endTimeConv4
        endTimeConv4 = 0
        print(f"Tiempo acumulado en Banda 4: {FinalTimeConv4} segundos")


def runInspectionSection(ID,num):
    for item in obj_list8:
        print("\nOn Curve 4")
        endTimeCurve4 = moveCurve(Conv_curved4, PART_ROTATION_ANGLE)
        if item.PoseAbs()[0,3] >= 1900: 
            item.setParentStatic(frame_conv1)
            resetCurve(Conv_curved4, PART_ROTATION_ANGLE)
        FinalTimeCurve4 = endTimeCurve4
        endTimeCurve4 = 0
        print(f"Tiempo acumulado en Curva 4: {FinalTimeCurve4} segundos")

    for item in obj_list1:
        print("\nOn Conveyor 1")
        endTimeConv1, piezaPosition, OnPickTarget = MoveConveyor1(Conv_mechanism1, PART_TRAVEL_MM1, item)
        if OnPickTarget:
            print("Estoy en el Target del UR3")
            # Station_Inspection.Run(ID,num)
            time.sleep(5)
        
        if piezaPosition < 0:
            item.setParentStatic(frame_curve1)
            ResetConveyorPosition(Conv_mechanism1, 0)
        FinalTimeConv1 = endTimeConv1
        endTimeConv1 = 0
        print("Time acumulado en Banda 1: ", FinalTimeConv1)

    for item in obj_list2:
        print("\nOn Curve 1")
        endTimeCurve1 = moveCurve(Conv_curved1, PART_ROTATION_ANGLE)
        
        if item.PoseAbs()[0,1] > -830:
            item.setParentStatic(frame_conv2)
            resetCurve(Conv_curved1, PART_ROTATION_ANGLE)
        FinalTimeCurve1 = endTimeCurve1
        endTimeCurve1 = 0
        print(f"Tiempo acumulado en Curva 1: {FinalTimeCurve1} segundos")
    
    for item in obj_list3:
        print("\nOn Conveyor 2")
        #print(item.PoseAbs())
        #time.sleep(40)
        endTimeConv2, piezaPosition, OnPickTarget = MoveConveyor2(Conv_mechanism2, PART_TRAVEL_MM2, item)
        if OnPickTarget:
            print("Estoy en el Target del ASRS")
            time.sleep(5)
            #Llamar Robot ASRS

#TotalTime = runLatheSection()
#print(f"Tiempo total en la sección del torno: {TotalTime} segundos")
#runMellingSection()
#runLatheSection('EP1_2023_23_10_C2_H10_T7',1,'[1,3]','piece1')