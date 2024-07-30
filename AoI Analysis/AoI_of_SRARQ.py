from create_status import createStatus

def AoIOfSRARQ(windowSize=3, probOfNACK=0.1, packetCount=1000):
     packets = list(range(packetCount, 0, -1))  # creating mock packets
     window = [0] * windowSize  # creating a window
     AoI = []  # aoi for storing every step
     AoI_ind = {i: 0 for i in range(1, packetCount + 1)}  # Initialize AoI for each packet

     while packets or any(window):
          AoI_temp = []

          # Load new packets into the window if slots are free
          for index in range(windowSize):
               if window[index] == 0 and packets:
                    window[index] = packets.pop()

          print("Window after loading packets:", window)

          # Process the packets in the window
          for index in range(windowSize):
               if window[index] > 0:
                    if createStatus(probOfNACK):
                         print(f"ACK received for packet {window[index]}")
                         AoI_ind[window[index]] *= -1  # Packet successfully acknowledged
                         AoI_temp.append(AoI_ind.get(window[index]))
                         window[index] = 0  # Clear the slot
                    else:
                         print(f"NACK received for packet {window[index]}")
                         AoI_ind[window[index]] += 1  # Increase AoI since NACK received
                         AoI_temp.append(AoI_ind.get(window[index]))

                    print(AoI_ind)


          AoI.append(AoI_temp)
     return AoI