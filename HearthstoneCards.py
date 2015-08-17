
import urllib
import urllib2
import re




'''
hero: mage, hunter, paladin, warrior, druid, warlock, shaman, priest, rogue
'''


class Spider:
    
    def __init__(self):
        self.siteURL = 'http://db.duowan.com/lushi/card/list/eyJwIjoxLCJzb3J0IjoiaWQuZGVzYyJ9.html'
        self.content = ''
    
    def getPage(self):
        return self.siteURL
    
    
    def getContent(self):
        request = urllib2.Request(self.getPage())
        try: 
            print 'fetch page success'
            self.content = urllib2.urlopen(request)
            
        except urllib2.URLError, e:
            print e                




def fillCardInfo(rawInfo):
    isParseStart = False
    card = {}
    print rawInfo
    for line in rawInfo:
        #print line
        if isParseStart == True:
            if 'color' in line:
                card['rarity'] = line.split('#')[1].split('\"')[0]
                print card
            elif 'target=' in line:
                card['chineseName'] = line.split('>')[1]
                print card
            
        if 'tbody' in line:
            if isParseStart == False:
                print 'Parse start'
                isParseStart = True
            else:
                print 'Parse done'
                isParseStart = False    

        



if __name__=="__main__":
    spider = Spider()
    spider.getContent()
    #print spider.content.read()
    fillCardInfo(spider.content.readlines())
    
    
    
    
    
    