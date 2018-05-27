# -*- coding: utf-8 -*-

import SLACKBOT
from bs4 import BeautifulSoup
from gtts import gTTS
from SLACKBOT.lib.curve.ttypes import *
from datetime import datetime
from time import sleep
import time, datetime, random, sys, json, codecs, threading, glob, re, string, os, requests, html5lib, subprocess, urllib, urllib2, goslate, urllib3, wikipedia, ast

cl = SLACKBOT.LINE()
#cl.login(qr=True)
cl.login(token='TOKENMU')
cl.loginResult()

print "╔═════¤═════╗\n╠➣Login Success\n╚═════¤═════╝"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔════════════════════╗
    [HΣLP MΣSSΔGΣ]
╠════════════════════╝
╠➣Bc: [text]
╠➣Id: [Text]
╠➣Gpict [Text]
╠➣Music [Text]
╠➣Rename: [Text]
╠➣Say [Text]
╠➣Yt [Text]
╠➣Wiki [Text]
╠➣Pict group [Nama group]
╠➣Invite [@]
╠➣Info [@]
╠➣Mid [@]
╠➣Kill [@]
╠➣Vkick [@]
╠➣Blacklist
╠➣Gift
╠➣Mentionall
╠➣Translate
╠➣Set
╠➣Steal
╠➣Sider
╠➣Kernel 
╠➣Ifconfig 
╠➣System 
╠➣Cpu 
╠➣Copy
╠➣Speed
╠➣Runtime
╠➣Gurl
╠➣Gcreator
╠➣Group
╠➣Cancelall
╠➣Cancel invitation
╠➣Waktu
╠➣Whitelist
╠➣Sc: [mid]
╠➣Gn: [name]
╠➣Kick: [mid]
╠➣Minfo [mid]
╠➣Invite: [mid]
╚════════════════════╝
╔════════════════════╗
      sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
      TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

steal ="""╔════════════════════╗
    「 Steal Key 」
╠════════════════════╝
╠➣Steal pict [@]
╠➣Steal cover [@]
╠➣Steal vid [@]
╠➣Steal name [@]
╠➣Steal bio [@]
╠➣Steal gpict
╠════════════════════╝
╔════════════════════╗
      sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""
WhiteList ="""╔════════════════════╗
   「 Whitelist Key 」
╠════════════════════╝
╠➣Wl [@]
╠➣Unwl [@]
╠➣Clear Wl
╠➣White list
╠════════════════════╝
╔════════════════════╗
     sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

blacklist ="""╔════════════════════╗
    「 Blacklist Key 」
╠════════════════════╝
╠➣Ban [@]
╠➣Unban [@]
╠➣Clear ban [@]
╠➣Banlist
╠════════════════════╝
╔════════════════════╗
     sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

copy ="""╔════════════════════╗
     「 Copy Key 」
╠════════════════════╝    
╠➣Copy [@]
╠➣Copy pict [@]
╠➣Copy cover [@]
╠➣Copy name [@]
╠➣Copy bio [@]
╠➣Backup
╠════════════════════╝
╔════════════════════╗
     sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

groupkey ="""╔════════════════════╗
    「 Group key 」
╠════════════════════╝
╠➣Autojoin:[on/off]
╠➣Contact:[on/off]
╠➣Read [on/off]
╠➣Invite [on/off]
╠➣Join [on/off]
╠➣Gname [on/off]
╠➣Url:[on/off]
╠════════════════════╝
╔════════════════════╗
     sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

translateMessage =""" ╔════════════════════╗
    「 TRANSLATE 」
