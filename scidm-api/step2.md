開始學習利用 python module '''ckanapi''' 來開發API程式，透過之前學習到的curl方式取得資料換成python自動化方式執行。

我們需要先安裝 ckanapi 與相關 python 工具，請執行指令

`apt-get install python3-pip`{{execute}}

並用pip工具安裝 python 套件模組 ckanapi

`pip3.5 install ckanapi`{{execute}}

安裝完成之後，我們可以用 ckanapi 指令確認安裝是否成功

`ckanapi --help`{{execute}}

完成之後，我們可以直接參考範例程式碼：

    import urllib
    import urllib.error
    import urllib.request
    
    from ckanapi import RemoteCKAN
    url = "https://scidm.nchc.org.tw"
    ua  = 'ckanapiexample/1.0 (+http://example.com/my/website)'
    
    def downloadFile(url, name):
        try:
            opener = urllib.request.build_opener()
            #opener.addheaders = [('Authorization', key)]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url, name)
            return True
        except Exception as e:
            print("Sync %s to %s error.(%s)\n", url, name, str(e))
            return False
    
        return False
    
    
    demo = RemoteCKAN(url, user_agent=ua)
    pkg_data = demo.action.package_show(id='mnist')
    print(pkg_data)
    
    
    for res in pkg_data['resources']:
        print("download {0} to {1}".format(res['url'], res['name']))
        downloadFile(res['url'], res['name'])

上述程式如果想要執行，可以執行：

`python3.5 demo.py`{{execute}}
    
複雜程式碼我不想懂，能給我一個一鍵下載嘛？
