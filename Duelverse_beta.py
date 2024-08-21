from tkinter import *
import sqlite3 as sq
from tkinter.ttk import Notebook
from PIL import Image, ImageTk
import random
from tkinter import ttk
def arenagenerate():
    global board,Buttons,terraincontrast,terraingeneration,terraingenerationlikelyhood,terrainneighbourcount,pstat
    if plist[0] != "" and plist[1] != "":
        terraincontrast = random.randint(5, 6) #these are the recomended values if you want them you can change them but it will impact the game
        board = [["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""],
                ["","","","","","","","","","","","","","","","","",""]]
        for l in range (0,len(board[0])):
            board[len(board)-1][l] = "s"
        for p2 in reversed(range (1,7)):
            for p3 in range (1,17):
                terrainneighbourcount = 0
                terraingenerationlikelyhood = 0
                if board[p2-1][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                if board[p2-1][p3] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2-1][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                if board[p2][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                terraingenerationlikelyhood = terrainneighbourcount / terraincontrast
                terraingeneration = random.randint(0, 1000)
                if terraingeneration <= terraingenerationlikelyhood * 1000:
                    board[p2][p3] = "g"
            for p2 in reversed(range (1,7)):
                for p3 in range (1,17):
                    terrainneighbourcount = 0
                    if board[p2-1][p3] != "":
                        terrainneighbourcount = terrainneighbourcount + 1 
                    if board[p2][p3-1] != "":
                        terrainneighbourcount = terrainneighbourcount + 1 
                    if board[p2][p3+1] != "":
                        terrainneighbourcount = terrainneighbourcount + 1 
                    if board[p2+1][p3] != "":
                        terrainneighbourcount = terrainneighbourcount + 1 
                    if terrainneighbourcount == 4:
                        board[p2][p3] = "g" 
        for p2 in reversed(range (1,7)):
            for p3 in range (1,17):
                terrainneighbourcount = 0
                if board[p2-1][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                if board[p2-1][p3] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2-1][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                if board[p2][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3-1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3] != "":
                    terrainneighbourcount = terrainneighbourcount + 1 
                if board[p2+1][p3+1] != "":
                    terrainneighbourcount = terrainneighbourcount + 1
                if terrainneighbourcount == 0:
                    terraingenerationlikelyhood = random.randint(0, terraincontrast-1)
                    if terraingenerationlikelyhood == 1:    
                        board[p2][p3] = "f"
        startcycle()
        boardupdate()
        actionupdate()
        pstat = -1
        pchange()
        buttonnumber = 0
        for i1 in range ( 0,8 ):
            for i2 in range ( 0,16 ):
                Buttons[buttonnumber].place ( x = (i2*buttonsize)+320, y = i1*buttonsize, width = buttonsize, height = buttonsize )
                buttonnumber = buttonnumber + 1
        battlecard.place ( x = 0, y = 0, width = 320, height = 320)
        endturn.place ( x = 1605, y = 810, width = 810, height = 120)
        arenadeletebutton.place ( x = 1605, y = 940, width = 250, height = 120)
        arenageneratebutton.place ( x = 19835, y = 480, width = 250, height = 120)
        logobtn.place ( x = 19835, y = 280, width = 450, height = 200)
        upbtn.place ( x = 1425, y = 900, width = 75, height = 75)
        downbtn.place ( x = 1425, y = 975, width = 75, height = 75)
        leftbtn.place ( x = 1350, y = 975, width = 75, height = 75)
        rightbtn.place ( x = 1500, y = 975, width = 75, height = 75)
        cancelbtn.place ( x = 1350, y = 900, width = 75, height = 75)
        selectbtn.place ( x = 1500, y = 900, width = 75, height = 75)
        gcyclecount.place(x = 1350,y=825,width = 225,height= 50)
        chchoose4.place ( x = 1055500, y = 450, width = 150, height = 150)
        chchoose3.place ( x = 805550, y = 450, width = 150, height = 150)
        chchoose2.place ( x = 655500, y = 450, width = 150, height = 150)
        chchoose1.place ( x = 405550, y = 450, width = 150, height = 150)
        chcancel.place ( x = 43227 + 200*(playercount-1), y = 650, width = 75, height = 75)
        status1.place ( x = 150, y = 525, width = 85, height = 25)
        status2.place ( x = 235, y = 525, width = 85, height = 25)
        status3.place ( x = 150, y = 550, width = 85, height = 25)
        status4.place ( x = 235, y = 550, width = 85, height = 25)
        pstatnum.place ( x = 100, y = 350, width = 120, height = 50)
        statbc.place ( x = 0, y = 425, width = 150, height = 150)
        ultstat.place(x=245, y=475)
        energystat.place(x=245, y=450)
        healthstat.place(x=245, y=425)
        energystat2.place ( x = 150, y = 450, width = 95, height = 25)
        healthstat2.place ( x = 150, y = 425, width = 95, height = 25)
        ultstat2.place ( x = 150, y = 475, width = 95, height = 25)
        attackstat.place ( x = 150, y = 500, width = 85, height = 25)
        defstat.place ( x = 235, y = 500, width = 85, height = 25)
def boardupdate():
    for l in range (0,len(Buttons)):
        if board[l//16][(l%16)+1] == "s":
            Buttons[l].config(image = stone)
        if board[l//16][(l%16)+1] == "g":
            Buttons[l].config(image = grass)
            if l//16 >0:
                if board[(l//16)-1][(l%16)+1] == "g":
                    Buttons[l].config(image = dirt)    
        if board[l//16][(l%16)+1] == "f":
            Buttons[l].config(image = platform)
            if l//16 <= 1:
                Buttons[l].config(image = cloud)     
        if board[l//16][(l%16)+1] == "":
            Buttons[l].config(image = air)
        if board[l//16][(l%16)+1] == "p1":
            skinsearch(l,0)
            name1.place(x = (l%16*buttonsize)+345, y = (l//16)*buttonsize)
            if pcycle ==0:
                name1.config(bg="gray")   
            else:
                name1.config(bg = "white") 
        if board[l//16][(l%16)+1] == "p2":
            skinsearch(l,1)
            name2.place(x = (l%16*buttonsize)+345, y = (l//16)*buttonsize)
            if pcycle ==1:
                name2.config(bg="gray")  
            else:
                name2.config(bg = "white")   
        if board[l//16][(l%16)+1] == "p3":
            skinsearch(l,2)
            name3.place(x = (l%16*buttonsize)+345, y = (l//16)*buttonsize)
            if pcycle ==2:
                name3.config(bg="gray")  
            else:
                name3.config(bg = "white")   
        if board[l//16][(l%16)+1] == "p4":
            skinsearch(l,3)
            name4.place(x = (l%16*buttonsize)+345, y = (l//16)*buttonsize)
            if pcycle ==3:
                name4.config(bg="gray")  
            else:
                name4.config(bg = "white")   
def skinsearch(l,p):
    for i in range(len(matchlist1)):
        if matchlist1[i] == plist[p]:
            Buttons[l].config(image = matchlist2[i][pside[p]])
            

    
def startcycle():
    global plist,playercount
    startplaceselect(1)
    startplaceselect(2)
    if playercount >= 3:
        startplaceselect(3)
        if playercount == 4:
            startplaceselect(4)
def startplaceselect(i):
    whileexit = 0
    while whileexit == 0:
        x = random.randint(1, 17)
        y = random.randint(0, 6)
        if (board[y+1][x] == "g" or board[y+1][x] == "g") and board[y][x] == "":
            board[y][x] = ("p" + str(i))
            whileexit = 1
def cycleend():
    global pcycle,gcycle,pstat
    if pcycle < playercount-1:
        pcycle = pcycle + 1
    else:
        pcycle = 0
        gcycle = gcycle+1
        gcyclecount.config(text = "Global Cycles Survived - " + str(gcycle))
    actionupdate()
    markcancel()
    boardupdate()
    pstat = pcycle
    pstat = pstat-1
    pchange()
def actionupdate():
    if skills[0] == "basic":
        skillbutton1.place ( x = 610, y = 850, width = 200, height = 200)
        skillbutton1.config(image = moveimg)
        skillbutton2.place ( x = 860, y = 850, width = 200, height = 200)
        skillbutton2.config(image = mineimg)
        skillbutton3.place ( x = 1110, y = 850, width = 200, height = 200)
        skillbutton3.config()
        charachterbc.config(image = matchlist2[matchlist1.index(plist[pcycle])][2])
        charachterbc.place ( x = 370, y = 850, width = 150, height = 150)
        pname.config(text = "P" + str(pcycle+1) + "-" + pnames[pcycle])
        pname.place ( x = 407, y = 813, width = 75, height = 25)
def skill1():
    boardupdate()
    pointshow(2,0,0,"move",0)
def skill2():
    boardupdate()
    pointshow(1,1,0,"mine",0)
def skill3():
    boardupdate()
def pointshow(r,w,p,s,c):
    global markx,marky,markchangex,markchangey,markchangelimit,thoughplayers,thoughwalls,currentskill
    for x1 in range(1,17):    
        for y1 in range(0,8):
            if board[y1][x1] == ("p" + str(pcycle+1)):
                markx = x1
                marky = y1
                markchangex = 0
                markchangey = 0
                if c == 1:
                    cancelbtn.config(command = no)
                    skillbutton1.config(command = no)
                    skillbutton2.config(command = no)
                    skillbutton3.config(command = no)
                thoughwalls = w
                thoughplayers = p
                markchangelimit = r
                currentskill = s
                Buttons[marky*16+(markx-1)].config(image = skillpoint)
def markw():
    global markx,marky,markchangex,markchangey
    if marky > 0 and markchangey > (0-markchangelimit):
        if thoughwalls == 0:
            if board[marky-1][markx] != "" and board[marky-1][markx] != "p1" and board[marky-1][markx] != "p2" and board[marky-1][markx] != "p3" and board[marky-1][markx] != "p4":
                marky = marky+1
                markchangey = markchangey+1
        marky = marky-1
        markchangey = markchangey-1        
        boardupdate()
        Buttons[marky*16+(markx-1)].config(image = skillpoint)
def marks():
    global markx,marky,markchangex,markchangey
    if marky < 7 and markchangey < markchangelimit:
        if thoughwalls == 0:
            if board[marky+1][markx] != "" and board[marky+1][markx] != "p1" and board[marky+1][markx] != "p2" and board[marky+1][markx] != "p3" and board[marky+1][markx] != "p4":
                marky = marky-1
                markchangey = markchangey-1 
        marky = marky+1
        markchangey = markchangey+1
        boardupdate()
        Buttons[marky*16+(markx-1)].config(image = skillpoint)    
def marka():
    global markx,marky,markchangex,markchangey
    if markx > 1 and markchangex > (0-markchangelimit):
        if thoughwalls == 0:
            if board[marky][markx-1] != "" and board[marky][markx-1] != "p1" and board[marky][markx-1] != "p2" and board[marky][markx-1] != "p3" and board[marky][markx-1] != "p4":
                markx = markx+1
                markchangex = markchangex+1
        markx = markx-1
        markchangex = markchangex-1
        sidecheck()
        boardupdate()
        Buttons[marky*16+(markx-1)].config(image = skillpoint)     
def markd():
    global markx,marky,markchangex,markchangey
    if markx < 16 and markchangex < markchangelimit:
        if thoughwalls == 0:
            if board[marky][markx+1] != "" and board[marky][markx+1] != "p1" and board[marky][markx+1] != "p2" and board[marky][markx+1] != "p3" and board[marky][markx+1] != "p4":
                markx = markx-1
                markchangex = markchangex-1
        markx = markx+1
        markchangex = markchangex+1
        sidecheck()
        boardupdate()
        Buttons[marky*16+(markx-1)].config(image = skillpoint)
def sidecheck():
    if markchangex > 0:
        pside[pcycle] = 1
    if markchangex < 0:
        pside[pcycle] = 0
    boardupdate()
def markteleport():
    for l in range (0,len(Buttons)):
        if board[l//16][(l%16)+1] == ("p" + str(pcycle+1)):
            board[l//16][(l%16)+1] = ""
    board[marky][markx] = ("p" + str(pcycle+1))
    fallcheck()
    markcancel()
def fallcheck():
    for p in range (1,5):
        for q in range (0,10):
            for l in range (0,len(Buttons)):
                if board[l//16][(l%16)+1] == ("p" + str(p)):
                    if board[l//16+1][(l%16)+1] == "":
                        board[l//16][(l%16)+1] = ""
                        board[l//16+1][(l%16)+1] = ("p" + str(p))   
def markmine():
    if board[marky][markx] == "g":
        board[marky][markx] = ""
        fallcheck()
        markcancel()
        pointshow(2,0,0,"place",1)
def markplace():
    board[marky][markx] = "g"
    markcancel()
def no():
    print("no")
def markconfirm():
    if (board[marky][markx] == "p1" or board[marky][markx] == "p2"  or board[marky][markx] == "p3"  or board[marky][markx] == "p4") == (thoughplayers == 1):
        if currentskill == "move":
            markteleport()
        if currentskill == "place":
            markplace()
        if currentskill == "mine":
            markmine()    
def markcancel():
    global markx,marky,markchangex,markchangey,markchangelimit,thoughplayers,thoughwalls,currentskill
    boardupdate()
    markx = 0
    marky = 0
    markchangex = 0
    markchangey = 0
    thoughwalls = 0
    thoughplayers = 0
    markchangelimit = 0  
    currentskill = "" 
    cancelbtn.config(command = markcancel)     
    skillbutton1.config(command = skill1)
    skillbutton2.config(command = skill2)
    skillbutton3.config(command = skill3)          
def arenadelete():
    global gcycle,pcycle
    buttonnumber = 0
    pcycle = 0
    for i1 in range ( 0,8 ):
        for i2 in range ( 0,16 ):
            Buttons[buttonnumber].place ( x = (i2*buttonsize)+16000, y = i1*buttonsize, width = buttonsize, height = buttonsize )
            buttonnumber = buttonnumber + 1
    battlecard.place ( x = 10000, y = 0, width = 320, height = 800)
    arenadeletebutton.place ( x = 19835, y = 480, width = 250, height = 120)   
    arenageneratebutton.place ( x = 800, y = 880, width = 250, height = 120) 
    logobtn.place ( x = 0, y = 0, width = 450, height = 200)
    skillbutton1.place ( x = 11610, y = 850, width = 200, height = 200)
    skillbutton2.place ( x = 11860, y = 850, width = 200, height = 200)
    skillbutton3.place ( x = 111110, y = 850, width = 200, height = 200)
    charachterbc.place ( x = 5110, y = 150, width = 150, height = 150)
    endturn.place ( x = 16015, y = 940, width = 810, height = 120)
    upbtn.place ( x = 142225, y = 850, width = 75, height = 75)
    downbtn.place ( x = 142225, y = 925, width = 75, height = 75)
    leftbtn.place ( x = 135220, y = 925, width = 75, height = 75)
    rightbtn.place ( x = 152200, y = 925, width = 75, height = 75)
    cancelbtn.place ( x = 122350, y = 850, width = 75, height = 75)
    selectbtn.place ( x = 122500, y = 850, width = 75, height = 75)
    chchoose4.place ( x = 1000, y = 450, width = 150, height = 150)
    chchoose3.place ( x = 800, y = 450, width = 150, height = 150)
    chchoose2.place ( x = 600, y = 450, width = 150, height = 150)
    chchoose1.place ( x = 400, y = 450, width = 150, height = 150)
    chcancel.place ( x = 437 + 200*(playercount-1), y = 650, width = 75, height = 75)
    name4.place ( x = 10000, y = 350, width = 50, height = 20)
    name3.place ( x = 10000, y = 350, width = 50, height = 20)
    name2.place ( x = 10000, y = 350, width = 50, height = 20)
    name1.place ( x = 10000, y = 350, width = 50, height = 20)
    gcyclecount.place(x = 0,y = 19000)
    pname.place ( x = 10000, y = 350, width = 120, height = 20)
    status1.place ( x = 15110, y = 525, width = 85, height = 25)
    status2.place ( x = 23115, y = 525, width = 85, height = 25)
    status3.place ( x = 15110, y = 550, width = 85, height = 25)
    pstatnum.place ( x = 10110, y = 350, width = 120, height = 50)
    status4.place ( x = 23115, y = 550, width = 85, height = 25)
    statbc.place ( x = 0, y = 42522, width = 150, height = 150)
    energystat2.place ( x = 12250, y = 450, width = 95, height = 25)
    gcycle = 1
    ultstat.place(x=2425, y=475)
    energystat.place(x=2425, y=450)
    healthstat.place(x=2425, y=425)
    healthstat2.place ( x = 150, y = 42225, width = 95, height = 25)
    ultstat2.place ( x = 12250, y = 475, width = 95, height = 25)
    attackstat.place ( x = 12250, y = 500, width = 85, height = 25)
    defstat.place ( x = 235, y = 50220, width = 85, height = 25)
def chchange(p):
    global playercount
    if plist[p] != "dog" and plist[p] != "":
        plist[p] = matchlist1[matchlist1.index(plist[p])+1]
    else:
        if plist[p] == "dog":
            plist[p] = "mozg"
    if plist[p] == "":
        if playercount == p:
            playercount = playercount + 1
            print(playercount)
            plist[p] = "mozg"
    playersupdate()
def playersupdate():
    if plist[0] != "":
        chchoose1.config(image = matchlist2[matchlist1.index(plist[0])][2])
    else:
        chchoose1.config(image = nobc)
    if plist[1] != "":
        chchoose2.config(image = matchlist2[matchlist1.index(plist[1])][2])
    else:
        chchoose2.config(image = nobc)
    if plist[2] != "":
        chchoose3.config(image = matchlist2[matchlist1.index(plist[2])][2])
    else:
        chchoose3.config(image = nobc)
    if plist[3] != "":
        chchoose4.config(image = matchlist2[matchlist1.index(plist[3])][2])
    else:
        chchoose4.config(image = nobc)
    chcancel.place ( x = 437 + 200*(playercount-1), y = 650, width = 75, height = 75)
def chremove():
    global playercount
    plist[playercount-1] = ""
    playercount = playercount-1
    print(playercount)
    playersupdate()
def pchange():
    global pstat
    if pstat+1 < playercount:
        pstat = pstat+1
    else:
        pstat = 0
    pstatnum.config(text = "P" + str(pstat+1) + "-" + pnames[pstat])
    healthstat['value'] = (phealth[pstat] / pmaxhealth[pstat]) * 100
    energystat['value'] = (penergy[pstat] / pmaxenergy[pstat]) * 100
    ultstat['value'] = (pult[pstat] / 10) * 100
    healthstat2.config(text = "HP-" + str(phealth[pstat]))
    energystat2.config(text = "MANA-" + str(penergy[pstat]))
    ultstat2.config(text = "CHARGE-" + str(pult[pstat])+ "/" + str(10))
    statbc.config(image = matchlist2[matchlist1.index(plist[pstat])][2])
    attackstat.config(text = "ATK-" + str(pattack[pstat]))
    defstat.config(text = "DEF-" + str(pdef[pstat]))
    status1.config(text = "❤️" + str(pstatus[pstat][0][0]) + "("+str(pstatus[pstat][0][1])+ ")")
    status2.config(text = "⚡" + str(pstatus[pstat][1][0]) + "("+str(pstatus[pstat][1][1])+ ")")
    status3.config(text = "⚔️" + str(pstatus[pstat][2][0]) + "("+str(pstatus[pstat][2][1])+ ")")
    status4.config(text = "🛡️" + str(pstatus[pstat][3][0]) + "("+str(pstatus[pstat][3][1])+ ")")
board = [["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""],
        ["","","","","","","","","","","","","","","","","",""]]
root = Tk()
root.geometry("1920x1080")
root.config(bg="brown")
Buttons = []
buttonsize = 100
buttonnumber = 0
playercount = 0
terrainneighbourcount = 0
terraingenerationlikelyhood = 0
markx = 0
marky = 0
markchangex = 0
markchangey = 0
markchangelimit = 0
thoughwalls = 0
thoughplayers = 0
currentskill = ""  
pstat = 0
gcycle = 1
phealth = [100,100,100,100]
pmaxhealth = [100,100,100,100]
penergy = [100,100,100,100]
pmaxenergy = [100,100,100,100]
pult = [0,0,0,0]
pdef = [0,0,0,0]
pattack = [0,0,0,0]
pstatus = [[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]]] #healing/poisoning,enegrized/tired,strong/weak,tough/fragile, duration
pnames = ["mozg","babyyoda","tel","kagero"]
plist = ["","","",""]
pstatnum = Button ( root,text = "P" + str(pstat+1) + "-" + pnames[pstat],command = pchange)
pstatnum.place ( x = 11100, y = 350, width = 120, height = 50)
statbc = Label ( root,image = "")
statbc.place ( x = 0, y = 42225, width = 150, height = 150)
s = ttk.Style()
s.theme_use('clam')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
healthstat = ttk.Progressbar(root,orient='horizontal', style="green.Horizontal.TProgressbar",mode='determinate',length=75)
healthstat.place(x=24335, y=425)
healthstat['value'] = (phealth[pstat] / pmaxhealth[pstat]) * 100
healthstat2 = Label ( root,text = "HP-" + str(phealth[pstat]))
healthstat2.place ( x = 15220, y = 425, width = 95, height = 25)
s = ttk.Style()
s.theme_use('clam')
s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
energystat = ttk.Progressbar(root,orient='horizontal', style="blue.Horizontal.TProgressbar",mode='determinate',length=75)
energystat.place(x=23345, y=450)
energystat['value'] = (penergy[pstat] / pmaxenergy[pstat]) * 100
energystat2 = Label ( root,text = "ENERGY-" + str(penergy[pstat]))
energystat2.place ( x = 15220, y = 450, width = 95, height = 25)
s = ttk.Style()
s.theme_use('clam')
s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
ultstat = ttk.Progressbar(root,orient='horizontal', style="yellow.Horizontal.TProgressbar",mode='determinate',length=75)
ultstat.place(x=24335, y=475)
ultstat['value'] = (pult[pstat] / 10) * 100
ultstat2 = Label ( root,text = "CHARGE-" + str(pult[pstat])+ "/" + str(10))
ultstat2.place ( x = 15220, y = 475, width = 95, height = 25)
attackstat = Label ( root,text = "ATK-" + str(pattack[pstat]))
attackstat.place ( x = 150, y = 50220, width = 85, height = 25)
defstat = Label ( root,text = "DEF-" + str(pdef[pstat]))
defstat.place ( x = 235, y = 50220, width = 85, height = 25)
status1 = Label ( root,text = "❤️" + str(pstatus[pstat][0][0]) + "("+str(pstatus[pstat][0][1])+ ")")
status1.place ( x = 151110, y = 525, width = 85, height = 25)
status2 = Label ( root,text = "⚡" + str(pstatus[pstat][1][0]) + "("+str(pstatus[pstat][1][1])+ ")")
status2.place ( x = 222235, y = 525, width = 85, height = 25)
status3 = Label ( root,text = "⚔️" + str(pstatus[pstat][2][0]) + "("+str(pstatus[pstat][2][1])+ ")")
status3.place ( x = 11110, y = 550, width = 85, height = 25)
status4 = Label ( root,text = "🛡️" + str(pstatus[pstat][3][0]) + "("+str(pstatus[pstat][3][1])+ ")")
status4.place ( x = 22135, y = 550, width = 85, height = 25)
grass = ImageTk.PhotoImage(Image.open("grass.png"))
dirt = ImageTk.PhotoImage(Image.open("dirt.png"))
stone = ImageTk.PhotoImage(Image.open("stone.png"))
platform = ImageTk.PhotoImage(Image.open("flyingplatform.png"))
air = ImageTk.PhotoImage(Image.open("air.png"))
cloud = ImageTk.PhotoImage(Image.open("cloud.png"))
nobc = ImageTk.PhotoImage(Image.open("nobc.png"))
mozgbc = ImageTk.PhotoImage(Image.open("mozgbc.png"))
mozgleft = ImageTk.PhotoImage(Image.open("mozgleft.png"))
mozgright = ImageTk.PhotoImage(Image.open("mozgright.png"))
yodabc = ImageTk.PhotoImage(Image.open("yodabc.png"))
yodaleft = ImageTk.PhotoImage(Image.open("yodaleft.png"))
yodaright = ImageTk.PhotoImage(Image.open("yodaright.png"))
dogbc = ImageTk.PhotoImage(Image.open("doggobc.png"))
dogleft = ImageTk.PhotoImage(Image.open("doggoleft.png"))
dogright = ImageTk.PhotoImage(Image.open("doggoright.png"))
gearbc = ImageTk.PhotoImage(Image.open("gearmanbc.png"))
gearleft = ImageTk.PhotoImage(Image.open("gearmanleft.png"))
gearright = ImageTk.PhotoImage(Image.open("gearmanright.png"))
moveimg = ImageTk.PhotoImage(Image.open("walkimg.png"))
mineimg = ImageTk.PhotoImage(Image.open("mineimg.png"))
skillpoint = ImageTk.PhotoImage(Image.open("skillpoint.png"))
cancelimg = ImageTk.PhotoImage(Image.open("cancel.png"))
chchoose1 = Button ( root,image = nobc,command = lambda: chchange(0))
chchoose1.place ( x = 400, y = 450, width = 150, height = 150)
chchoose2 = Button ( root,image = nobc,command = lambda: chchange(1))
chchoose2.place ( x = 600, y = 450, width = 150, height = 150)
chchoose3 = Button ( root,image = nobc,command = lambda: chchange(2))
chchoose3.place ( x = 800, y = 450, width = 150, height = 150)
chchoose4 = Button ( root,image = nobc,command = lambda: chchange(3))
chchoose4.place ( x = 1000, y = 450, width = 150, height = 150)
chcancel = Button ( root,image = cancelimg,command = chremove)
chcancel.place ( x = 437, y = 650, width = 75, height = 75)
pside = [random.randint(0, 1),random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)]
skills = ["basic",["move",2,0,0],["mine",1,1,0]] #name,radius,throughwalls,onplayers
skillbutton1 = Button ( root,command = skill1)
skillbutton1.place ( x = 11610, y = 850, width = 200, height = 200)
skillbutton2 = Button ( root,command = skill2)
skillbutton2.place ( x = 11860, y = 850, width = 200, height = 200)
skillbutton3 = Button ( root,command = skill3)
skillbutton3.place ( x = 111110, y = 850, width = 200, height = 200)
gcyclecount = Button ( root, text = "Global Cycles Survived - " + str(gcycle))
gcyclecount.place(x = 10000,y=10000,width = 225,height= 50)
upimg = ImageTk.PhotoImage(Image.open("up.png"))
downimg = ImageTk.PhotoImage(Image.open("down.png"))
leftimg = ImageTk.PhotoImage(Image.open("left.png"))
rightimg = ImageTk.PhotoImage(Image.open("right.png"))
selectimg = ImageTk.PhotoImage(Image.open("confirm.png"))
upbtn = Button ( root,image = upimg,command = markw)
downbtn = Button ( root,image = downimg,command = marks)
leftbtn = Button ( root,image = leftimg,command = marka)
rightbtn = Button ( root,image = rightimg,command = markd)
selectbtn = Button ( root,image = selectimg,command = markconfirm)
cancelbtn = Button ( root,image = cancelimg,command = markcancel)
upbtn.place ( x = 142500, y = 850, width = 75, height = 75)
downbtn.place ( x = 142500, y = 925, width = 75, height = 75)
leftbtn.place ( x = 135000, y = 925, width = 75, height = 75)
rightbtn.place ( x = 150000, y = 925, width = 75, height = 75)
cancelbtn.place ( x = 135000, y = 850, width = 75, height = 75)
selectbtn.place ( x = 150000, y = 850, width = 75, height = 75)
pcycle = 0
matchlist1 = ["mozg","yoda","gear","dog"]
matchlist2 = [[mozgleft,mozgright,mozgbc],[yodaleft,yodaright,yodabc],[gearleft,gearright,gearbc],[dogleft,dogright,dogbc]]
charachterbc = Label ( root,image = "")
charachterbc.place ( x = 111150, y = 150, width = 150, height = 150)
pname = Label ( root,text = "P" + str(pcycle+1) + "-" + pnames[pcycle])
pname.place ( x = 10000, y = 350, width = 120, height = 20)
for i1 in range ( 0,8 ):
        for i2 in range ( 0,16 ):
            Buttons.append (Label(root, text = i1*16+i2, font=( 100)))
            Buttons[buttonnumber].place ( x = (i2*buttonsize)+16000, y = i1*buttonsize, width = buttonsize, height = buttonsize)
            buttonnumber = buttonnumber + 1
name1 = Label ( root,text = pnames[0])
name1.place ( x = 10000, y = 350, width = 50, height = 20)
name2 = Label ( root,text = pnames[1])
name2.place ( x = 10000, y = 350, width = 50, height = 20)
name3 = Label ( root,text = pnames[2])
name3.place ( x = 10000, y = 350, width = 50, height = 20)
name4 = Label ( root,text = pnames[3])
name4.place ( x = 10000, y = 350, width = 50, height = 20)
bc_standart = ImageTk.PhotoImage(Image.open("battlecard_standart.png"))
battlecard = Label ( root,image = bc_standart)
battlecard.place ( x = 11000, y = 0, width = 320, height = 800)
battlbutton = ImageTk.PhotoImage(Image.open("Battlebutton.png"))
leavebutton = ImageTk.PhotoImage(Image.open("leavebutton.png"))
arenageneratebutton = Button ( root,image = battlbutton,command = arenagenerate)
arenageneratebutton.place ( x = 800, y = 880, width = 250, height = 120)
arenadeletebutton = Button ( root,image = leavebutton,command = arenadelete)
arenadeletebutton.place ( x = 19835, y = 480, width = 250, height = 120)
endturn = Button ( root,text = "end turn",command = cycleend)
endturn.place ( x = 16205, y = 940, width = 810, height = 120)
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logobtn = Button ( root,image = logo)
logobtn.place ( x = 0, y = 0, width = 450, height = 200)
root.mainloop()
