import serial
import time
import threading
#sudo chmod 666 /dev/ttyUSB0 
import sys
sys.path.insert(0, "..")
import logging

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()

c = serial.Serial('COM7', 9600,timeout=3) 
    
def SendN(N):
    S = str(N)
    S = S.encode('ascii')
    d = c.write(S)
    print(S)
    print(d)
def wait():
    c.timeout = 0.2
    c.flushInput()
    c.flushInput()
    c.flushInput()
    c.flushInput()
    c.flushInput()
    N = b''
    while N == b'':
        Recibe = c.readline()
        N = Recibe
        time.sleep(1)
    print(int(Recibe))
    c.flushInput()
    return int(Recibe)


from opcua import ua, uamethod, Server


# method to be exposed through server

def Piston(parent, Station):
    print(Station)
    StationN = Station.Value
    print(StationN)
    t = threading.Thread(target=SendN,args=(StationN,))
    t.start()
    print("Ejecutado")
    return [ua.Variant(1, ua.VariantType.Int32)]
    
def Sen(SensorEvent):
    while True:
        St = wait()
        print(St)
        if  St == 1:
            SensorEvent.event.Message = ua.LocalizedText("SENSOR: OK")
            SensorEvent.event.State = 1
            SensorEvent.trigger()
            print("trigged")
        elif St == 2:
            SensorEvent.event.Message = ua.LocalizedText("SENSOR: OK")
            SensorEvent.event.State = 2
            SensorEvent.trigger()
            print("trigged")
        elif St == 3:
            SensorEvent.event.Message = ua.LocalizedText("SENSOR: OK")
            SensorEvent.event.State = 3
            SensorEvent.trigger()
            print("trigged")
        elif St == 4:
            SensorEvent.event.Message = ua.LocalizedText("SENSOR: OK")
            SensorEvent.event.State = 4
            SensorEvent.trigger()
            print("trigged")
        elif St == 5:
            SensorEvent.event.Message = ua.LocalizedText("SENSOR: OK")
            SensorEvent.event.State = 5
            SensorEvent.trigger()
            print("trigged")
        else: 
            print("st:  "+St)


if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)

    # now setup our server
    server = Server()
    #server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    server.set_endpoint("opc.tcp://192.168.200.100:4840/ARD/")
    #server.set_endpoint("opc.tcp://172.17.6.150:4840/ARD/")
    
    server.set_server_name("Transport System Server")

    # setup our own namespace
    uri = "http://cap.edu.co"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    Services = objects.add_object(idx, "Services")
    
    Pistons = Services.add_method(idx, "Piston", Piston, [ua.VariantType.Int32],[ua.VariantType.Int32])
    
    # Creating a custom event
    Sensor_etype = server.nodes.base_event_type.add_object_type(2, 'Sensor')
    Sensor_etype.add_property(2, 'State', ua.Variant(0, ua.VariantType.Int32))

    SensorEvent = server.get_event_generator(Sensor_etype, Services)

    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        print("esperando")
        S = threading.Thread(target=Sen,args=(SensorEvent,))
        S.start()
        print("Ready")
        embed()
    finally:
        server.stop()
