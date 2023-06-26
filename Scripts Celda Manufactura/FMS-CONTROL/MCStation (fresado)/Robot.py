# -*- coding: utf-8 -*-
import serial
import time
#sudo chmod 666 /dev/ttyS0 


class execute:
    """
    Esta clase se encarga de enviar los comandos al robot para que sean ejecutados inmediatamente
    """
    def __init__(self, port ='\\.\COM1', baudrate=9600, parity="O", bytesize=7, stopbits=2,xonxoff = False):
         self.po = port
         self.br = baudrate
         self.pa = parity
         self.bs = bytesize
         self.sb = stopbits
         self.nf = xonxoff
         self.c = serial.Serial(port = self.po, baudrate=self.br,stopbits=self.sb,parity=self.pa,bytesize=self.bs,xonxoff=self.nf,timeout=30)
         
    def tx(self, s):
        #enviar texto TX
        #codificar string y mandar por puerto serial
        data = str.encode(s)+b"\n"
        self.c.write(data)
        print(data)
    
    def txl(self, a):
        #enviar texto largo TXL
    #esta funcion agrega los que haga falta para que el texto este con el formato correcto antes de enviar.
        r = len(a)
        for i in range(r):
            if i == 0:
                data = a[i] + " "
            elif i == (r-1):
                if isinstance(a[i], float):
                    if a[i]>0:
                        data = data + "+"+str(a[i])
                    else:
                        data = data+str(a[i]) 
                else:                           
                    data = data + str(a[i])
            else:
                if isinstance(a[i], float):
                    if a[i]>0:
                        data = data + "+"+str(a[i])+ ", "
                    else:
                        data = data+str(a[i])+ ", " 
                else:                           
                    data = data + str(a[i])+ ", "
        self.tx(data)
        
    
    def DP(self):
        """
        Decrement Position
        Movest he robot to a predefine position with a position numbers smaller than the current one.
        """
        self.tx("DP")
    
    def DW(self,x,y,z):
        """
        Draw
        """
        data = ["DW",x,y,z]
        self.txl(data)
        
    def HE(self, PositionNumber):
        """
        Here
        Definets the coordinates of the current position by assigning a positionn number to it
        """
        data = ["HE",PositionNumber]
        self.txl(data)
        
    def HO(self):
        """
        Home
        reference posotion in the cartesioan coordenate system
        """
        self.tx("HO")
        
    def IP(self):
        """
        Increment Position
        """
        self.tx("IP")
        
    def MA(self, Pa, Pb, OC):
        """
        Move Approach
        """
        data = ["MA",Pa, Pb, OC]
        self.txl(data)
        
    def MC(self, Pa, Pb):
        """
        Move continuous
        """
        data = ["MC",Pa, Pb]
        self.txl(data)
        
    def MJ(self, a1, a2, a3, a4, a5):
        """
        Move Joint
        """
        data = ["MJ", a1, a2, a3, a4, a5]
        self.txl(data)
    
    def MO(self, Position, OC):
        """
        Move 
        """
        data = ["MO",Position, OC]
        self.txl(data)
     
    def MP(self, x,y,z,p,r):
        """
        Move Position 
        """
        data = ["MP",x,y,z,p,r]
        self.txl(data)
        
    def MS(self, Position,points,OC):
        """
        Move Straight
        """
        data = ["MS",Position,points,OC]
        self.txl(data)
    
    def MT(self, Position,distance,OC):
        """
        Move Tool
        """
        data = ["MT",Position,distance,OC]
        self.txl(data)
        
    def NT(self):
        """
        Nest
        """
        self.tx("NT")
        
    def OG(self):
        """
        Origin
        """
        self.tx("OG")
        
    def PA(self, Pallet,Colums,Grid):
        """
        Pallet Assign
        """
        data = ["PA", Pallet,Colums,Grid]
        self.txl(data)
        
    def PC(self, Position1,Position2):
        """
        Position Clear
        """
        data = ["PC",Position1,Position2]
        self.txl(data)
        
    def PD(self, Position,x,y,z,p,r):
        """
        Position Define
        """
        data = ["PD",Position,x,y,z,p,r]
        self.txl(data)
      
    def PL(self, Position1,Position2):
        """
        Position Load
        """
        data = ["PL",Position1,Position2]
        self.txl(data)
    
    def PT(self, Pallet):
        """
        Position Load
        """
        data = ["PT",Pallet]
        self.txl(data)
        
    def PX(self, Position1,Position2):
        """
        Position Load
        """
        data = ["PX",Position1,Position2]
        self.txl(data)
        
    def SF(self, Position1,Position2):
        """
        Shift
        """
        data = ["SF",Position1,Position2]
        self.txl(data)
        
    def SP(self, Speed, acel):
        """
        Speed
        """
        data = ["SP",Speed, acel]
        self.txl(data)
        
    def TI(self, Time):
        """
        time delay
        """
        data = ["TI",Time]
        self.txl(data)
        
    def TL(self, ToolLength):
        """
        Tool Length
        """
        data = ["TL",ToolLength]
        self.txl(data)
        
    def CP(self, Counter):
        """
        compare counter
        """
        data = ["CP",Counter]
        self.txl(data)
        
    def DA(self, Bit):
        """
        Disable act
        """
        data = ["DA",Bit]
        self.txl(data)
        
    def DC(self, Bit):
        """
        decrement counter
        """
        data = ["DC",Bit]
        self.txl(data)
        
    def DL(self, Line1, Line2):
        """
        Delete Line
        """
        data = ["DL",Line1, Line2]
        self.txl(data)
        
    def EA(self, Bit, line):
        """
        Enable Act
        """
        data = ["EA",Bit, line]
        self.txl(data)
        
    def ED(self):
        """
        Go Sub
        """
        self.tx("ED")
        
    def GT(self, line):
        """
        Go to 
        """
        data = ["GT",line]
        self.txl(data)
        
    def IC(self, Counter):
        """
        Increment Counter
        """
        data = ["IC",Counter]
        self.txl(data)
        
    def NW(self):
        """
        New Borrar todo !!!
        """
        self.tx("NW")
        
    def NX(self):
        """
        Next
        """
        self.tx("NX")
        
    def RC(self, No):
        """
        Repeat Cycle
        """
        data = ["RC",No]
        self.txl(data)
        
    def RN(self, Line1, Line2):
        """
        Run
        """
        data = ["RN",Line1, Line2]
        self.txl(data)
        
    def RT(self):
        """
        Return
        """
        self.tx("RT")
        
    def SC(self, Counter, Value):
        """
        Set Counter
        """
        data = ["SC",Counter, Value]
        self.txl(data)
        
    def GC(self):
        """
        Grip Close
        """
        self.tx("GC")
        
    def GF(self, Switch):
        """
        Grip Flag
        """
        data = ["GF",Switch]
        self.txl(data)
        
    def GO(self):
        """
        Grip open
        """
        self.tx("GO")
        
    def GP(self, Starting, Retained, Time):
        """
        Grip Pressure
        """
        data = ["GP",Starting, Retained, Time]
        self.txl(data)
        
    def ID(self):
        """
        input direct
        """
        self.tx("ID")
        
    def IN(self):
        """
        input
        """
        self.tx("IN")
        
    def OT(self):
        """
        output
        """
        self.tx("OT")
        
    def CR(self, Counter):
        """
        Counter Read
        """
        data = ["CR",Counter]
        self.txl(data)
        
    def DR(self):
        """
        Data read
        """
        self.tx("DR")
        
    def ER(self):
        """
        Error Read
        """
        self.tx("ER")
        
    def LR(self, Line):
        """
        Line read
        """
        data = ["LR",Line]
        self.txl(data)
        
    def PR(self, Position):
        """
        Position Read
        """
        data = ["PR",Position]
        self.txl(data)
        
    def WH(self):
        """
        Where
        """
        self.tx("WH")
        
    def RS(self):
        """
        Reset
        """
        self.tx("RS")
        
    def TR(self):
        """
        Transfer
        """
        self.tx("TR")
        
    def WR(self):
        """
        Write
        """
        self.tx("WR")
        
    def Join(self,c,a):
        if c == "W":
            self.MJ(a,0,0,0,0)
        elif c == "S":
            self.MJ(0,a,0,0,0)
        elif c == "E":
            self.MJ(0,0,a,0,0)
        elif c == "P":
            self.MJ(0,0,0,a,0)
        elif c == "R":
            self.MJ(0,0,0,0,a)
            
    def send(self, filename,s):
        f = open(filename, "rb")
        for i in f:
            self.tx(i)
            print (i)
            time.sleep(s)
            
    def Axis(self,c,d):
        """pendiente """       
        if c == "X":
            self.MJ(d,0,0,0,0)
        elif c == "Y":
            self.MJ(0,d,0,0,0)
        elif c == "Z":
            self.MJ(0,0,d,0,0)
            
    def _readline(self):
        eol = b'\r'
        line = b"Pos: "
        print(line)
        while True:
            c1 = self.c.read(1)
            if c1 == eol:
                break
            else:
                line = line + c1
        return line
        
    def read(self):
        line = self._readline()
        print (line)
        return line
        

