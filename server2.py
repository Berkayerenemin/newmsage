import socket 
import threading 
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverRunning = True 
ip = "127.0.0.1" 
port = 25566 

app = {}
app["anaoda"] = {}
con = []

s.bind((ip, port)) #Sunucu belirtilen ip ve porta bağlandı.
s.listen() 
print("Sunucu Hazır...") 
print("Sunucu ip adresi::%s"%ip)

def foo():
    numberroom = list(app.keys())
    name = list(app["anaoda"].keys())
    msg4 ="\n".join(numberroom)
    msg6="\n".join(name) 
    client.send("MSAGE Güncelleniyor...".encode("utf8"))
    client.send(msg4.encode("utf8"))
    client.send(msg6.encode("utf8")) 
    threading.Timer(100, foo).start()

def hall(client, username, app):
    clientConnected = True
    

    while clientConnected:
        msg = client.recv(1024).decode("utf8")
        msg2 = str(username)+":"+msg 
        name = list(app["anaoda"].keys())
        print(app["anaoda"].items)

        try:
            for k,v in app["anaoda"].items():
                v.send(msg2.encode("utf8"))           
            
            if "**online" in msg: 
                msg2="\n".join(name) 
                client.send(msg2.encode("utf8")) 
            
            if "**yenioda" in msg:
                client.send("Yeni odanın adını yazınız".encode("utf8"))  
                newroomname = client.recv(1024).decode("utf8")
                app[newroomname] = {}
                app["anaoda"].pop(username)
                print(app)
                roomConnected = True
                room(client, username, app, roomConnected, newroomname)
            
            if "**odasayisi" in msg:
                numberroom = list(app.keys())
                msg4 ="\n".join(numberroom)
                client.send(msg4.encode("utf8"))

            if "**odayagir" in msg:
                client.send("Gireceğiniz odanın adını söyleyiniz.".encode("utf8"))
                joinedroom = client.recv(1024).decode("utf8")
                numberroom2 = list(app.keys())
                if joinedroom in numberroom2:
                    app["anaoda"].pop(username)
                    roomConnected = True
                    joinroom(client, username, app, roomConnected, joinedroom)
                else:
                    client.send("Böyle bir oda bulunamadı".encode("utf8"))
            
            if "**quit" in msg:
                app["anaoda"].pop(username)
                msg78 ="\n".join(name) 
                bb = "Aramızdan biri ayrıldı."
                for i in con:
                    print(i)
                    i.send(bytes(bb,"utf8"))
                    i.send(msg78.encode("utf8"))
                client.close()
                clientConnected = False

        except:
            print("Hata")
        

def room(client, username, app, roomConnected, newroomname):

    while roomConnected:
        app[newroomname][username] = client
        msgroom = client.recv(1024).decode("utf8")
        msg2room = str(username)+":"+msgroom
        nameroom = list(app[newroomname].keys())
        try:
            for x,y in app[newroomname].items():
                y.send(msg2room.encode("utf8"))

            if "**online" in msgroom: 
                msg2room="\n".join(nameroom)
                client.send(msg2room.encode("utf8")) 

            if "**odasayisi" in msgroom:
                numberroom = list(app.keys())
                msg4 ="\n".join(numberroom)
                client.send(msg4.encode("utf8"))

            if "**odadançık" in msgroom:
                app[newroomname].pop(username)
                app["anaoda"][username] = client
                roomConnected = False
                hall(client, username, app)


        except:
            print("Oda hatası")

def joinroom(client, username, app, roomConnected, joinedroom):

    while roomConnected:
        app[joinedroom][username] = client
        msgroom2 = client.recv(1024).decode("utf8")
        msg2room2 = str(username)+":"+msgroom2
        nameroom2 = list(app[joinedroom].keys())
        try:
            for t,k in app[joinedroom].items():
                k.send(msg2room2.encode("utf8"))

            if "**online" in msg: 
                msg2room2="\n".join(nameroom2)
                client.send(msg2room2.encode("utf8")) 

            if "**odasayisi" in msgroom:
                numberroom = list(app.keys())
                msg4 ="\n".join(numberroom)
                client.send(msg4.encode("utf8"))

            if "**odadançık" in msgroom:
                app[newroomname].pop(username)
                app["anaoda"][username] = client
                roomConnected = False
                hall(client, username, app)

        except:
            print("Oda hatası")

while serverRunning:
    client, address =  s.accept()
    username = client.recv(1024).decode("utf8")
    numberroom = list(app.keys())
    msg7 ="\n".join(numberroom)
    client.send(msg7.encode("utf8"))
    print("%s sunucuya giriş yaptı"%str(username))
    con.append(client)

    if username not in app["anaoda"].keys():
        app["anaoda"][username] = client
        name = list(app["anaoda"].keys())
        msg77="\n".join(name) 
        client.send(msg77.encode("utf8")) 
        print(app["anaoda"])
        time.sleep(1)
        print(app["anaoda"][username])
        aa = "Sunucuda yeni arkadaşlar var!"
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        for i in con:
            print(i)
            i.send(bytes(aa,"utf8"))
            i.send(msg77.encode("utf8"))
            print("xxxxyaptıxxxxx")
        #client.send(msg77.encode("utf8"))
        time.sleep(5)
        client.send("Herhangi bir zorluk yaşadığın zaman **yardım komutu ile yardım alabilirsin!".encode("utf8"))
        threading.Thread(target = hall, args = (client, username, app)).start()

    else:
        client.send("Böyle bir kullanıcı bulunmakta başka bir isim seç.")
