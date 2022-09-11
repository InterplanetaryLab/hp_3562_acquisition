import os.path
import serial
import sys

class data_3562A:
    def __init__(self, header_list):
        self.header = {
                "delta_x": str(header_list[56])
                }

if __name__ == '__main__':

    comport = '/dev/ttyUSB1'
    addr = 20

    ser = serial.Serial()

    ser = serial.Serial(comport, 9600, timeout=0.5 )

    cmd = str.encode('++mode 1'+'\n','utf-8')
    print( 'Sending:', cmd)
    ser.write(cmd)
    s = ser.read(256);
    if len(s) > 0:
        print (s)

    cmd = str.encode('++addr '+str(addr)+'\n','utf-8')
    print( 'Sending:', cmd)
    ser.write(cmd)
    s = ser.read(256);
    if len(s) > 0:
        print (s)

    cmd = str.encode('++auto 1'+'\n','utf-8')
    print( 'Sending:', cmd)
    ser.write(cmd)
    s = ser.read(256);
    if len(s) > 0:
        print (s)

    cmd = str.encode('DDAS'+'\n','utf-8')
    print( 'Sending:', cmd)
    ser.write(cmd)
    f = open("baud150neg10dB.txt", "wb")
    s = ""
    while (1):
        s = ser.read(20000);
        if len(s) > 0:
            f.write(s)
            print (s)
        else:
            break
    f.close()
    vals = s.split(b'\r\n')
    print(vals)
    print("len: %d" %len(vals))
    #header = data_3562A(vals)
    #print(header.header["delta_x"])
