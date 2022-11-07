if __name__ == '__main__':
   from collections import deque

   fifo = deque()
   l=[10,20,30,40]
   for i in [10, 20, 30, 40]:
      fifo.extend([30, 40])


   x = fifo.pop()

   x = fifo.pop()

   y = fifo.pop()


   print("x vaut ", x, " et y vaut ", y)