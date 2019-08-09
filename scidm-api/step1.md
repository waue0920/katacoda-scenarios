我們使用的是 Ubuntu Linux 系統，搭配 [ckan api 的手冊](https://app.swaggerhub.com/apis/jeanhsu/NCHC_DataMarket/V1.0)，使用者可以快速學習利用 API 搜尋與下載資料集與相關資源。

開始之前請請先進行套件庫更新

`apt-get update`{{execute}}

我們先用基本工具學習資料市集API與相關metadata架構，先安裝 curl

`apt-get install curl`{{execute}}

curl 安裝完畢之後我們先搜尋一個資料集，如果不知道要搜尋什麼資料集，可以到[資料市集網站](https://scidm.nchc.org.tw)探險看看，在這邊我們用AI訓練用的hello world 神級資料集 MNIST 來試試看！

`curl https://scidm.nchc.org.tw/api/3/action/package_search?q=mnist`{{execute}}

這個指令協助我們執行一個 restful api [package_search](https://app.swaggerhub.com/apis/jeanhsu/NCHC_DataMarket/V1.0#/action/get_action_package_search)，API用途請參考[手冊](https://app.swaggerhub.com/apis/jeanhsu/NCHC_DataMarket/V1.0#/action/get_action_package_search)，回傳的內容會以 [JSON 格式](https://zh.wikipedia.org/wiki/JSON)表示出來。

為了有效的瀏覽JSON format，我們建議安裝一個工具 jq ，請執行以下安裝指令。

`apt-get install jq`{{execute}}

讓我們再執行一次 curl 並將結果 pipe 導向 jq，指令如下：

`curl https://scidm.nchc.org.tw/api/3/action/package_search?q=mnist | jq`{{execute}}

根據回傳的結果，我們看到搜尋結果剛好只有一筆資料，接下來我們仔細看回傳的內容。基本上回傳項目包含有API執行狀態、結果。回傳結果就是資料集詮釋資料，在ckan稱之為 package 的結構。package 結構中會包含許多 metadata 的欄位，其中最主要的有 id, name, tag, organization, resiurces, note, license_title，還有其他...，基本上和[台灣資料集詮釋資料標準規範](https://data.gov.tw/node/18252)差不多？！

了解資料集 / package 之後，需要進一步了解資源檔案的詮釋資料，也就是 ckan 中定義的 resource 結構，主要是用來描述資源/檔案的屬性，其中比較重要的有 id, name, url，所以，當我們確認並取得 url 這個 matadata 的屬性之後，就可以依照 url 的值取得檔案。讓我們執行以下範例：

先確認我們需要的資料集 mnist，並複習資料集的詮釋資料

`curl https://scidm.nchc.org.tw/api/3/action/package_show?id=mnist | jq`{{execute}}

確認 mnist 就是我們要下載的資料集，與確認相關資源描述

`curl https://scidm.nchc.org.tw/api/3/action/package_show?id=mnist | jq .result.resources `{{execute}}

取得其中的 url 屬性

`curl https://scidm.nchc.org.tw/api/3/action/package_show?id=mnist | jq .result.resources[].url `{{execute}}

就可以看到資源/檔案的url的值

"https://scidm.nchc.org.tw/dataset/ef890176-6fd9-499d-9687-5fe2863c6941/resource/c24b3977-b37e-40a9-88fc-993a65308830/download/train-labels-idx1-ubyte.gz"

可以用 curl 直接下載

`curl https://scidm.nchc.org.tw/dataset/ef890176-6fd9-499d-9687-5fe2863c6941/resource/c24b3977-b37e-40a9-88fc-993a65308830/download/train-labels-idx1-ubyte.gz -o train-labels-idx1-ubyte-0.gz`{{execute}}``


到這邊，應該有基本概念，並可以用curl取得需要的檔案。

接下來，可以學習如何用 python 進行自動化程式與資料集API之互動。
