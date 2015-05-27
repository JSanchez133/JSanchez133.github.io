from gopigo import *

def turn_right:
  enc_tgt(1,0,15)
  right()

while 1>0:
  while us_dist(15) > 20:
    fwd()
  stop()
  turn_right()
