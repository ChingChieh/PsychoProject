# 使用法方
## 先把專案複製到本地端
在終端機 (terminal) 輸入
```
$ git clone https://github.com/ChingChieh/PsychoProject.git
```
然後進入該 directory
```
$ cd PsychoProject
```
## 開始
在終端機 (terminal) 打以下
- 啟動 server:
```
$ ./base
```
- 啟動 client:
```
$ ./base_client
```
目前需要 3 個 client 才能開始運作，如果要在同一台電腦上測試可以多開幾個 terminal 視窗來跑 client

## 中間過程
### 連線完成
當三個 clients 都連上 server 之後 server 的終端機視窗會出現
```
$ All users are connected. Wait for signal (type any key and "enter" or "enter" only):
```
此時只要按 enter 就可以進入下個階段

### 按5
接下來會出現按 5 的畫面
![](https://i.imgur.com/4rdRXOg.png)
當每個 client 都按5之後就會開始每個 trail 的步驟

### 測驗開始
以下是 ID 為 3 的人的畫面，按 1 代表選 ID 2 的人，按 2 代表選右邊的人
![](https://i.imgur.com/6mPxYqz.png)

### 不同台電腦測試
要先把 base_client 裡面第 355 行的 Host 參數改成 server 的 IP
```python
# 原本
Host = socket.gethostbyname(socket.gethostname())

# 改成 server 所在的 IP
Host = '140.116.xxx.xxx'
```
