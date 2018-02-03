import smbus
bus = smbus.SMBus(1)
addr = 0x04
while(1):
        val = int(input())
        bus.write_byte(addr,val)
