#!/usr/bin/env python
  
import sys
import os
import serial
import time
from loggerinitializer import *
from crc16 import calcString


LED_E3_OFF     = "\x01\x05\x00\x02\x00\x00" 
LED_E3_ON       = "\x01\x05\x00\x02\xFF\x00"

LED_GbE_OFF   = "\x01\x05\x00\x04\x00\x00"
LED_GbE_ON     = "\x01\x05\x00\x04\xFF\x00"

LED_GPRS_OFF = "\x01\x05\x00\x05\x00\x00"
LED_GPRS_ON   = "\x01\x05\x00\x05\xFF\x00"

MODEM_OFF     = "\x01\x05\x00\x60\x00\x00"
MODEM_ON       = "\x01\x05\x00\x60\xFF\x00"





# Decimal to Hex.
def dec2hex(n):
    lo = n & 0x00FF
    hi = (n & 0xFF00) >> 8
    return chr(hi) + chr(lo)
    
# Hex. to Decimal
def hex2dec(s):
    return int(s, 16)

# Invert byte ( LO and HI )
def swapLoHi(n):
    lo = n & 0x00FF
    hi = (n & 0xFF00) >> 8
    return  lo << 8 | hi

# Calc. CRC16
def stCRC(msg):
    crc = calcString(msg, 0xFFFF)
    crc = swapLoHi(crc)
    return dec2hex(crc)
    
def HiLo(n):
    lo = n & 0x00FF
    hi = (n & 0xFF00) >> 8
    return  hi | lo





  
  
   
 
def LED_E3(state):
               try:
                              time.sleep(0.1)
                              ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                             
                              #logging.debug("[LED_E3] %s" %ser )                             
                              if state:
                                             PresetSingle = LED_E3_ON + stCRC(LED_E3_ON)
                              else:
                                             PresetSingle = LED_E3_OFF + stCRC(LED_E3_OFF)
                                             
                              ser.write (PresetSingle)
                              time.sleep(0.2)
                              ser.close()
               except:
                              try:
                                             time.sleep(0.2)
                                             ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                                             
                                             #logging.debug("[LED_E3] %s" %ser )                                            
                                             if state:
                                                            PresetSingle = LED_E3_ON + stCRC(LED_E3_ON)
                                             else:
                                                            PresetSingle = LED_E3_OFF + stCRC(LED_E3_OFF)
                                                            
                                             ser.write (PresetSingle)
                                             time.sleep(0.2)
                                             ser.close()
                              except  Exception, e:
                                             logging.error("[LED_E3  ERROR]  ERROR ---> %s !!!" %str(e)) 










def LED_GbE(state):
               try:
                              time.sleep(0.1)
                              ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                             
                              #logging.debug("[LED_GbE] %s" %ser )                              
                              if state:
                                             PresetSingle = LED_GbE_ON + stCRC(LED_GbE_ON)
                              else:
                                             PresetSingle = LED_GbE_OFF + stCRC(LED_GbE_OFF)
                                             
                              ser.write (PresetSingle)
                              time.sleep(0.2)
                              ser.close()
               except:
                              try:
                                             time.sleep(0.2)
                                             ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                                             
                                             #logging.debug("[LED_GbE] %s" %ser )                                             
                                             if state:
                                                            PresetSingle = LED_GbE_ON + stCRC(LED_GbE_ON)
                                             else:
                                                            PresetSingle = LED_GbE_OFF + stCRC(LED_GbE_OFF)
                                                            
                                             ser.write (PresetSingle)
                                             time.sleep(0.2)
                                             ser.close()
                              except  Exception, e:
                                             logging.error("[LED_GbE  ERROR]  ERROR ---> %s !!!" %str(e))











def LED_GPRS(state):
               try:
                              time.sleep(0.1)
                              ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                              
                              #logging.debug("[LED_GPRS] %s" %ser )                              
                              if state:
                                             PresetSingle = LED_GPRS_ON + stCRC(LED_GPRS_ON)
                              else:
                                             PresetSingle = LED_GPRS_OFF + stCRC(LED_GPRS_OFF)
                                             
                              ser.write (PresetSingle)
                              time.sleep(0.2)
                              ser.close()
               except:
                              try:
                                             time.sleep(0.2)
                                             ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                                             
                                             #logging.debug("[LED_GPRS] %s" %ser )                                             
                                             if state:
                                                            PresetSingle = LED_GPRS_ON + stCRC(LED_GPRS_ON)
                                             else:
                                                            PresetSingle = LED_GPRS_OFF + stCRC(LED_GPRS_OFF)
                                                            
                                             ser.write (PresetSingle)
                                             time.sleep(0.2)
                                             ser.close()
                              except  Exception, e:
                                             logging.error("[LED_GPRS ERROR] ERROR ---> %s !!!" %str(e))












def MODEM_POWER(state):
               try:
                              time.sleep(0.1)
                              ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                             
                              #logging.debug("[LED_MODEM_POWER] %s" %ser )                             
                              if state:
                                             PresetSingle = MODEM_ON + stCRC(MODEM_ON)
                              else:
                                             PresetSingle = MODEM_OFF + stCRC(MODEM_OFF)
                                             
                              ser.write (PresetSingle)
                              time.sleep(0.2)
                              ser.close()
               except:
                              try:
                                             time.sleep(0.2)
                                             ser = serial.Serial(port='/dev/pic',baudrate=115200, timeout=1)                                             
                                             #logging.debug("[LED_MODEM_POWER] %s" %ser )                                             
                                             if state:
                                                            PresetSingle = MODEM_ON + stCRC(MODEM_ON)
                                             else:
                                                            PresetSingle = MODEM_OFF + stCRC(MODEM_OFF)
                                                            
                                             ser.write (PresetSingle)
                                             time.sleep(0.2)
                                             ser.close()
                              except Exception, e:
                                             logging.error("[MODEM_POWERRESET  ERROR] ERROR ---> %s !!!" %str(e))









def LEDS_OFF():
               try:
                              LED_E3(False)
                              LED_GbE(False)
                              LED_GPRS(False)
               except Exception, e:
                              logging.error("[LEDS_OFF ERROR]  ERROR ---> %s" %str(e))   
    




#LED_GPRS(True)
#LED_GbE(True)
#LED_E3(True)
#time.sleep(3)
#LEDS_OFF()

