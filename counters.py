import time, os, glob

counter_paths = {}

paths = glob.glob('/sys/class/net/*/device/infiniband/*/ports/*/counters/port_rcv_data')
for p in paths:
   segs = p.split('/')
   print(segs)
   dev = segs[4]
   ca = segs[7]
   counter_paths[('%s (%s)' % (dev, ca)).ljust(15)] = p

curr = {}
rate = {}
while True:
  for k, p in counter_paths.items():
    with open(p) as f:
       counter = int(f.read().strip())
       last = curr.get(k, counter)
       rate[k] = counter - last
       curr[k] = counter
  for k, v in rate.items():
     print(k, ':', v)
  time.sleep(1.0)
