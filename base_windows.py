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
from ast import literal_eval

class MyRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        #print(df.head())
        global current_client, allclient_connect, allclient_press5, lock, ID_CLIENT
        global trail, sourceList, clientSelection, whoPick, trailFail
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

            # Initialize global variable
            clientSelection = [[0 for x in range(3)] for y in range(len(ID_list) // 3)]
            whoPick = [[0 for x in range(3)] for y in range(len(ID_list) // 3)]
            trailFail = [0 for i in range(len(ID_list) // 3)]

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
        global finishSelect_client, after_firstTrail, trail, clientSelection, trailFail 
        global whoPick, sourceList, allocate, allocList, ID_list
        # print('connect from ', self.client_address)
        # cur_trd = threading.current_thread()
        print("Server request info:",self.request)
        while True:
            if after_firstTrail:
                sourceList = list(df.loc[trail, ['PlayerA', 'PlayerB','PlayerC']])
                print("Source:",sourceList)
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
                # data[0]:開始時間   data[1]:決策時間   data[2]:選了誰
                self.data = literal_eval(self.data)
                clientSelection[getGroup(self.thread_id) - 1][(int(self.thread_id) - 1) % 3] = int(self.data[2])

            if len(current_client) >= max_client_count:   # 傳送給每個client, 所有client選了誰
                print("trailFail:",trailFail)
                for i in range(len(ID_list) // 3):
                    if (-1 in clientSelection[i]) or (sum(clientSelection[i]) == 6):
                        # clientSelection = [-1, -1, -1]
                        whoPick[i] = [-1,-1,-1]
                        trailFail[i] = 1

                for i in range(len(trailFail)):
                    if not trailFail[i]:
                        # 該決定誰要開始
                        whoPick[i][0] = (clientSelection[i][clientSelection[i][0] - 1] == 1) * 1
                        whoPick[i][1] = (clientSelection[i][clientSelection[i][1] - 1] == 2) * 1
                        whoPick[i][2] = (clientSelection[i][clientSelection[i][2] - 1] == 3) * 1
                        print(whoPick[i])
                        print("####",sourceList)
                        whoPick[i] = [a * b for a,b in zip(whoPick[i],sourceList)]
                        print(whoPick[i])

                        whoPickMax = max(whoPick[i])
                        if whoPick[i].count(whoPickMax) - 1:
                            minIndex = whoPick[i].index(min(whoPick[i]))
                            whoPick[i][randTwoNumber((minIndex + 1) % 3, (minIndex + 2) % 3)] = 0
                            whoPick[i][whoPick[i].index(max(whoPick[i]))] = 1
                            print(whoPick[i])
                        else:
                            maxIndex = whoPick[i].index(whoPickMax)
                            whoPick[i][(maxIndex + 1) % 3] = 0
                            whoPick[i][(maxIndex + 2) % 3] = 0
                            whoPick[i][whoPick[i].index(max(whoPick[i]))] = 1
                            print(whoPick[i])

                for index,s in enumerate(ID_CLIENT):
                    s.sendall((str(clientSelection[index // 3]) + ',' + str(whoPick[index // 3])).encode())

                current_client.clear()
                trail += 1
                after_firstTrail = 1
                finishSelect_client = 0
                allocate = 0
                # 當每48次要重新對每個 client 分配ID
                if (trail - 1) % shuffle_num == 0:
                    print("HEY! We need shuffle!!!")
                    random.shuffle(ID_list)
                    # self.request.send(bytes(str(ID_list),"utf-8"))


            while True:
                if finishSelect_client == 0:
                    break

            if trailFail[getGroup(self.thread_id) - 1] == 1:
                a = time.time()
                sleep(14)
                b = time.time()
                print("time elapse: ", b - a)
                trailFail[getGroup(self.thread_id) - 1] = 0
                clientSelection[getGroup(self.thread_id) - 1] = [0] * 3
                # 這裡有個小疑問是說傳 ID 的時候是傳 1-3 還是 1-6
                if (trail - 1) % shuffle_num == 0:
                    print("HEY! Send ID:", getPassID(self.thread_id))
                    self.request.send(bytes(str(getPassID(self.thread_id)),"utf-8"))
                continue

            if whoPick[getGroup(self.thread_id) - 1][(int(self.thread_id) - 1) % 3]:
                allocList = self.request.recv(1024).strip().decode()
                allocate = 1
            else:
                while True:
                    if allocate == 1:
                        break

            
            # 這裡有個小疑問是說傳 ID 的時候是傳 1-3 還是 1-6
            if (trail - 1) % shuffle_num == 0:
                print("HEY! Send ID:", getPassID(self.thread_id))
                self.request.send(bytes(str(getPassID(self.thread_id)) + ',',"utf-8"))
            
            self.request.send(bytes(str(allocList),"utf-8"))
            print("allocList:", allocList)

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
    
def getPassID(ID):
    print("thread:",ID)
    print("new:", ID_list.index(ID) % 3 + 1)
    return ID_list.index(ID) % 3 + 1
    
def randTwoNumber(num1,num2):
    ran = random.randint(0,1)
    return num1 if ran else num2

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    # List variable
    lock = threading.Lock()
    sourceList = []
    allocList = []
    ID_list = []
    ID_CLIENT = []
    current_client = []

    # variable
    trail = 1
    trailFail = 0              # Initialize in setup method
    after_firstTrail = 0
    finishSelect_client = 0
    allclient_press5 = 0
    max_client_count = 3       # This variable decide how many client can connect
    clientSelection = []       # Initialize in setup method
    whoPick = [0] * 3          # Initialize in setup method
    allclient_connect = 0
    allocate = 0
    connected_client = 0
    shuffle_num = 3

    df = getData();
    print(df.head());

    # HOST, PORT = '127.0.0.1', 10001
    HOST = socket.gethostbyname(socket.gethostname())   # check current IP address
    PORT = 10001

    if (len(sys.argv) == 2):
        if(RepresentsInt(sys.argv[1])) and not(int(sys.argv[1]) % 3):
            max_client_count = int(sys.argv[1])
        else:
            print("Input format is wrong, please try: python base_windows.py 6")
            print("Can change number after program to other number that is multiple of 3")
            sys.exit()
    else:
        pass

    print("max_client_count:",max_client_count)

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
