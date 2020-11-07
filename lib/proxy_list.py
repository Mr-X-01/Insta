# Author: Mr-X-01
# Telegram: @Mrxanon
# https://github.com/Mr-X-01

class ProxyList(object):

    def __init__(self):
        self.list = []

    def __contains__(self, proxy):
        for _proxy in self.list:
            if _proxy.ip == proxy['ip'] and _proxy.port == proxy['port']:
                return True 
        return False 

    def append(self, proxy):
        self.list.append(proxy) 
