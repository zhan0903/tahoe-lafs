from twisted.application import service
import time,thread

threshold_workload = 2
threshold_interval = 60#


class Cr_monitor(service.MultiService):
    """
    I am a serveice that watch the tahoe-LAFS's workload, and decide to
    do someting.
    """
    def __init__(self,storage_broker):
        service.MultiService.__init__(self)
        self.storage_broker = storage_broker

    def startService(self):
        print "startService in Cr_monitor"
        service.MultiService.startService(self)
        thread.start_new_thread(self.workload_monitor,())

    def workload_monitor(self):#implement adaptive check algorithm
        """
        implement adaptive check algorithm,recently implement a simple strategy:
        every 60 sec detect the network workload and then decide if check file
        and repair file.
        """
        print "start workload_monitor..."
        while True:
            time_start = time.time()
            for server in self.storage_broker.get_connected_servers():
                version = server.get_version()
            time_end = time.time()
            elapse_time = time_end - time_start
            print "elapse time:",elapse_time
            if elapse_time < threshold_workload:
                self.passive_r()
            time.sleep(threshold_interval)
        
    def passive_r(self):#repair invalid file in a passive way
        print "in passive_cr"

    def adaptive_c(self):#
        print "in adaptive_c"
        

    
