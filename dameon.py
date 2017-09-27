from cw_libs import daemon
import socket
import sys
import json
from thread import *
import time

HOST = ''   
PORT = 4000

docker_client = cwd.CWDockerClient()


class RoundRobin(daemon.Daemon):
    def measureTimes(timeQuanta):
        start = time.time()
        user = 0#id of the user in the queue
        while 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            start_new_thread(clientthread ,(conn,))
            user = 1;#put for loop in later
            s.close()
        end = time.time()
        userTime = end - start
        return userTime
    def checkTime(timeQuanta - userTime):
        if timeQuanta < userTime):
            blacklist += user
            print 'you are taking too long'#error handle this later
            user = user + 1
    def execute():
        conn, addr = s.accept()
        start_new_thread(clientthread ,(conn,))
        measureTimes(timeQuanta)
        checkTimes(timeQuanta, userTime)


            

#have yet to make the driver class     