class program:
    """
    Esta clase se encarga de enviar los comandos pero precedidos de el numero de linea, por lo cual solo pueden ser ejecutados con el
    comando Robot.execute.RN
    """
    def __init__(self, port ='\\.\COM1', baudrate=9600, parity="O", bytesize=7, stopbits=2,xonxoff = False):
         self.po = port
         self.br = baudrate
         self.pa = parity
         self.bs = bytesize
         self.sb = stopbits
         self.nf = xonxoff
         self.c = serial.Serial(port = self.po, baudrate=self.br,stopbits=self.sb,parity=self.pa,bytesize=self.bs,xonxoff=self.nf)
         
    def tx(self, n, s):
        #codificar string y mandar por puerto serial
        data = str.encode(str(n)+" ")+str.encode(s)+b"\n"
        self.c.write(data)
        print(data)
        time.sleep(0.1)
    
    def txl(self,n, a):
        r = len(a)
        for i in range(r):
            if i == 0:
                data = a[i] + " "
            elif i == (r-1):
                if isinstance(a[i], float):
                    if a[i]>0:
                        data = data + "+"+str(a[i])
                    else:
                        data = data+str(a[i]) 
                else:                           
                    data = data + str(a[i])
            else:
                if isinstance(a[i], float):
                    if a[i]>0:
                        data = data + "+"+str(a[i])+ ", "
                    else:
                        data = data+str(a[i])+ ", " 
                else:                           
                    data = data + str(a[i])+ ", "
        self.tx(n,data)
        
    
    def DP(self):
        """
        Decrement Position
        Movest he robot to a predefine position with a position numbers smaller than the current one.
        """
        self.tx("DP")
    
    def DW(self,x,y,z):
        """
        Draw
        """
        data = ["DW",x,y,z]
        self.txl(data)
        
    def HE(self, PositionNumber):
        """
        Here
        Definets the coordinates of the current position by assigning a positionn number to it
        """
        data = ["HE",PositionNumber]
        self.txl(data)
        
    def HO(self):
        """
        Home
        reference posotion in the cartesioan coordenate system
        """
        self.tx("HO")
        
    def IP(self):
        """
        Increment Position
        """
        self.tx("IP")
        
    def MA(self,n, Pa, Pb, OC):
        """
        Move Approach
        """
        data = ["MA",Pa, Pb, OC]
        self.txl(n,data)
        
    def MC(self, Pa, Pb):
        """
        Move continuous
        """
        data = ["MC",Pa, Pb]
        self.txl(data)
        
    def MJ(self, a1, a2, a3, a4, a5):
        """
        Move Joint
        """
        data = ["MJ", a1, a2, a3, a4, a5]
        self.txl(data)
    
    def MO(self, n,Position, OC):
        """
        Move 
        """
        data = ["MO",Position, OC]
        self.txl(n,data)
     
    def MP(self, x,y,z,p,r):
        """
        Move Position 
        """
        data = ["MP",x,y,z,p,r]
        self.txl(data)
        
    def MS(self,n, Position,points,OC):
        """
        Move Straight
        """
        data = ["MS",Position,points,OC]
        self.txl(n,data)
    
    def MT(self, Position,distance,OC):
        """
        Move Tool
        """
        data = ["MT",Position,distance,OC]
        self.txl(data)
        
    def NT(self,n):
        """
        Nest
        """
        self.tx(n,"NT")
        
    def OG(self):
        """
        Origin
        """
        self.tx("OG")
        
    def PA(self, Pallet,Colums,Grid):
        """
        Pallet Assign
        """
        data = ["PA", Pallet,Colums,Grid]
        self.txl(data)
        
    def PC(self, Position1,Position2):
        """
        Position Clear
        """
        data = ["PC",Position1,Position2]
        self.txl(data)
        
    def PD(self, Position,x,y,z,p,r):
        """
        Position Define
        """
        data = ["PD",Position,x,y,z,p,r]
        self.txl(data)
      
    def PL(self, Position1,Position2):
        """
        Position Load
        """
        data = ["PL",Position1,Position2]
        self.txl(data)
    
    def PT(self, Pallet):
        """
        Position Load
        """
        data = ["PT",Pallet]
        self.txl(data)
        
    def PX(self, Position1,Position2):
        """
        Position Load
        """
        data = ["PX",Position1,Position2]
        self.txl(data)
        
    def SF(self, Position1,Position2):
        """
        Shift
        """
        data = ["SF",Position1,Position2]
        self.txl(data)
        
    def SP(self, n, Speed, acel):
        """
        Speed
        """
        data = ["SP",Speed, acel]
        self.txl(n, data)
        
    def TI(self, n, Time):
        """
        time delay
        """
        data = ["TI",Time]
        self.txl(n,data)
        
    def TL(self, ToolLength):
        """
        Tool Length
        """
        data = ["TL",ToolLength]
        self.txl(data)
        
    def CP(self, Counter):
        """
        compare counter
        """
        data = ["CP",Counter]
        self.txl(data)
        
    def DA(self, Bit):
        """
        Disable act
        """
        data = ["DA",Bit]
        self.txl(data)
        
    def DC(self, Bit):
        """
        decrement counter
        """
        data = ["DC",Bit]
        self.txl(data)
        
    def DL(self, Line1, Line2):
        """
        Delete Line
        """
        data = ["DL",Line1, Line2]
        self.txl(data)
        
    def EA(self, Bit, line):
        """
        Enable Act
        """
        data = ["EA",Bit, line]
        self.txl(data)
        
    def ED(self):
        """
        Go Sub
        """
        self.tx("ED")
        
    def GT(self, line):
        """
        Go to 
        """
        data = ["GT",line]
        self.txl(data)
        
    def IC(self, Counter):
        """
        Increment Counter
        """
        data = ["IC",Counter]
        self.txl(data)
        
    def NW(self):
        """
        New Borrar todo !!!
        """
        self.tx("NW")
        
    def NX(self):
        """
        Next
        """
        self.tx("NX")
        
    def RC(self, No):
        """
        Repeat Cycle
        """
        data = ["RC",No]
        self.txl(data)
        
    def RN(self, Line1, Line2):
        """
        Run
        """
        data = ["RN",Line1, Line2]
        self.txl(data)
        
    def RT(self):
        """
        Return
        """
        self.tx("RT")
        
    def SC(self, Counter, Value):
        """
        Set Counter
        """
        data = ["SC",Counter, Value]
        self.txl(data)
        
    def GC(self,n):
        """
        Grip Close
        """
        self.tx(n,"GC")
        
    def GF(self, Switch):
        """
        Grip Flag
        """
        data = ["GF",Switch]
        self.txl(data)
        
    def GO(self,n):
        """
        Grip open
        """
        self.tx(n,"GO")
        
    def GP(self, Starting, Retained, Time):
        """
        Grip Pressure
        """
        data = ["GP",Starting, Retained, Time]
        self.txl(data)
        
    def ID(self):
        """
        input direct
        """
        self.tx("ID")
        
    def IN(self):
        """
        input
        """
        self.tx("IN")
        
    def OT(self):
        """
        output
        """
        self.tx("OT")
        
    def CR(self, Counter):
        """
        Counter Read
        """
        data = ["CR",Counter]
        self.txl(data)
        
    def DR(self):
        """
        Data read
        """
        self.tx("DR")
        
    def ER(self):
        """
        Error Read
        """
        self.tx("ER")
        
    def LR(self, Line):
        """
        Line read
        """
        data = ["LR",Line]
        self.txl(data)
        
    def PR(self, Position):
        """
        Position Read
        """
        data = ["RN",Position]
        self.txl(data)
        
    def WH(self,n):
        """
        Where
        """
        self.tx(n,"WH")
        
    def RS(self):
        """
        Reset
        """
        self.tx("RS")
        
    def TR(self):
        """
        Transfer
        """
        self.tx("TR")
        
    def WR(self):
        """
        Write
        """
        self.tx("WR")
        
    def Join(self,c,a):
        if c == "W":
            self.MJ(a,0,0,0,0)
        elif c == "S":
            self.MJ(0,a,0,0,0)
        elif c == "E":
            self.MJ(0,0,a,0,0)
        elif c == "P":
            self.MJ(0,0,0,a,0)
        elif c == "R":
            self.MJ(0,0,0,0,a)
            
    def send(self, filename,s):
        f = open(filename, "rb")
        for i in f:
            self.tx(i)
            print (i)
            time.sleep(s)
            
    def Axis(self,c,d):
        """pendiente """       
        if c == "X":
            self.MJ(d,0,0,0,0)
        elif c == "Y":
            self.MJ(0,d,0,0,0)
        elif c == "Z":
            self.MJ(0,0,d,0,0)
    """
    def read(self,b):
        self.WR()
        line = self.c.read(b)
        print (line)
    """
        
    
    
    
        
    
    
           
    
        
    
    
        