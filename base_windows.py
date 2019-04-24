#!/usr/bin/env python3
import socketserver
from time import ctime
from time import sleep
import time
import socket
import sys
#from termios import tcflush, TCIFLUSH
import threading
import json
import pandas as pd
import random

class MyRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        #print(df.head())
        global current_client, allclient_connect, allclient_press5, lock, ID_CLIENT, trail, sourceList
        self.thread_id = int(threading.currentThread().getName().split("-")[1])
        self.data = None;
        self.request.send(bytes(str((self.thread_id - 1) % 3 + 1),"utf-8"))
        
        lock.acquire()
        ID_list.append(self.thread_id)
        current_client.append(self.request)
        lock.release()
        
        print('a user connect, IP:',self.client_address)
        print("This thread id",self.thread_id)
        if len(current_client) >= max_client_count: # only one client will enter this IF condition
            #tcflush(sys.stdin, TCIFLUSH)  # clean the input queue, try to avoid type 'enter' beforehead
            print(ID_list,current_client)
            signal = input("All users are connected. Wait for signal (type any key and \"enter\" or \"enter\" only): ")
            message = "press 5 to continue"
            for s in current_client:
                s.sendall(bytes(message,"utf-8"))
            print("wait for clients to answer...")
            ID_CLIENT = current_client.copy()
            current_client.clear()
            allclient_connect = 1

        while True: # Some client need to wait here for other clients connect to server
            if allclient_connect == 1:
                break

        client_press_5 = self.request.recv(1024).strip().decode()
        current_client.append(self.request)

        # In this if, server send ID to all clients and pass the first source list to them
        if len(current_client) >= max_client_count:
            #tcflush(sys.stdin, TCIFLUSH)  # clean the input queue, try to avoid type 'enter' beforehead
            message = "Start the game!"
            #for s,i in zip(ID_CLIENT,ID_list):
            #    s.sendall(bytes(i,"utf-8"))
            for s in ID_CLIENT:
                sourceList = list(df.loc[trail, ['PlayerA', 'PlayerB','PlayerC']])
                s.sendall(bytes(str(sourceList),"utf-8"))
            current_client.clear()
            allclient_press5 = 1
            # trail += 1

        while True:
            if allclient_press5 == 1:
                break


    def handle(self):
        global finishSelect_client, after_firstTrail, trail, clientSelection, trailFail, whoPick, sourceList, allocate, allocList
        # print('connect from ', self.client_address)
        # cur_trd = threading.current_thread()
        print("Server request info:",self.request)
        while True:
            if after_firstTrail:
                sourceList = list(df.loc[trail, ['PlayerA', 'PlayerB','PlayerC']])
                self.request.send(bytes(str(sourceList),"utf-8"))


            self.data = self.request.recv(1024).strip().decode()
            if not self.data:  # If client disconnect data will be None
                break
            else:
                print(self.thread_id ,"client say:", self.data)
                #self.request.sendall(('%s' % data).encode())
                #client_finish = self.request.recv(1024).strip().decode()
                #print("after client finish:", client_finish)
                current_client.append(self.request)
                finishSelect_client += 1
                clientSelection[int(self.thread_id) - 1] = int(self.data)

            if len(current_client) >= max_client_count:   # 傳送給每個client, 所有client選了誰
                if (-1 in clientSelection) or (sum(clientSelection) == 6):
                    # clientSelection = [-1, -1, -1]
                    whoPick = [-1,-1,-1]
                    trailFail = 1
                
                if not trailFail:
                    # 該決定誰要開始
                    whoPick[0] = (clientSelection[clientSelection[0] - 1] == 1) * 1    
                    whoPick[1] = (clientSelection[clientSelection[1] - 1] == 2) * 1    
                    whoPick[2] = (clientSelection[clientSelection[2] - 1] == 3) * 1    
                    print(whoPick)
                    print("####",sourceList)
                    whoPick = [a * b for a,b in zip(whoPick,sourceList)]
                    print(whoPick)
                
                    whoPickMax = max(whoPick)
                    if whoPick.count(whoPickMax) - 1:
                        minIndex = whoPick.index(min(whoPick))
                        whoPick[randTwoNumber((minIndex + 1) % 3, (minIndex + 2) % 3)] = 0
                        whoPick[whoPick.index(max(whoPick))] = 1
                        print(whoPick)
                    else:
                        maxIndex = whoPick.index(whoPickMax)
                        whoPick[(maxIndex + 1) % 3] = 0
                        whoPick[(maxIndex + 2) % 3] = 0
                        whoPick[whoPick.index(max(whoPick))] = 1   
                        print(whoPick)

                for s in current_client:
                    s.sendall((str(clientSelection) + ',' + str(whoPick)).encode())
                    
                current_client.clear()
                trail += 1
                after_firstTrail = 1
                finishSelect_client = 0
                allocate = 0

            while True:
                if finishSelect_client == 0:
                    break

            if trailFail == 1:
                a = time.time()
                sleep(14)
                b = time.time()
                print("time elapse: ", b - a)
                trailFail = 0
                clientSelection = [0] * 3
                continue
            print("whoPick type:",type(whoPick))
            if whoPick[int(self.thread_id) - 1]:
                allocList = self.request.recv(1024).strip().decode()
                allocate = 1
            else: 
                while True:
                    if allocate == 1:
                        break

            self.request.send(bytes(str(allocList),"utf-8"))


        self.request.close()
    def finish(self):
        print('A user diconnect.')

class ThreadingTCPSserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True        # kill all of the thread when get any exceptions
    allow_reuse_address = True   # avoid some error when reboot the server
    pass

def getData():
    df = pd.read_excel("dic.xlsx")
    df.drop(df.columns[6:],axis = 1, inplace=True)
    df.columns = df.iloc[0]
    df.drop([0],axis = 0, inplace=True)
    return df

def getGroup(ID):
    group = int((ID_list.index(ID))) // 3 + 1
    return group
    
    

def randTwoNumber(num1,num2):
    ran = random.randint(0,1)
    return num1 if ran else num2

if __name__ == "__main__":

    # List variable
    lock = threading.Lock()
    sourceList = []
    allocList = []
    ID_list = []
    ID_CLIENT = []
    current_client = []
    
    #clientSelection = []

    # variable
    trail = 1
    trailFail = 0
    after_firstTrail = 0
    finishSelect_client = 0
    allclient_press5 = 0
    max_client_count = 4       # This variable decide how many client can connect 
    clientSelection = [0] * 3
    whoPick = [0] * 3
    allclient_connect = 0
    allocate = 0
    connected_client = 0


    df = getData();
    print(df.head());

    # HOST, PORT = '127.0.0.1', 10001
    HOST = socket.gethostbyname(socket.gethostname())   # check current IP address
    PORT = 10001
    print(HOST)
    ADDRESS = (HOST,PORT)
    try:
        with ThreadingTCPSserver(ADDRESS,MyRequestHandler) as server:
            print('waiting for connection')
            server.serve_forever()
    except KeyboardInterrupt:
        print("\ncaught keyboard interrupt, exiting")
        server.shutdown()
        server.server_close()
    except ConnectionResetError:
        print("client already close! can't send!")
