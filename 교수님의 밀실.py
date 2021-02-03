#coding-utf-8

import pygame as pg
from tkinter import*
import tkinter.messagebox as tm
import time
import sys
#import FSP #같은그림찾기 게임파일
#import FM #지뢰찾기 게임파일
#import breakout #벽돌깨기 게임파일
############################################################################

#setup default value
BLACK= (0,0,0)
WHITE= (255,255,255)
BLUE = (0,0,255)
GREEN= (0,255,0)
RED  = (255,0,0)
size = [1000,600]

title = "교수님의 밀실"
btn_position_x1 = size[0]-50  ;  btn_position_y1 = size[1]/2
btn_position_x2 = 30          ;  btn_position_y2 = size[1]/2
btn_position_x3 = size[0]/2   ;  btn_position_y3 = 30
btn_position_x4 = size[0]/2   ;  btn_position_y4 = size[1]-50

ht1_position_x1 = 100         ;  ht1_position_y1 = 100
ht2_position_x1 = 450         ;  ht2_position_y1 = 900
ht3_position_x1 = 100         ;  ht3_position_y1 = 100
ht4_position_x1 = 100         ;  ht4_position_y1 = 100
ht5_position_x1 = 100         ;  ht5_position_y1 = 100
ht6_position_x1 = 100         ;  ht6_position_y1 = 100
ht7_position_x1 = 100         ;  ht7_position_y1 = 100
ht8_position_x1 = 100         ;  ht8_position_y1 = 100
ht9_position_x1 = 0           ;  ht9_position_y1 = 0
ht10_position_x1 = 100        ;  ht10_position_y1 = 100
ht11_position_x1 = 0          ;  ht11_position_y1 = 0
ht12_position_x1 = 0          ;  ht12_position_y1 = 0
ht13_position_x1 = 0          ;  ht13_position_y1 = 0
ht14_position_x1 = 0          ;  ht14_position_y1 = 0
ht15_position_x1 = 100        ;  ht15_position_y1 = 100
ht16_position_x1 = 0          ;  ht16_position_y1 = 0
ht17_position_x1 = 100        ;  ht17_position_y1 = 100
ht18_position_x1 = 100        ;  ht18_position_y1 = 100
ht19_position_x1 = 100        ;  ht19_position_y1 = 100
ht20_position_x1 = 100        ;  ht20_position_y1 = 100
ht21_position_x1 = 0          ;  ht21_position_y1 = 0
ht22_position_x1 = 100        ;  ht22_position_y1 = 100
ht23_position_x1 = 100        ;  ht23_position_y1 = 100
ht24_position_x1 = 100        ;  ht24_position_y1 = 100

start = r"start.jpg"#시작화면
start1 = r"start1.jpg"
ad1 = r"class1.jpg"#강의실 1
ad2 = r"class2.jpg"#강의실 2
ad3 = r"class3.jpg"#강의실 3...
ad4 = r"class4.jpg"#강의실 4...
ad5 = r"class5.jpg"#강의실 5...
ad6 = r"class6.jpg"#강의실 6...
ad7 = r"class7.jpg"#강의실 7...
ad8 = r"class8.jpg"#강의실 8...
ad9 = r"class9.jpg"#강의실 9...

hint1 = r"단서1.png"#힌트 1
hint2 = r"단서2.png"#힌트 2
hint3 = r"단서3.png"#힌트 3
hint3m = r"단서3(쪽지).jpg"#힌트 3(쪽지)
hint3m1 = r"단서3(쪽지)1.jpg"
hint4 = r"단서4.png"#힌트 4
hint5 = r"단서5.png"#힌트 5
hint6 = r"단서6.png"#힌트 6
hint7 = r"단서7.png"#힌트 7

