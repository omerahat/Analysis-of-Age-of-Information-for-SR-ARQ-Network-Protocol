# AoIOfSRARQ

> AoIOfSRARQ(int windowSize, float probOfBadChannel, float probOfBadNACK, float probOfGoodNACK, int packetCount)


## Description

Simulates SRARQ Protocol for with AoI

## Parameters

- `windowSize`: The size of the window. The default value is 3.
- `probOfBadChannel`: The possibility of a bad channel. The default value is 0.2.
- `probOfBadNACK`: The possibility of returning NACK when the channel is bad. The default value is 0.8.
- `probOfGoodNACK`: The possibility of returning NACK when the channel is good. The default value is 0.1.
- `packetCount`: The amount of packets. The default value is 1000.

## What the Function Returns

Returns a 2D array that stores the AoI of each packet in the window at each step.
