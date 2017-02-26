import httplib, urllib, base64
import cognitive_face as CF

KEY = '7d7f3f0463de4f1cbe29d9c9225768af'
CF.Key.set(KEY)
CompareUrl= "http://rivista-cdn.pittsburghmagazine.com/Best-of-the-Burgh-Blogs/The-412/May-2014/Want-to-Win-a-Free-Flight-to-San-Francisco/c117ecd8acbe616668fea6528829433a.jpg?ver=1400627273"
def catalog(imgURL_list):
    data = []
    for url in imgURL_list:
        if url == -1: #do we want to completely take it out of the list?
            break;
        try:
            result = CF.face.detect(url)
            data.append(result)
        except:
            pass
    return data
def compare(userURL, data, imgURL_list):
    result = CF.face.detect(userURL)
    try:
        for url in imgURL_list:
            CF.face_list.add_face(url, 'kjhtvuyctyurkuyrkycr')
    except:
        pass
    sim = CF.face.find_similars(result[0]['faceId'], 'kjhtvuyctyurkuyrkycr', max_candidates_return = 1, mode = 'matchFace')
    return sim
    
url_list = open("url_list.txt", "r")
URLS = []

while True :
    line = url_list.readline()
    URLS.append(line)
    if ("" == line):
        print "file finished"
        break
data = catalog(URLS)
#data_ids = CF.face_list.create('kjhtvuyctyurkuyrkycr')
similarFace = compare(CompareUrl, 'kjhtvuyctyurkuyrkycr', URLS)
print similarFace

    

