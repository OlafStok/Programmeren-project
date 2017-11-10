import hashlib
import time
import json
import dict2xml
import urllib.request
import random
import re

publickey = "9f7c5ef3984bf26b3fda32ed64602dfe"
privatekey = "22470edb225057c649fa5b023f34988f92b94aab"
characters = {}
id = ""
name = ""
charoffset = 0

def request(whattoget, offset):
    #parameters offset kan je bepalen. offset is hoe ver je naar voren moet zoeken dus als
    #naam ben parker id blabla naam ben reilly id blabla is offset 0 en offset 1 is dan
    #naam reilly id blabla naam ben urich id blabla
    parameters = "&orderBy=name&limit=100&offset=" + offset
    #timestamp, iets dat telkens veranderd voor security
    timestamp = str(time.time());
    #dit maakt een string van de timestamp en keys
    tomd5 = timestamp + privatekey + publickey
    #dit encode de md5 naar utf-8 voor de hashlib functie
    tomd5 = tomd5.encode('utf-8')
    #dit maakt een md5 hash van tomd5
    #is een lege md5 som
    md5_ts_pk_prk = hashlib.md5()
    #hier voeg je de text aan de lege md5 toe
    md5_ts_pk_prk.update(tomd5)
    #hier maak je md5 van de text in t md5 bestand
    md5_ts_pk_prk = md5_ts_pk_prk.hexdigest()
    #hier verander je de list van bytes weer in een string
    md5_ts_pk_prk = str(md5_ts_pk_prk)
    #hier definier je de request-url
    testrequest = "http://gateway.marvel.com/v1/public/" + whattoget + "?ts=" + timestamp + parameters + "&apikey=" + publickey + "&hash=" + md5_ts_pk_prk;
    #we printen m voor troubleshooting
    print(testrequest)
    #dit slaat de json die de server returnt op in een variable
    jsonfile = urllib.request.urlopen(testrequest).read()
    global jsondict
    #hier wordt de json veranderd in een dict
    jsondict = json.loads(jsonfile)
    #de dict verandert in een xml file
    xmlfile = dict2xml.dict2xml(jsondict);



    #maak een xmlbestand
    with open("xmlfromjason.xml", "w") as xmlfilefile:
        xmlfilefile.write(xmlfile);

def getlistofcharacters(offset):
    #pakt een lijst characters
    request("characters", str(offset))
    for result in jsondict["data"]["results"]:
        print("naam: " + result["name"] + " - id: " + str(result["id"]))
        global characters
        #maakt een global variable characters, een dict met id en naam gelinkt
        characters[result["id"]] = result["name"];
    return characters