hint8 = r"강의실 맨뒤에 있는 기계 수납 사진.jpg"#힌트 8
hint9 = r"교수님 책상 옆 기계 사진.jpg"#힌트 9
#hint10 = r"C:\Users\Samsung\Desktop\Image\assignment\교수님 책상 전체적 사진.jpg"#힌트 10
hint11 = r"교수님 책상사진.jpg"#힌트 11
hint12 = r"기계 확대 사진.jpg"#힌트 12
hint13 = r"노트 사진.jpg"#힌트 13
hint14 = r"노트 찾는 그림 단서 사진.jpg"#힌트 14#
hint15 = r"노트 찾는 그림 단서.png"#힌트 15#
hint16 = r"노트 찾는 단서 있는 컴퓨터 확대 사진.jpg"#힌트 16#
hint17 = r"노트 펼친 단서 찐.png"#힌트 17
hint18 = r"노트 펼친 단서.png"#힌트 18
hint19 = r"노트 펼친 사진.jpg"#힌트 19
hint20 = r"노트.png"#힌트 20
hint21 = r"노트찾는 단서 쪽지 있는 컴퓨터 사진.jpg"#힌트 21#
hint22 = r"수납함 문 열었을때 사진.jpg"#힌트 22
hint23 = r"열쇠 단서.png"#힌트 23
hint24 = r"열쇠 사진.jpg"#힌트 24
hint25 = r"lock.jpg"
hint26 = r"table_open.jpg"
hint27 = r"table_close.jpg"
com = r"com.jpg"
back = r"back.png"
door = r"door.jpg"
lock = r"lock.jpg"
capture = r"capture.png"

out1 = r"1.jpg"
out2 = r"2.jpg"
out3 = r"3.jpg"
out4 = r"4.jpg"
out5 = r"5.jpg"
out6 = r"6.jpg"
out7 = r"7.jpg"
out8 = r"8.jpg"
out9 = r"9.jpg"
out10 = r"1-1.jpg"
out11 = r"1-2.jpg"
out12 = r"3-1.jpg"
out13 = r"3-2.jpg"
out14 = r"3-3.jpg"
out15 = r"3-4.jpg"
out16 = r"3-5.jpg"
out17 = r"5-1.jpg"
out18 = r"5-2.jpg"
out19 = r"5-3.jpg"
out20 = r"5-4.jpg"
out21 = r"6-1.jpg"
out22 = r"6-2.jpg"
out23 = r"8-1.jpg"
out24 = r"8-2.jpg"
out25 = r"8-3.jpg"
out26 = r"8-4.jpg"
out27 = r"8-5.jpg"
out28 = r"8-6.jpg"
out29 = r"9-1.jpg"
out30 = r"9-2.jpg"
out31 = r"9-3.jpg"
out32 = r"9-4.jpg"
out33 = r"9-5.jpg"
out34 = r"9-6.jpg"
out35 = r"9-7.jpg"
out36 = r"10.jpg"##
out37 = r"10-1.jpg"
out38 = r"10-2.jpg"

global hintImage
hintImage = 0

bglist = [
    [ad5,ad6,ad9],
    [ad4,ad3,ad8],
    [ad2,ad1,ad7],
    [hint8,hint8,door]
]
bglist2 = [
    out1,out2,out3,out4,out5,out6,out7,out8,out9,out36,out37
]

hintlist = [
    ad9,hint9,hint12,hint13,hint18,hint19
]
hintlist2 = [
    ad9,hint11
]
hintlist3 = [
    ad9,hint27,hint26,hint3m
]
hintlist4 = [
    hint8,hint22,hint24
]
hintlist5 = [
    door,lock
]
hintlist6 = [
    out1,out10,out11
]
hintlist7 = [
    out3,out12,out13,out14
]
hintlist8 = [
    out3,out15,out16
]
hintlist9 = [
    out5,out17,out18,out19,out20
]
hintlist10 = [
    out6,out21,out22
]
hintlist11 = [
    out8,out23,out25
]
hintlist12 = [
    out8,out26,out28
]
hintlist13 = [
    out9,out29,out30
]
hintlist14 = [
    out9,out31,out33,out34,out35
]
######################################################################################

#setup pygame
pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption(title)
clock= pg.time.Clock()
########################################################################################

class BackGround():
    def __init__(self,position_x,position_y,width,height,color):
        rect = pg.Rect((position_x, position_y), (width, height))
        pg.draw.rect(screen, color, rect)
        
class Image():
    def __init__(self,position_x,position_y,adress):
        self.position_x = position_x
        self.position_y = position_y
        self.img = pg.image.load(adress)#.convert_alpha()
        screen.blit(self.img, (self.position_x,self.position_y))
    def width(self):
        width = self.img.get_width()
        return width
    def height(self):
        height = self.img.get_width()
        return height

