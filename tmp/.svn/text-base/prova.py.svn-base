
import threading
class Worker(threading.Thread):
      reqID = 0
      def __init__(self, id_serv, coa_consultes, coa_respostes, **kwds):
          threading.Thread.__init__(self, **kwds)
          self.setDaemon(1)
          self.workRequestQueue = coa_consultes
          self.resultQueue = coa_respostes
          self.start()
          self.id_serv = id_serv
      
      def performWork(self, id_work):
          "called"
          Worker.reqID+=1
          self.workRequestQueue.put((Worker.reqID, id_work))
          return Worker.reqID
      
      def run(self):
          while 1:
              reqID, id_work = self.workRequestQueue.get()
              #print "SERVER ",self.id_serv, "      Request ID ", reqID, "id_work = ",id_work
              self.resultQueue.put((reqID, id_work+1))
              

import Queue
from random import *

if __name__ == "__main__":
   coa_cons = Queue.Queue()  
   coa_res = Queue.Queue()

   for i in range(3):
       worker = Worker(i, coa_cons, coa_res)

   for c in range(100):
       p = (random()*10)%255
       coa_cons.put((c, p))
       rID, r_work = coa_res.get()
       print p, "  ",r_work
       
       