# PySniff

A simple packet sniffing script i decided to make in order to help rememdy a faulty network connection.

## Why?
  My Linux machine does not have an integrated wifi adapter, and the ethernet ports are disabled where I live. Since I was on a budget, the USB network adapter I purchased has a tendency to disconnect at random times, but the comptuer does not provide any feedback to indicate the loss of connection. 
  
  By having this script open in the background, I can constantly monitor the status of my network as well as the packet information. Basically, two birds with one stone. If the connection is lost, the destination MAC addresses will default to 00:00:00... or FF:FF:FF... 
  
