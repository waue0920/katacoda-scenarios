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