class Search():
    def __init__(self):
        label1 = Label(t, text = "무엇을 검색하시겠습니까?")
        global entry1
        t.geometry("400x400")
        entry1 = Entry(t)
        btn1 = Button(t, text = "Search", bd = 5, command = Get)
        label1.pack()
        entry1.pack()
        btn1.pack()
class Note():
    def __init__(self):
        label1 = Label(s,text = "몇페이지를 펼칠까요?")
        global entry2
        entry2 = Entry(s)
        btn1 = Button(s, text = "open", bd = 5, command = Open)
        label1.pack()
        entry2.pack()
        btn1.pack()
def Get():
    result = str(entry1.get())
    if "게임" == result:
        s = Toplevel(t)
        #btn1 = Button(s,text = "지뢰찾기",command = F)
        #btn2 = Button(s,text = "같은그림",command = G)
        #btn3 = Button(s,text = "벽돌깨기",command = H)
        btn1.pack()
        btn2.pack()
        btn3.pack()
    else:
        tm.showinfo("info", "다시 검색해보세요!")
#def F():
    #FM.prepareWindow()
    #FM.prepareGame()
    #FM.window.mainloop()
#def G():
    #FSP.main()
#def H():
    #br = breakout.Breakout()
    #br.main()

def Open():
    global note
    result = int(entry2.get())
    if 122 == result:
        note = True
    else:
        tm.showinfo("info", "다시 입력하세요")
#######################################################################################

#Main Event Loop
if __name__ == "__main__":
    Image(0,0,start1)
    current_Image = [0,0]
    hintImage1 = 0
    hintImage2 = 0
    hintImage3 = 0
    hintImage4 = 0
    hintImage5 = 0
    hintImage6 = 0
    hintImage7 = 0
    hintImage8 = 0
    hintImage9 = 0
    hintImage10 = 0
    hintImage11 = 0
    hintImage12 = 0
    hintImage13 = 0
    hintImage14 = 0
    hintImage15 = 0
    page = 0
    pr = 0
    p = 0
    done = True
    note = False
    app = False
    app1 = False
    app2 = False
    app3 = False
    app4 = False
    app5 = False
    app6 = False
    app7 = False
    key1 = False
    key2 = False
    key3 = False
    while done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
