import smbus
bus = smbus.SMBus(1)
addr = 0x05
while(1):
    x = int(input())
    while x>0:
        j = x%256
        bus.write_byte(addr,j)
        s = int(x/256)
	bus.write_byte(addr,j)