╠════════════════════╝
╠➣Tr-id = Indonesia
╠➣Tr-ja = Jepang
╠➣Tr-en = Inggris
╠➣Tr-es = Spanyol
╠➣Tr-th = Thailand
╠➣Tr-ko = Korea
╠➣Tr-jw = Jawa
╠➣Tr-ru = Rusia
╠➣Tr-ms = Malaysia
╠➣Tr-ar = Arab
╠➣Tr-fr = Perancis
╠➣Tr-it = Itali
╠➣Tr-de = Jerman
╠➣Tr-tr = Turki
╠➣Tr-la = Latin
╠➣Tr-vi = Vietnam
╠➣Tr-hi = India
╠➣Tr-su = Sunda
╠════════════════════╝
╔════════════════════╗
     sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ  : 
     TΣΔM SLΔCҜβΩT
╚════════════════════╝
line.me/ti/p/~fuck.you__
"""

mid = cl.getProfile().mid
Creator="MIDMU BABY"
admin=["MIDMU SAYANG"]

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "autoreject":False,
    "Members":0,
    "autoinvite":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "whitelist":{},
    "read":False,
    "Timeline":False,
    "name":False,
    "name":{},
    "Gname":{},
    "Contact":False,
    "lang":"JP",
    "BlGroup":{}
}

mimic = {
    "status":False,
    "target":{}
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'rom':{}
    }

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': 'album',
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def post_content(self, urls, data=None, files=None):
    return self._session.post(urls, headers=self._headers, data=data, files=files)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' %(hours,mins,secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","ï¼¾","ã‚µãƒ†ãƒ©:","ã‚µãƒ†ãƒ©:","ã‚µãƒ†ãƒ©ï¼š","ã‚µãƒ†ãƒ©ï¼š"] 
    for tex in tex:
        for command in commands:
            if string ==command:
                return True

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def updateProfilePicture(self, path):
    file=open(path, 'rb')
    files = {
        'file': file
    }
    params = {
        'name': 'media',
        'type': 'image',
        'oid': self.profile.mid,
        'ver': '1.0',
    }
    data={
        'params': json.dumps(params)
    }
    r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
    if r.status_code != 201:
        raise Exception('Update profile picture failure.')
    return True

def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "╠[ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
      print error

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
#---------------------------------------------------------------------------------------#        
        if op.type == 0:
            return
#---------------------------------------------------------------------------------------#
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
            print e
#---------------------------------------------------------------------------------------#
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)
#--------------NOTIFIED_INVITE_INTO_GROUP---------------------
        if op.type == 13:
            if wait["AutoJoin"] == True:
                cl.acceptGroupInvitation(op.param1)
#-------------------------------------------------------------
        if op.type == 13:
            if wait["autoreject"] == True:
                cl.rejectGroupInvitation(op.param1)
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
          if op.param1 in Backup:
                if not op.param2 in admin:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                          if target not in admin:
                            if target not in wait["whitelist"]:
                              try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                cl.inviteIntoGroup(op.param1, [op.param3])
                              except:
                                return
                    except Exception, e:
                        print e
#----------------------------------------------------------------------
        if op.type == 26:
            if wait["read"] == True:
                msg = op.message
                if msg.toType == 2:
                    msg.to = msg.to
                    msg.from_ = msg.from_
                    cl.sendChatChecked(msg.to,msg.id)


        if op.type == 26:
            if wait["read"] == True:
                msg = op.message
                if msg.toType == 0:
                    msg.to = msg.from_
                    msg.from_ = msg.to
                    cl.sendChatChecked(msg.from_,msg.id)
#-------------------------------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['name']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        pass
                    G.name = wait['Gname'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                      pass
                    cl.sendText(op.param1,"Jangan gonta ganti nama group asw 􀜁􀅈Rage Face􏿿")
#-------------------------------------------------------------------
        if op.type == 15:
          if wait["autoinvite"] == True:
            cl.inviteIntoGroup(op.param1, [op.param2])
#--------------------------SEND_MESSAGE---------------------------
        if op.type == 25:
            msg = op.message                     
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            cl.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            cl.sendText(msg.to,"aded")
            
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage)
                         cl.sendText(msg.to,msg.contentMetadata["mid"])
                         cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                         cl.sendImageWithURL(msg.to, cu)
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage)
                         cl.sendText(msg.to,msg.contentMetadata["mid"])
                         cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                         cl.sendImageWithURL(msg.to, cu)
#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\nMembers : " + str(len(ginfo.members)) + " members\nPending : " + sinvitee + " people\nURL : " + u + " it is inside")
                        cl.sendImageWithURL(msg.to, "http://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator)
                        cl.sendImageWithURL(msg.to, "http://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u78643d09e42a36836a17cc918963a8b7"}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"MyCreator╔═════¤═════╗\n  『✍͡➴͜Ĝα₤αηĸ͜͡✫』\n╚═════¤═════╝\nTikung aja Boss,kalau pacaran sama dia susah move on loh")
#--------------------------------------------------------
            elif msg.text in ["Group creator","Gcreator","gcreator"]:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Itu kak yang Buat Group ini")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
#--------------------------------------------------------
            elif msg.text in ["Translate"]:
                cl.sendText(msg.to,translateMessage)
#---------------------------------------------------------
            elif msg.text in ["Steal"]:
                cl.sendText(msg.to,steal)
#-----------------------------------------------------
            elif msg.text in ["Whitelist"]:
              cl.sendText(msg.to,WhiteList)
#---------------------------------------------------------
            elif msg.text in ["Blacklist"]:
              cl.sendText(msg.to,blacklist)
#---------------------------------------------------------
            elif msg.text in ["Copy"]:
              cl.sendText(msg.to,copy)
#--------------------------------------------------------
            elif msg.text in ["Group"]:
              cl.sendText(msg.to,groupkey)
#--------------------------------------------------------
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    Cl.sendText(msg.to,"Can not be used outside the group")
#-------------------------------------------------------
            elif msg.text in ["Ourl","Url:on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url on 􀜁􀆚Hare Krishna􏿿")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Curl","Url:off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
                wait["AutoJoin"] = True
                cl.sendText(msg.to,"AutoJoin Active 􀜁􀆚Hare Krishna􏿿")

            elif msg.text in ["Join off","Autojoin:off"]:
                wait["AutoJoin"] = False
                cl.sendText(msg.to,"AutoJoin inActive 􀜁􀆚Hare Krishna􏿿")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact on 􀜁􀆚Hare Krishna􏿿")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact off 􀜁􀆚Hare Krishna􏿿")
#--------------------------------------------------------
            elif msg.text in ["Status"]:
                md = ""
                if wait["autoreject"] == True: md+="🔹 Auto Reject : on\n"
                else: md+= "🔸 Auto Reject : off\n"
                if wait["read"] == True: md+="🔹 Auto read : on\n"
                else: md+="🔸 Auto read : off\n"
                if wait["autoinvite"] == True: md+="🔹 Auto invite : on\n"
                else: md+="🔸 Auto invite : off\n"
                if wait["AutoJoin"] == True: md+="🔹 Auto join : on\n"
                else: md +="🔸 Auto join : off\n"
                if wait["Contact"] == True: md+="🔹 Contact : on\n"
                else: md+="🔸 Contact : off\n"
                cl.sendText(msg.to,"「Status」\n"+md)
#--------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
#-------------------------------------------------------
            elif msg.text in ["Set"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, 'I can see u siders (｀・ω・´)\n\n%s' % (datetime.datetime.now().strftime('%H:%M')))
                print "Cek sider"

            elif msg.text in ["Sider"]:
                lurkGroup = ""
                dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "•"
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\n\n%i users have seen at the lastseen point(｀・ω・´) \n\n%s' % (len(dataResult), datetime.datetime.now().strftime('%H:%M'))
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, 'There is no sider (｀・ω・´)\n\n%s' % (datetime.datetime.now().strftime('%H:%M')))
                        print "Result Sider"
#-----------------------------------------------------
            elif "Wl" in msg.text:
                print "Whitelist excuting"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                     if target not in admin:
                      if target not in wait["blacklist"]:
                       try:
                          wait["whitelist"][target] = True
                          f=codecs.open('st2__b.json','w','utf-8')
                          json.dump(wait["whitelist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                          cl.sendText(msg.to,"Dimasukan dalam whitelist")
                       except:
                          cl.sendText(msg.to,"Telah ada dalam whitelist")

            elif "Unwl" in msg.text:
                print "Unwhitelist excuting"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                     if target not in admin:
                      if target not in wait["blacklist"]:
                       try:
                          del wait["whitelist"][target]
                          f=codecs.open('st2__b.json','w','utf-8')
                          json.dump(wait["whitelist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                          cl.sendText(msg.to,"Dihapus dari whitelist.")
                       except:
                          cl.sendText(msg.to,"Tidak ada dalam whitelist")

            elif msg.text in ["White list"]:
                if wait["whitelist"] == {}:
                    cl.sendText(msg.to,"The whitelist is empty")
                else:
                    mc = ""
                    for mi_d in wait["whitelist"]:
                      mc += "• " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"「 WhiteList 」\n" + mc +"Total whitelist : "+ str(len(wait["whitelist"])))
                    print "[Command]Whitelist executed"

            elif msg.text in ["Clear wl"]:
                cl.sendText(msg.to,"Clearing whitelist "+ str(len(wait["whitelist"]))+ " users")
                wait["whitelist"] = {}
                cl.sendText(msg.to,"Clear whitelist done")
#---------------------------------------------------------
            elif "Gname on" in msg.text:
                if msg.to in wait['name']:
                    cl.sendText(msg.to,"Gname on 􀜁􀆚Hare Krishna􏿿")
                else:
                    cl.sendText(msg.to,"Already On 􀜁􀆚Hare Krishna􏿿")
                    wait['name'][msg.to] = True
                    wait['Gname'][msg.to] = cl.getGroup(msg.to).name
            elif "Gname off" in msg.text:
                if msg.to in wait['name']:
                    cl.sendText(msg.to,"Gname off 􀜁􀆚Hare Krishna􏿿")
                    del wait['name'][msg.to]
                else:
                    cl.sendText(msg.to,"Already On 􀜁􀆚Hare Krishna􏿿")
#----------------------------------------------------------
            elif msg.text in ["Read on"]:
              wait["read"] = True
              cl.sendText(msg.to,"Auto Read on")

            elif msg.text in ["Read off"]:
              wait["read"] = False
              cl.sendText(msg.to,"Auto Read off")
#---------------------------------------------------------
            elif msg.text in ["Ban"]:
                print "[Ban]ok"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                     if target not in admin:
                      if target not in wait["whitelist"]:
                       try:
                          wait["blacklist"][target] = True
                          f=codecs.open('st2__b.json','w','utf-8')
                          json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                          cl.sendText(msg.to,"Ban Succes")
                       except:
                          cl.sendText(msg.to,"Telah ada dalam blacklist")

            elif msg.text in ["Unban"]:
                print "[Unban]ok"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Unban Succes")
                   except:
                      cl.sendText(msg.to,"Tidak ada dalam blacklist")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak ada yang terdaftar dalam blacklist")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "• " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"「 Blacklist User 」\n" + mc +"\nTotal : "+ str(len(wait["blacklist"])))

            elif msg.text in ["Clear ban"]:
                cl.sendText(msg.to,"Clearing Ban "+ str(len(wait["blacklist"]))+ " users")
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Done 􀜁􀆚Hare Krishna􏿿")
#--------------------------------------------------------
            elif "Kill " in msg.text:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    print mentionees
                    for mention in mentionees:
                        cl.kickoutFromGroup(msg.to,[mention['M']])
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#-----------------KICK BY MID-----------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                if midd not in admin:
                    cl.kickoutFromGroup(msg.to,[midd])
#-----------------INVITE BY MID-----------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["Cancel invtation"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
#-------------------------------------------------------
            elif "Rename:" in msg.text:
                    string = msg.text.replace("Rename:","")
                    if len(string.decode('utf-8')) <= 20000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Set displayname <"+string+"> Success")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
            elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendText(msg.to,"「 Friendlist 」\n"+ap+"Total : "+str(len(anl)))
#---------------------------------------------------------
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#--------------------------------------------------------
            elif msg.text in ["Self Like"]:
                try:
                    print "activity"
                    url = cl.activity(limit=1)
                    print url
                    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
                    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Auto Like by TΣΔM SLΔCҜβΩT\n\nhttp://line.me/ti/p/~fuck.you__")
                    cl.sendText(msg.to, "Success~")
                except Exception as E:
                    try:
                        cl.sendText(msg.to,str(E))
                    except:
                        pass
#--------------------------------------------------------
            elif msg.text in ["Speed"]:
                start = time.time()
                cl.sendText(msg.to, "Loading...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s detik" % (elapsed_time))
#--------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
#--------------------------------------------------------
            elif msg.text in ["Backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to,"Success backup profile 􀜁􀆚Hare Krishna􏿿")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
            elif "Copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
                group = cl.getGroup(msg.to)
                for contact in group.members:
                    cname = cl.getContact(contact.mid).displayName
                    if cname == _name:
                        cl.CloneContactProfile(contact.mid)
                        cl.sendText(msg.to, "Success~")
                    else:
                        pass
#----------------------------------------------------
            elif "Copy pict @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy pict @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.clonePictureProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Picture profile")
                                except Exception as e:
                                    print e                                    
            elif "Copy cover @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy cover @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneCoverProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Cover profile")
                                except Exception as e:
                                    print e                                
            elif "Copy name @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy name @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneNameProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Name profile")
                                except Exception as e:
                                    print e  
            elif "Copy bio @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy bio @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneStatusProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Bio profile")
                                except Exception as e:
                                    print e
#---------------------------------------------------------
            elif "Id: " in msg.text:
              msgg = msg.text.replace('Id: ','')
              conn = cl.findContactsByUserid(msgg)
              msg.contentType = 13
              msg.contentMetadata = {'mid': conn.mid}
              cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
              cl.sendMessage(msg)
#---------------------------------------------------------
            elif "Yt " in msg.text:
                key = msg.text.replace("Yt ","")
                r=requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyDIb5SdetT4XEYbNOEMcnFG_-ZxhEjrqI0&part=snippet&order=relevance&maxResults=5&q="+key+"&type=video")
                data=r.text
                data=json.loads(data)
                for a in data.get('items', []):
                    if a['id']['kind'] == 'youtube#video':
                        hasil = a['snippet']['title'],a['id']['videoId']
                        cl.sendText(msg.to, hasil[0]+'\n https://www.youtube.com/watch?v='+hasil[1])
#-------------------------------------------------------
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#-------------------------------------------------
            elif "Kk " in msg.text:
                txt = msg.text.replace("Kk ", "")
                cl.kedapkedip(msg.to,txt)
#-----------------------------------------------------------
            elif "Gpict " in msg.text:
                search = msg.text.replace("Gpict ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#--------------------------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = cl.getContact(linedev.mid)
                        #./linedev/ervan
                        try:
                            cover = cl.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage)
                        cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + mid.pictureStatus)
                        cl.sendImageWithURL(msg.to, cover)
                    else:
                        pass

            elif "Minfo " in msg.text:
                mid = msg.text.replace("Minfo ","")
                anu = cl.getContact(mid)
                try:
                    cover = cl.channel.getCover(mid)
                except:
                    cover = ""
                cl.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n[Mid]:\n" + mid + "\n[BIO]:\n" + anu.statusMessage)
                cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + anu.pictureStatus)
                cl.sendImageWithURL(msg.to, cover)
#--------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#------------------------------------------------------
            elif msg.text in ["Mentionall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                      tagall(msg.to, nama)
                  if jml > 100 and jml < 500:
                      for i in range(0,99):
                          nm1 += [nama[i]]
                      tagall(msg.to, nm1)
                      for j in range(100, len(nama)-1):
                          nm2 += [nama[j]]
                      tagall(msg.to, nm2)
                      for k in range(200, len(nama)-1):
                          nm3 += [nama[k]]
                      tagall(msg.to, nm3)
                      for l in range(300, len(nama)-1):
                          nm4 += [nama[l]]
                      tagall(msg.to, nm4)
                      for m in range(400, len(nama)-1):
                          nm5 += [nama[m]]
                      tagall(msg.to, nm5)
                  cnt = Message()
                  cnt.text = "Done : " + str(jml) +  " Members"
                  cnt.to = msg.to
                  cl.sendMessage(cnt)
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "Done : " + str(jml) +  " Members"
                      cnt.to = msg.to
                      cl.sendMessage(cnt)
#------------------------------------------------------
            elif "Kk " in msg.text.lower():
                txt = msg.text.replace("Kk ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#-----------------------------------------------------
            elif msg.text in ["Waktu","#Waktu"]:
                timeNow = datetime.datetime.now()
                timeHours = datetime.datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : " + inihari.strftime('%H:%M') + " Wib"
                cl.sendText(msg.to, rst)
#----------------------------------------------------
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, "「INFO NetStat」\n\n" + botKernel)
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, "「INFO SYSTEM」\n\n" + botKernel)
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, "「INFO KERNEL」\n\n" + botKernel)
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, "「INFO CPU」\n\n" + botKernel)
#-----------------------------------------------------------------------
            elif "Pict group " in msg.text:
                saya = msg.text.replace('Pict group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)                
#-----------------------------------------------------
            elif "Cek " in msg.text:
                tanggal = msg.text.replace("Cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#-------------------------------------------------------
            elif "Wiki " in msg.text:
                  try:
                      wiki = msg.text.replace("Wiki ","")
                      wikipedia.set_lang("id")
                      pesan="[ "
                      pesan+=wikipedia.page(wiki).title
                      pesan+=" ]\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=5)
                      pesan+="\n[ "
                      pesan+=wikipedia.page(wiki).url
                      pesan+=" ]"
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#--------------------------------------------------------
            elif msg.text in ["Runtime"]:
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
#-------------------------------------------------------
            elif "Steal pict" in msg.text:
                 if msg.toType == 2:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            print e
#--------------------------------------------------------
            elif "Steal cover" in msg.text:
                 if msg.toType == 2:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            print e
#--------------------------------------------------------
            elif "Steal vid" in msg.text:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                  for target in targets:
                      try:
                          contact = cl.getContact(target)
                          path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                          cl.sendVideoWithURL(msg.to, path)
                      except Exception as e:
                          print e
#--------------------------------------------------------
            elif "Steal gpict" in msg.text:
              group = cl.getGroup(msg.to)
              path = ("http://dl.profile.line-cdn.net/" + group.pictureStatus)
              cl.sendImageWithURL(msg.to, path)
#---------------------------------------------------------
            elif msg.text in ["Invite on"]:
                if wait["autoinvite"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Auto invite On 􀜁􀆚Hare Krishna􏿿")
                else:
                    wait["autoinvite"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto invite On 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Invite off"]:
                if wait["autoinvite"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Auto invite Off 􀜁􀆚Hare Krishna􏿿")
                else:
                    wait["autoinvite"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto invite Off 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
#-------------------------------------------------------
            elif msg.text in ["Autoreject on"]:
                if wait["autoreject"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"Autoreject On 􀜁􀆚Hare Krishna􏿿")
                else:
                    wait["autoreject"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoreject On 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"already on 􀜁􀆚Hare Krishna􏿿")
            elif msg.text in ["Autoreject off"]:
                if wait["autoreject"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"Autoreject Off 􀜁􀆚Hare Krishna􏿿")
                else:
                    wait["autoreject"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoreject Off 􀜁􀆚Hare Krishna􏿿")
                    else:
                        cl.sendText(msg.to,"Already off 􀜁􀆚Hare Krishna􏿿")
#-----------------------------------------------------
            elif "Vkick" in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                        cl.inviteIntoGroup(msg.to,[target])
                                        cl.cancelGroupInvitation(msg.to,[target])
                                    except:
                                        cl.sendText(msg.to, "Error")
#-------------------------------------------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                cl.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ko " in msg.text:
                nk0 = msg.text.replace("Tr-ko ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ko')
                cl.sendText(msg.to,str(trans))
            elif "Tr-es " in msg.text:
                nk0 = msg.text.replace("Tr-es ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'es')
                cl.sendText(msg.to,str(trans))
            elif "Tr-fr " in msg.text:
                nk0 = msg.text.replace("Tr-fr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'fr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-jw " in msg.text:
                nk0 = msg.text.replace("Tr-jw ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'jw')
                cl.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                cl.sendText(msg.to,str(trans))
            elif "Tr-de " in msg.text:
                nk0 = msg.text.replace("Tr-de ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'de')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ru " in msg.text:
                nk0 = msg.text.replace("Tr-ru ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ru')
                cl.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-hi " in msg.text:
                nk0 = msg.text.replace("Tr-hi ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hi')
                cl.sendText(msg.to,str(trans))
            elif "Tr-vi " in msg.text:
                nk0 = msg.text.replace("Tr-vi ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'vi')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                cl.sendText(msg.to,str(trans))
            elif "Tr-la " in msg.text:
                nk0 = msg.text.replace("Tr-la ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'la')
                cl.sendText(msg.to,str(trans))
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-su " in msg.text:
                nk0 = msg.text.replace("Tr-su ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'su')
                cl.sendText(msg.to,str(trans))
#-------------------------------------------------------
            elif "Steal bio " in msg.text:
                nk0 = msg.text.replace("Steal bio ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    sendMessage(msg.to, "Error")
                    pass
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            y = contact.statusMessage
                            cl.sendText(msg.to,y)
                        except Exception as e:
                            cl.sendText(msg.to, "Error")
                            print e
#-------------------------------------------------------
            elif "Steal name " in msg.text:
                nk0 = msg.text.replace("Steal name ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    sendMessage(msg.to, "Error")
                    pass
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            y = contact.displayName
                            cl.sendText(msg.to,y)
                        except Exception as e:
                            cl.sendText(msg.to, "Error")
                            print e
#--------------------------------------------------------
            elif "Sc: " in msg.text:
                mmid = msg.text.replace("Sc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"                            
#--------------------------------------------------------
            elif "Yt " in msg.text:
                key = msg.text.replace("Yt ","")
                r=requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyDIb5SdetT4XEYbNOEMcnFG_-ZxhEjrqI0&part=snippet&order=relevance&maxResults=5&q="+key+"&type=video")
                data=r.text
                data=json.loads(data)
                for a in data.get('items', []):
                    if a['id']['kind'] == 'youtube#video':
                        hasil = a['snippet']['title'],a['id']['videoId']
                        cl.sendText(msg.to, hasil[0]+'\n https://www.youtube.com/watch?v='+hasil[1])
#---------------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = '「 Music 」\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                  cl.sendText(msg.to, str(njer))
#--------------------------------------------------------
            elif msg.text in ["Restart"]:
                cl.sendText(msg.to, "Restarted 􀜁􀆚Hare Krishna􏿿")
                restart_program()
                print "@Restart"
#--------------------------------------------------------
            
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