############################################################################################# 
    #event controll
        if True == app:
            Image(850,70,hint23)
        if True == key1:
            Image(920,70,hint15)
        if True == key2:
            Image(850,150,hint17)
        if True == key3:
            Image(920,150,hint3m1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=False
            #When you let go of the left mouse button in the area of a button, the button does something.
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if 0 == p:
                        if (600 < event.pos[0] < 900) and (190 < event.pos[1] < 330):
                            p = 1
                            Image(0,0,start)
                    #clicked right button
                    if (btn_position_x1 < event.pos[0] < btn_position_x1 + btn_1.width()) and (btn_position_y1 < event.pos[1] < btn_position_y1 + btn_1.height()):
                        print("btn clicked!")
                        if current_Image[1] < 2:
                            hintImage1 = 0
                            hintImage2 = 0
                            hintImage3 = 0
                            hintImage4 = 0
                            hintImage5 = 0
                            current_Image[1] += 1
                            Image(0,0,bglist[current_Image[0]][current_Image[1]])

                    #clicked left button
                    if (btn_position_x2 < event.pos[0] < btn_position_x2 + btn_2.width()) and (btn_position_y2 < event.pos[1] < btn_position_y2 + btn_2.height()):
                        print("btn clicked!")
                        if current_Image[1] > 0:
                            hintImage1 = 0
                            hintImage2 = 0
                            hintImage3 = 0
                            hintImage4 = 0
                            hintImage5 = 0
                            current_Image[1] -= 1
                            Image(0,0,bglist[current_Image[0]][current_Image[1]])

                    #clicked up button
                    if (btn_position_x3 < event.pos[0] < btn_position_x3 + btn_3.width()) and (btn_position_y3 < event.pos[1] < btn_position_y3 + btn_3.height()):
                        print("btn clicked!")
                        if current_Image[0] > 0:
                            hintImage1 = 0
                            hintImage2 = 0
                            hintImage3 = 0
                            hintImage4 = 0
                            hintImage5 = 0
                            current_Image[0] -= 1
                            Image(0,0,bglist[current_Image[0]][current_Image[1]])
                            
                    #clicked down button
                    if (btn_position_x4 < event.pos[0] < btn_position_x4 + btn_4.width()) and (btn_position_y4 < event.pos[1] < btn_position_y4 + btn_4.height()):
                        print("btn clicked!")
                        if current_Image[0] < 3:
                            hintImage1 = 0
                            hintImage2 = 0
                            hintImage3 = 0
                            hintImage4 = 0
                            hintImage5 = 0
                            current_Image[0] += 1
                            Image(0,0,bglist[current_Image[0]][current_Image[1]])
                    #################################################################
                    #start

                    #hint in class2
                    if 2 == current_Image[0] and 0 == current_Image[1]:
                        if (70 < event.pos[0] < 250) and (300 < event.pos[1] < 550):
                            print("Game Start!")
                            Image(ht21_position_x1,ht21_position_y1,hint21)
                            hintImage = 16
                    if 16 == hintImage:
                        if (500 < event.pos[0] < 710) and (350 < event.pos[1] < 550):
                            Image(ht16_position_x1,ht16_position_y1,hint16)
                            hintImage = 14
                    if 14 == hintImage:
                        if (535 < event.pos[0] < 610) and (320 < event.pos[1] < 410):
                            ht14 = Image(ht14_position_x1,ht14_position_y1,hint14)
                            hintImage = 0
                            key1 = True
                    #hint in class9
                    if (0 == hintImage1) and (0 == hintImage2) and (0 == hintImage3):
                        pr = 0

                    if 0 == pr:
                        if 0 == current_Image[0] and 2 == current_Image[1]:
                            if (380 < event.pos[0] < 520) and (175 < event.pos[1] < 500):
                                hintImage1 = 1
                                Image(ht9_position_x1,ht9_position_y1,hintlist[hintImage1])
                                page = 1
                                pr = 1
                            elif (630 < event.pos[0] < 800) and (250 < event.pos[1] < 400):
                                hintImage2 = 1
                                Image(ht11_position_x1,ht11_position_y1,hintlist2[hintImage2])
                                page = 2
                                pr = 1
                            elif (150 < event.pos[0] < 490) and (50 < event.pos[1] < 175):
                                hintImage3 = 1
                                Image(0,0,hintlist3[hintImage3])
                                page = 3
                                pr = 1

                    elif 1 == pr:
                        if 1 == page:
                            if 0 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (380 < event.pos[0] < 520) and (175 < event.pos[1] < 500):
                                        hintImage1 = 1
                                        Image(ht9_position_x1,ht9_position_y1,hintlist[hintImage1])
                            elif 1 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (490 < event.pos[0] < 610) and (300 < event.pos[1] < 420):
                                        hintImage1 = 2
                                        Image(0,0,hintlist[hintImage1])
                            elif 2 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (240 < event.pos[0] < 570) and (290 < event.pos[1] < 400):
                                        hintImage1 = 3
                                        Image(0,0,hintlist[hintImage1])
                            elif 3 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (400 < event.pos[0] < 600) and (100 < event.pos[1] < 500):
                                        hintImage1 = 4
                                        Image(0,0,hintlist[hintImage1])
                            elif 4 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (300 < event.pos[0] < 700) and (100 < event.pos[1] < 500):
                                        s = Tk()
                                        Note()
                                        s.mainloop()
                                        hintImage1 = 5
                            elif 5 == hintImage1:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if True == note:
                                        Image(0,0,hintlist[hintImage1])
                                        key2 = True
                        if 2 == page:
                            pass
                        if 3 == page:
                            if 0 == hintImage3:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (150 < event.pos[0] < 490) and (50 < event.pos[1] < 175):
                                        hintImage3 = 1
                                        Image(0,0,hintlist3[hintImage3])
                                        page = 3
                            if 1 == hintImage3:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (150 < event.pos[0] < 850) and (100 < event.pos[1] < 500):
                                        hintImage3 = 2
                                        Image(0,0,hintlist3[hintImage3])
                            if 2 == hintImage3:
                                if 0 == current_Image[0] and 2 == current_Image[1]:
                                    if (440 < event.pos[0] < 560) and (240 < event.pos[1] < 360):
                                        hintImage3 = 3
                                        Image(0,0,hintlist3[hintImage3])
                                        key3 = True

                    #hint in class 3
                    if 1 == current_Image[0] and 1 == current_Image[1]:
                        if (780 < event.pos[0] < 1000) and (365 < event.pos[1] < 580):
                            t = Tk()
                            Search()
                            t.mainloop()
                        elif (0 < event.pos[0] < 230) and (365 < event.pos[1] < 580):
                            Image(0,0,capture)
                    # key hint
                    if 0 == hintImage4:
                        if 3 == current_Image[0]:
                            if (190 < event.pos[0] < 250) and (245 < event.pos[1] < 305):
                                hintImage4 = 1
                                Image(0,0,hintlist4[hintImage4])
                            
                    if 1 == hintImage4:
                        if 3 == current_Image[0]:
                            if (300 < event.pos[0] < 375) and (350 < event.pos[1] < 420):
                                print("getted key!")
                                hintImage4 = 2
                                Image(0,0,hintlist4[hintImage4])
                                app = True

                    #hint in door
                    if 0 == hintImage5:
                        if 3 == current_Image[0] and 2 == current_Image[1]:
                            if (730 < event.pos[0] < 800) and (300 < event.pos[1] < 410):
                                hintImage5 = 1
                                Image(0,0,hintlist5[hintImage5])
                    if 1 == hintImage5:
                        if 3 == current_Image[0] and 2 == current_Image[1]:
                            if (540 < event.pos[0] < 640) and (100 < event.pos[1] < 500):
                                if True == app:
                                    print("Escape!")
                                    done = False

                    ## back key
                    if (20 < event.pos[0] < 20 + bk.width()) and (20 < event.pos[1] < 20 + bk.height()):    
                        if 3 == current_Image[0]:#############error check
                            if 0 < hintImage4:
                                hintImage4 -= 1
                                Image(0,0,hintlist4[hintImage4])
                        
                        if 3 == current_Image[0] and 2 == current_Image[1]:
                            if 0 < hintImage5:
                                hintImage5 -= 1
                                Image(0,0,hintlist5[hintImage5])
                        if 0 == current_Image[0] and 2 == current_Image[1]:
                            if 1 == page: 
                                if 0 < hintImage1:
                                    hintImage1 -= 1
                                    Image(0,0,hintlist[hintImage1])
                            if 2 == page:
                                if 0 < hintImage2:
                                    hintImage2 -= 1
                                    Image(0,0,hintlist2[hintImage2])
                            if 3 == page:
                                if 0 < hintImage3:
                                    hintImage3 -= 1
                                    Image(0,0,hintlist3[hintImage3])

        btn_1 = Image(btn_position_x1,btn_position_y1,r"C:\Users\Samsung\Desktop\Image\assignment\right.png")
        btn_2 = Image(btn_position_x2,btn_position_y2,r"C:\Users\Samsung\Desktop\Image\assignment\left.png")
        btn_3 = Image(btn_position_x3,btn_position_y3,r"C:\Users\Samsung\Desktop\Image\assignment\up.png")
        btn_4 = Image(btn_position_x4,btn_position_y4,r"C:\Users\Samsung\Desktop\Image\assignment\down.png")
        bk = Image(20,20,back)
        pg.display.flip()
    #################################################################
    
    #escape the class
    done = True
    current_Image = 0
    o1 = Image(0,0,out1)
    page = 0
    page1 = 0
    page2 = 0
    pr = 0
    pr1 = 0
    pr2 = 0
    while done:
        clock.tick(10)
        if True == app1:
            Image(850,70,hint1)
        if True == app2:
            Image(920,70,hint2)
        if True == app3:
            Image(850,150,hint3)
        if True == app4:
            Image(920,150,hint4)
        if True == app5:
            Image(850,230,hint6)
        if True == app6:
            Image(920,230,hint5)
        if True == app7:
            Image(850,310,hint7)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=False
            
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    #clicked right button
                    if (btn_position_x1 < event.pos[0] < btn_position_x1 + btn_1.width()) and (btn_position_y1 < event.pos[1] < btn_position_y1 + btn_1.height()):
                        print("btn clicked!")
                        if 10 > current_Image:
                            hintImage7 = 0
                            hintImage8 = 0
                            hintImage11 = 0
                            hintImage12 = 0
                            hintImage13 = 0
                            hintImage14 = 0
                            current_Image += 1
                            Image(0,0,bglist2[current_Image])

                    #clicked left button
                    if (btn_position_x2 < event.pos[0] < btn_position_x2 + btn_2.width()) and (btn_position_y2 < event.pos[1] < btn_position_y2 + btn_2.height()):
                        print("btn clicked!")
                        if 0 < current_Image:
                            hintImage7 = 0
                            hintImage8 = 0
                            hintImage11 = 0
                            hintImage12 = 0
                            hintImage13 = 0
                            hintImage14 = 0
                            current_Image -= 1
                            Image(0,0,bglist2[current_Image])
                    ###################################################################

                    #hint in out1
                    if 0 == hintImage6:
                        if 0 == current_Image:
                            if (700 < event.pos[0] < 810) and (350 < event.pos[1] < 450):
                                hintImage6 = 1
                                Image(0,0,hintlist6[hintImage6])

                    if 1 == hintImage6:
                        if 0 == current_Image:
                            if (460 < event.pos[0] < 540) and (150 < event.pos[1] < 350):
                                hintImage6 = 2
                                Image(0,0,hintlist6[hintImage6])

                    if 2 == hintImage6:
                        if 0 == current_Image:
                            if (250 < event.pos[0] < 600) and (100 < event.pos[1] < 400):
                                app1 = True#out1 hint 1-2

                    #hint in out3
                    if (0 == hintImage7) and (0 == hintImage8):
                        pr = 0
                    if 0 == pr:
                        if 0 == hintImage7:
                            if 2 == current_Image:
                                if (800 < event.pos[0] < 900) and (240 < event.pos[1] < 390):
                                    pr=1
                                    page = 1
                                    hintImage7 = 1
                                    Image(0,0,hintlist7[hintImage7])
                        if 0 == hintImage8:
                            if 2 ==current_Image:
                                if (200 < event.pos[0] < 430) and (150 < event.pos[1] < 320):
                                    pr =1
                                    page = 2
                                    hintImage8 = 1
                                    Image(0,0,hintlist8[hintImage8])
                    elif 1 == pr:
                        if 1 == page:
                            if 0 == hintImage7:
                                if 2 == current_Image:
                                    if (800 < event.pos[0] < 900) and (240 < event.pos[1] < 390):
                                        hintImage7 = 1
                                        Image(0,0,hintlist7[hintImage7])
                            if 1 == hintImage7:
                                if 2 == current_Image:
                                    if (450 < event.pos[0] < 700) and (450 < event.pos[1] < 580):
                                        hintImage7 = 2
                                        Image(0,0,hintlist7[hintImage7])
                            if 2 == hintImage7:
                                if 2 == current_Image:
                                    if (230 < event.pos[0] < 700) and (70 < event.pos[1] < 500):
                                        hintImage7 = 3
                                        Image(0,0,hintlist7[hintImage7])
                            if 3 == hintImage7:
                                if 2 == current_Image:
                                    if (200 < event.pos[0] < 560) and (140 < event.pos[1] < 450):
                                        app2 = True
                        if 2 == page:
                            if 1 == hintImage8:
                                if 2 == current_Image:
                                    if (800 < event.pos[0] < 930) and (70 < event.pos[1] < 540): 
                                            hintImage8 = 2
                                            Image(0,0,hintlist8[hintImage8])

                    #hint in out5
                    if 0 == hintImage9:
                        if 4 == current_Image:
                            if (730 < event.pos[0] < 900) and (240 < event.pos[1] < 580):
                                hintImage9 = 1
                                Image(0,0,hintlist9[hintImage9])
                    if 1 == hintImage9:
                        if 4 == current_Image:
                            if (80 < event.pos[0] < 330) and (240 < event.pos[1] < 550):
                                hintImage9 = 2
                                Image(0,0,hintlist9[hintImage9])
                    if 2 == hintImage9:
                        if 4 == current_Image:
                            if (600 < event.pos[0] < 750) and (200 < event.pos[1] < 400):
                                hintImage9 = 3
                                Image(0,0,hintlist9[hintImage9])
                    if 3 == hintImage9:
                        if 4 == current_Image:
                            if (500 < event.pos[0] < 650) and (350 < event.pos[1] < 500):
                                hintImage9 = 4
                                Image(0,0,hintlist9[hintImage9])
                    if 4 == hintImage9:
                        if 4 == current_Image:
                            if (200 < event.pos[0] < 700) and (150 < event.pos[1] < 450):
                                app3 = True

                    #hint in out6
                    if 0 == hintImage10:
                        if 5 == current_Image:
                            if (70 < event.pos[0] < 200) and (200 < event.pos[1] < 540):
                                hintImage10 = 1
                                Image(0,0,hintlist10[hintImage10])
                    if 1 == hintImage10:
                        if 5 == current_Image:
                            if (250 < event.pos[0] < 500) and (70 < event.pos[1] < 530):
                                hintImage10 = 2
                                Image(0,0,hintlist10[hintImage10])
                    if 2 == hintImage10:
                        if 5 == current_Image:
                            if (200 < event.pos[0] < 600) and (110 < event.pos[1] < 450):
                                app4 = True

                    #hint in out8
                    if (0 == hintImage11) and (0 == hintImage12):
                        pr1 = 0
                    if 0 == pr1:
                        if 0 == hintImage11:
                            if 7 == current_Image:
                                if (100 < event.pos[0] < 500) and (100 < event.pos[1] < 300):
                                    pr1 = 1
                                    hintImage11 = 1
                                    Image(0,0,hintlist11[hintImage11])
                                    page1 = 1
                                elif (740 < event.pos[0] < 935) and (50 < event.pos[1] < 330):
                                    pr1 = 1
                                    hintImage12 = 1
                                    Image(0,0,hintlist12[hintImage12])
                                    page1 = 2
                    elif 1 == pr1:
                        if 1 == page1:   
                            if 0 == hintImage11:
                                if 7 == current_Image:
                                    if (100 < event.pos[0] < 500) and (100 < event.pos[1] < 300):
                                        hintImage11 = 1
                                        Image(0,0,hintlist11[hintImage11])
                            if 1 == hintImage11:
                                if 7 == current_Image:
                                    if (550 < event.pos[0] < 760) and (220 < event.pos[1] < 330):
                                        hintImage11 = 2
                                        Image(0,0,hintlist11[hintImage11])
                                        print("click")
                            if 2 == hintImage11:
                                if 7 == current_Image:
                                    if (385 < event.pos[0] < 750) and (180 < event.pos[1] < 500):
                                        app5 = True
                                        print("click")
                        if 2 == page1:
                            if 0 == hintImage12:
                                if 7 == current_Image:
                                    if (740 < event.pos[0] < 935) and (50 < event.pos[1] < 330):
                                        hintImage12 = 1
                                        Image(0,0,hintlist12[hintImage12])
                            if 1 == hintImage12:
                                if 7 == current_Image:
                                    if (100 < event.pos[0] < 250) and (400 < event.pos[1] < 540):
                                        hintImage12 = 2
                                        Image(0,0,hintlist12[hintImage12])


                    #hint in out9
                    if (0 == hintImage13) and (0 == hintImage14):
                        pr2 = 0
                    if 0 == pr2:
                        if 0 == hintImage13:
                            if 8 == current_Image:
                                if (100 < event.pos[0] < 200) and (300 < event.pos[1] < 400):
                                    pr2 = 1
                                    hintImage13 = 1
                                    Image(0,0,hintlist13[hintImage13])
                                    page2 = 1
                                elif (300 < event.pos[0] < 890) and (100 < event.pos[1] < 430):
                                    pr2 = 1
                                    hintImage14 = 1
                                    Image(0,0,hintlist14[hintImage14])
                                    page2 = 2
                    elif 1 == pr2:
                        if 1 == page2:   
                            if 0 == hintImage13:
                                if 8 == current_Image:
                                    if (100 < event.pos[0] < 200) and (300 < event.pos[1] < 400):
                                        hintImage13 = 1
                                        Image(0,0,hintlist13[hintImage13])
                            if 1 == hintImage13:
                                if 8 == current_Image:
                                    if (400 < event.pos[0] < 600) and (150 < event.pos[1] < 450):
                                        hintImage13 = 2
                                        Image(0,0,hintlist13[hintImage13])
                            if 2 == hintImage13:
                                if 8 == current_Image:
                                    if (300 < event.pos[0] < 600) and (130 < event.pos[1] < 450):
                                        app6 = True
                        if 2 == page2:
                            if 0 == hintImage14:
                                if 8 == current_Image:
                                    if (300 < event.pos[0] < 890) and (100 < event.pos[1] < 430):
                                        hintImage14 = 1
                                        Image(0,0,hintlist14[hintImage14])
                            if 1 == hintImage14:
                                if 8 == current_Image:
                                    if (60 < event.pos[0] < 130) and (80 < event.pos[1] < 540):
                                        hintImage14 = 2
                                        Image(0,0,hintlist14[hintImage14])
                            if 2 == hintImage14:
                                if 8 == current_Image:
                                    if (250 < event.pos[0] < 600) and (100 < event.pos[1] < 530):
                                        hintImage14 = 3
                                        Image(0,0,hintlist14[hintImage14])
                            if 3 == hintImage14:
                                if 8 == current_Image:
                                    if (350 < event.pos[0] < 550) and (100 < event.pos[1] < 300):
                                        hintImage14 = 4
                                        Image(0,0,hintlist14[hintImage14])
                            if 4 == hintImage14:
                                if 8 == current_Image:
                                    if (265 < event.pos[0] < 580) and (190 < event.pos[1] < 370):
                                        app7 = True

                    if 10 == current_Image:
                        if (250 < event.pos[0] < 580) and (50 < event.pos[1] < 550):
                            if True == app7:
                                done = False

                    #back key button#            
                    if (20 < event.pos[0] < 20 + bk.width()) and (20 < event.pos[1] < 20 + bk.height()):
                        if 0 ==current_Image:
                            if 0 < hintImage6:
                                hintImage6 -= 1
                                Image(0,0,hintlist6[hintImage6])
                             
                        if 2 == current_Image:
                            if 1 == page:
                                if 0 < hintImage7:
                                    hintImage7 -= 1
                                    Image(0,0,hintlist7[hintImage7])
                            if 2 == page:
                                if 0 < hintImage8:
                                    hintImage8 -= 1
                                    Image(0,0,hintlist8[hintImage8])
                        if 4 == current_Image:
                            if 0 < hintImage9:
                                hintImage9 -= 1
                                Image(0,0,hintlist9[hintImage9])
                        if 5 == current_Image:
                            if 0 < hintImage10:
                                hintImage10 -= 1
                                Image(0,0,hintlist10[hintImage10])
                        if 7 == current_Image:
                            if 1 == page1:
                                if 0 < hintImage11:
                                    hintImage11 -= 1
                                    Image(0,0,hintlist11[hintImage11])
                            if 2 == page1:
                                if 0 < hintImage12:
                                    hintImage12 -= 1
                                    Image(0,0,hintlist12[hintImage12])
                        if 8 == current_Image:
                            if 1 == page2:
                                if 0 < hintImage13:
                                    hintImage13 -= 1
                                    Image(0,0,hintlist13[hintImage13])
                            if 2 == page2:
                                if 0 < hintImage14:
                                    hintImage14 -= 1
                                    Image(0,0,hintlist14[hintImage14])

        btn_1 = Image(btn_position_x1,btn_position_y1,r"C:\Users\Samsung\Desktop\Image\assignment\right.png")
        btn_2 = Image(btn_position_x2,btn_position_y2,r"C:\Users\Samsung\Desktop\Image\assignment\left.png")
        bk = Image(20,20,back)
        pg.display.flip()
    done = True
    while done:
        clock.tick(10)
        Image(0,0,out38)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=False
            
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    done = False
        pg.display.flip()
    pg.quit()
    