def gethintsfromlistofcharacterwithid(characterid):
    # timestamp, iets dat telkens veranderd voor security
    timestamp = str(time.time());
    # dit maakt een string van de timestamp en keys
    tomd5 = timestamp + privatekey + publickey
    # dit encode de md5 naar utf-8 voor de hashlib functie
    tomd5 = tomd5.encode('utf-8')
    # dit maakt een md5 hash van tomd5
    # is een lege md5 som
    md5_ts_pk_prk = hashlib.md5()
    # hier voeg je de text aan de lege md5 toe
    md5_ts_pk_prk.update(tomd5)
    # hier maak je md5 van de text in t md5 bestand
    md5_ts_pk_prk = md5_ts_pk_prk.hexdigest()
    # hier verander je de list van bytes weer in een string
    md5_ts_pk_prk = str(md5_ts_pk_prk)
    #hier definieer je de request url
    testrequest = "http://gateway.marvel.com/v1/public/characters/" + characterid + "?ts=" + timestamp + "&apikey=" + publickey + "&hash=" + md5_ts_pk_prk;
    # we printen m voor troubleshooting
    print(testrequest)
    with open ("characterdata.json", "w+") as characterdatafile:
        #dit slaat de json die de server returnt op in een variable
        characterdata = urllib.request.urlopen(testrequest).read()
        characterdatafile.write(str(characterdata))
    characterdata = json.loads(characterdata)
    hasdescription = False
    for result in characterdata["data"]["results"]:
        if result["description"] != "":
            hasdescription = True
    if not hasdescription:
        return "ERROR! HAS NO DESCRIPTION"
    else:
        for result in characterdata["data"]["results"]:
            hint1 = str(result["description"])
            hint1 = hint1.replace(str(result["name"]), "---")
            hint1 = re.sub("()/", "", hint1)
            for namepart in str(result["name"]).split(" "):
                if namepart != "the" and namepart != "The" and namepart != "THE":
                    hint1 = hint1.replace(namepart, "---")

            temphint1 = str(hint1)
            temp2hint1 = str(hint1)
            hint1 = hint1[:int(len(hint1)/3)] + "\n"
            temphint1 = temphint1[int(len(temphint1)/3):int(len(temphint1)/3*2)] + "\n"
            temp2hint1 = temp2hint1[int(len(temp2hint1) / 3*2):int(len(temp2hint1))]
            hint1 = hint1 + temphint1 + temp2hint1
            hint2 = "the first half of this characters name is: " + str(result["name"])[0:int(len(str(result["name"]))/2)]
            hint3 = "the second half of this characters name ends with: " + str(result["name"])[int(len(str(result["name"]))/4*3):len(str(result["name"]))]
            answer = (str(result["name"]))
            print(hint1)
            print(hint2)
            print(hint3)
            print("---\n" + answer)
            print(hint1 + ";;;" + hint2 + ";;;" + hint3 + ";;;" + answer)
            return hint1 + ";;;" + hint2 + ";;;" + hint3 + ";;;" + answer


def randomIDfromlist():
    with open("idswithdesc.txt", "r") as ids:
        id = random.choice(ids.read().split("\n"))
    return str(id);

#getlistofcharacters(2000)
#gethintsfromlistofcharacterwithid(randomIDfromlist())
#randomIDandNAMEfromlist()


def createlistofIDswithdescription(characterid):
    #deze lijst is iets aangepast om characters met hele vreemde namen en te lange descriptions eruit te filteren, maar het grootste deel van de lijst idswithdesc
    #is gemaakt met deze functie
    try:
        if characterid == None:
            exit(99)
    # timestamp, iets dat telkens veranderd voor security
        timestamp = str(time.time());
    # dit maakt een string van de timestamp en keys
        tomd5 = timestamp + privatekey + publickey
    # dit encode de md5 naar utf-8 voor de hashlib functie
        tomd5 = tomd5.encode('utf-8')
    # dit maakt een md5 hash van tomd5
    # is een lege md5 som
        md5_ts_pk_prk = hashlib.md5()
    # hier voeg je de text aan de lege md5 toe
        md5_ts_pk_prk.update(tomd5)
    # hier maak je md5 van de text in t md5 bestand
        md5_ts_pk_prk = md5_ts_pk_prk.hexdigest()
    # hier verander je de list van bytes weer in een string
        md5_ts_pk_prk = str(md5_ts_pk_prk)
    #hier definieer je de request url
        testrequest = "http://gateway.marvel.com/v1/public/characters/" + characterid + "?ts=" + timestamp + "&apikey=" + publickey + "&hash=" + md5_ts_pk_prk;
        print(characterid)
        characterdata = urllib.request.urlopen(testrequest).read()
        characterdata = json.loads(characterdata)
        for result in characterdata["data"]["results"]:
            print(result["description"])
            if result["description"] != "" and result["description"] != " ":
                IDofresult = result["id"]
                with open("idswithdesc.txt", "a+") as idswithdescfile:
                    idswithdescfile.write(str(IDofresult) + "\n")
        createlistofIDswithdescription(str(characters.popitem()[0]))
    except:
        getlistofcharacters(charoffset = charoffset + 100)
        createlistofIDswithdescription(str(characters.popitem()[0]))




#createlistofIDswithdescription(str(characters.popitem()[0]))