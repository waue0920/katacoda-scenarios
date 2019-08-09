以 curl 上傳檔案範例：

`apt-get install curl`{{execute}}

先到網站建立好資料集，並輸入適當的詮釋資料

資料集上傳之前，需要取得 API KEY

語法：

curl -H 'Authorization: API_金鑰' 'https://[hostname]/api/action/resource_create' --form upload=@檔案路徑 --form package_id=資料集ID/名稱 --form name=顯示名稱

以指令上傳請執行

`curl -H 'Authorization: XXXXXX' 'https://scidm.nchc.org.tw/api/action/resource_create' --form upload=@test_file.txt --form package_id=XXXXXX --form name=uploaded_file`{{execute}}
