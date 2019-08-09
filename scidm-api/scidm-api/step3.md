一鍵下載資料市集的工具之一

ckanSync

https://github.com/Thomas-Tsai/ckanDataDeployTools

使用上只要下載/clone git 上的程式原始碼，安裝對應的python套件，就可以使用。

我們需要用到下載與解壓縮工具

`apt-get install curl unzip`{{execute}}

下載請執行

`curl -L -k https://github.com/Thomas-Tsai/ckanDataDeployTools/archive/master.zip -o ckanSync.zip`{{execute}}

解壓縮

`unzip ckanSync.zip`{{execute}}

進行 python modules 安裝

`cd ckanDataDeployTools-master`{{execute}}

`pip3.5 install -r requirements.txt`{{execute}}

下載 mnist

`python3.5 ckanSync.py mnist`{{execute}}
