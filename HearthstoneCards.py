
import urllib
import urllib2
import re




'''
hero: mage, hunter, paladin, warrior, druid, warlock, shaman, priest, rogue
'''
rarityMapping = {'008000':'white',
	               '3366ff':'blue',
	               'c600ff':'purple',
	               'FF6600':'orange'}
TOTAL_PAGE_NUM = 14
class Spider:
    
    def __init__(self):
        self.siteURL = 'http://db.duowan.com/lushi/card/list/eyJwIjoxLCJzb3J0IjoiaWQuZGVzYyJ9.html'
        self.content = ''
    
    def getNextPage(self):
        self.siteURL = ''
        for line in self.content.readlines():
            if 'next' in line:
                self.siteURL = line.split('href=\"')[1].split('\">')[0]
                print self.siteURL          
        return self.siteURL
    
    
    def getContent(self):
        request = urllib2.Request(self.siteURL)
        try: 
            print 'fetch page success'
            self.content = urllib2.urlopen(request)
            
        except urllib2.URLError, e:
            print e                




def fillCardInfo(rawInfo,cardSet):
    isParseStart = False
    card = {}
    idx = 0
    #print rawInfo
    for line in rawInfo:
        #print line
        idx += 1
        if isParseStart == True:
            if 'color' in line:
                card['rarity'] = rarityMapping[line.split('#')[1].split('\"')[0]]
                print 'rarity '+card['rarity']
            elif 'target=' in line:
                card['chineseName'] = line.split('>')[1].split('<')[0].decode('utf-8')
                print 'chineseName '+card['chineseName']
            elif 'txt' in line:
                card['description'] = line.split('>')[1].split('<')[0].decode('utf-8')
                print 'description '+card['description']
                card['hero'] = rawInfo[idx].split('>')[1].split('<')[0].decode('utf-8')
                print 'hero '+card['hero']
                card['type'] = rawInfo[idx+1].split('>')[1].split('<')[0].decode('utf-8')
                print 'type '+card['type']
                card['crystal'] = rawInfo[idx+2].split('>')[1].split('<')[0].decode('utf-8')
                print 'crystal '+card['crystal']
                card['attack'] = rawInfo[idx+3].split('>')[1].split('<')[0].decode('utf-8')
                print 'attack '+card['attack']
                card['defence'] = rawInfo[idx+4].split('>')[1].split('<')[0].decode('utf-8')
                print 'defence '+card['defence']
                
                cardSet.append(card)
                card = {}
                card['rarity'] = 'blank'
            
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
    pageNum = 1
    #print spider.content.read()
    cardSet = []
    #fillCardInfo(spider.content.readlines(),cardSet)
    
    while spider.getNextPage() != '' and pageNum <= TOTAL_PAGE_NUM:
        spider.getContent()
        pageNum += 1
    
    
    
    
    
    