from create_status import createStatus

def SRARQ(windowSize=3, probOfNACK=0.1, packetCount=1000):
     packets = list(range(packetCount, 0, -1))
     window = [0] * windowSize
     time = 0
    
     while packets or any(window):
          time += 1
          print(f"\n------ Step {time} ------")
        
          # Load packets into window
          for index in range(windowSize):
               if window[index] == 0 and packets:
                    window[index] = packets.pop()
        
          print("Window after loading packets:", window)
        
          # Process the window and simulate ACK/NACK
          for i in range(windowSize):
               if window[i] != 0:
                    if createStatus(probOfNACK):
                         print(f"ACK received for packet {window[i]}")
                         window[i] = 0
                    else:
                         print(f"NACK received for packet {window[i]}, will retransmit")
        
          print("Window after processing:", window)
          #print("Remaining packets:", packets)

