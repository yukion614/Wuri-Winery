from cProfile import label
#from tty import setraw
from pygame import mixer
from tkinter import *
import tkinter
import pygame as py
from PIL import Image, ImageTk
import tkinter as tk
import cv2
import threading
import tkinter.simpledialog

global number
#-------------------------------------
import json
 
global setR
global setG
global setB

with open("json/setRGB.json") as f:

    # 讀取 JSON 檔案
    p = json.load(f)

    # 取得 值
    setR=p["setR"]
    setG=p["setG"]
    setB=p["setB"]

class basedesk():
    '''視窗基本設置'''
    def __init__(self,master):
        self.root = master
        self.root.config()
        #self.root.title('base page')
        root.attributes('-fullscreen', True)
        self.root.geometry('1080x1920')

        initface(self.root)##???
      
 
#第一畫面
class initface():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='gray')
        self.initface = tk.Frame(self.master)
        self.initface.pack()
        #背景2
        photo = tk.PhotoImage(file='img/bg_01.png')
        root.photo = photo
        lab =tk.Label(self.initface,width=1080,height=1920,image=photo)##??
        #控制lab顯示
        global t
        t = True
        lab.pack()

        #監控按鈕
        root.bind('n',self.key)
        root.bind('N',self.key)
        root.bind('S',self.setRGB)
        root.bind('s',self.setRGB)

       
        

    def key(self,event):
        #音效
        #mixer.music.load("sound_effect/button-21.mp3")
        #mixer.music.play()
        self.initface.destroy()
        shoot_photo(self.master)
  
    def setRGB(self,event):
        setR = tkinter.simpledialog.askinteger(title= '圖片中R< 輸入數值', prompt='輸入R')
        setG = tkinter.simpledialog.askinteger(title= '圖片中G> 輸入數值', prompt='輸入G')
        setB = tkinter.simpledialog.askinteger(title= '圖片中B< 輸入數值', prompt='輸入B')
        #item[r] < setR and item[g] > setG and item[b] < setB: 
       
    
#拍照畫面====
class shoot_photo():
    def __init__(self,master):
        global cap
        cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap.set(3,1920)
        cap.set(4,1080)
        self.master = master
        self.master.config(bg='orange')
        self.initface = tk.Frame(self.master)
        self.initface.pack()
        play_bgm()
        #倒數**********************

        label =tk.Label(master)
        label.pack()  

        #canvas = Canvas(master,width=1080,height=200,background='black',bd='-3')
        canvas = Canvas(master,width=1080,height=200,bd='-3')
        #canvas.pack()
        canvas.place(x=0,y=0)

        root.bind("n",shoot_photo.keyNN)
        root.bind("N",shoot_photo.keyNN)
        root.bind("b",shoot_photo.keyNN)
        root.bind("B",shoot_photo.keyNN)
        #canvas圖片

       
        self.remaining=8
        
        def countdown(remaining = None):
            if remaining is not None:
                self.remaining = remaining
          
            if self.remaining < 0:
                canvas.destroy()
                shoot_photo.keyNN()
            else:
       
                canvas.create_rectangle(0,0,1080,200,fill='black')
                canvas.create_text(1080/2,80,text="拍照倒數.. %d" % self.remaining,font=('新細明體',50),fill='white')
                self.remaining = self.remaining - 1
           
                root.after(1000, countdown)
        countdown()
        
        
        #監聽
        #root.bind("p", shoot_photo.keyN)
        #root.bind("P", shoot_photo.keyN)

       
        #開啟攝影機
        
        
        def show_frames():
        
            Vshow = cap.read()[1]
            Vshow1 = cv2.rotate(Vshow,cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2image= cv2.cvtColor(Vshow1,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            global imgtk
            imgtk = ImageTk.PhotoImage(image = img)
            
            #label.imgtk = imgtk
            label.configure(image=imgtk)
            #label.configure(image=img)
            if f :
                
                label.after(10, show_frames)
            else:
                label.destroy()
                cap.release()
                self.next()
    
        global f 
        f = True
        global b
        b = None
        



        show_frames()
    

    def keyB(self):
        global b
        b = True
        mixer.music.load("sound_effect/110.mp3")
        mixer.music.play()
        


    def keyNN():
        #音效
        mixer.music.load("sound_effect/110.mp3")
        mixer.music.play()
        global f
        f = False 
        global imgtk
        label.imgtk = imgtk
        file_name = "camera_img/IMG20220201.png"
        imagetk = label.imgtk
        imgpil = ImageTk.getimage( imagetk )
        imgpil.save(file_name, "PNG")
        imgpil.close()
    
    def keyN(event):
        #音效
        mixer.music.load("sound_effect/110.mp3")
        mixer.music.play()
        global f
        f = False 
        global imgtk
        label.imgtk = imgtk
        file_name = "camera_img/IMG20220201.png"
        imagetk = label.imgtk
        imgpil = ImageTk.getimage( imagetk )
        imgpil.save(file_name, "PNG")
        imgpil.close()
     
 
    def back(self):
        self.initface.destroy()
        initface(self.master)
    
    def next(self):
        self.initface.destroy()
        face1(self.master)

#處理中.......
class face1():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='orange')
        self.face1 = tk.Frame(self.master)
        self.face1.pack()
        play_bgm()
        
        #線1=====================
        def fun1():
            
            #創建畫布
            canvas =  Canvas(root,width=1080,height=1920,bd=0)
            bi =tkinter.PhotoImage(file='img/bg_02.png')
            root.bi = bi
            canvas.create_image(0,0,image=bi,anchor=NW)
            #canvas.pack(padx=0,pady=0)
                
            #轉圈
            frameCnt = 8
            frames = [PhotoImage(file='img/run.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

            
            def update(ind):

                frame = frames[ind]
                ind += 1
                if ind == frameCnt:
                    ind = 0
                canvas.create_image(400,1000,anchor=NW,image=frame)
                #終止條件
                if go == None:
                   
                    root.after(100, update, ind)

                if go:
                    
                    #one_thread.join()
                    canvas.destroy()
                    self.next()
    
            #處理中文字
            
            canvas.create_text(900,5000,text='處理中....',font=('Noto Sans CJK TC Black Black',60),fill='white')
            run = canvas
            run.place(x=0,y=0)
            root.after(0, update, 0)

        #線2=====================　去背
        def fun2():
            global go
            camra_pic = Image.open( "camera_img/IMG20220201.png")#相機照片
            source_pic1 = Image.open('souce_img/s_img01.png')#背景照片
            source_pic2 = Image.open('souce_img/s_img02.png')#背景照片
            source_pic3 = Image.open('souce_img/s_img03.png')#背景照片
            source_pic4 = Image.open('souce_img/s_img04.png')#背景照片
            def keys_effect(img):
                img = img.convert('RGBA')#??
                newImage = []
                for item in img.getdata():
            
                    r,g,b = 0,1,2
                    '''綠色'''
                    #if item[r] < 22 and item[g] > 110 and item[b] < 200: 
                    #    newImage.append((248,248,246,0))
                    '''綠色'''
                    if item[r] < setR and item[g] > setG and item[b] < setB: 
                        newImage.append((248,248,246,0))
                            
                    else:
                        newImage.append(item)
                img.putdata(newImage)

                return img

            def overlay():
                fore = keys_effect( camra_pic )
                
                #1
                source_pic1.paste(fore,mask = fore)
                source_pic1.save(f'save/resize_out1.png')
                #2
                source_pic2.paste(fore,mask = fore)
                source_pic2.save(f'save/resize_out2.png')
                #3
                source_pic3.paste(fore,mask = fore)
                source_pic3.save(f'save/resize_out3.png')
                #4
                source_pic4.paste(fore,mask = fore)
                source_pic4.save(f'save/resize_out4.png')
            
            overlay()
            
            go = True


        one_thread = threading.Thread(target=fun1)
        two_thread = threading.Thread(target=fun2)
 
        one_thread.start()
        two_thread.start()
       
        #run
        global go
        go = None
        
    def next(self):
        self.face1.destroy()
        face2(self.master)
        
#選照片
class face2():
    def __init__(self,master):
        self.master = master
        global count
        count = 0
        play_bgm()
        
        '''讀取照片'''
        '''1'''
        global img_1,img_2,img_3,img_4
        img1 = tkinter.PhotoImage(file='save/resize_out1.png')
        img_1 = img1.subsample(2,2)#小2倍
        img__1 = img1.subsample(5,5)#小5倍
        root.img1 = img1
        root.img__1 = img__1
    
        img2 = tkinter.PhotoImage(file='save/resize_out2.png')
        img_2 = img2.subsample(2,2)
        img__2 = img2.subsample(5,5)#小5倍
        root.img2 = img2
        root.img__2 = img__2
    
        img3 = tkinter.PhotoImage(file='save/resize_out3.png')
        img_3 = img3.subsample(2,2)
        img__3 = img3.subsample(5,5)#小5倍
        root.img3 = img3
        root.img__3 = img__3
 
        img4 = tkinter.PhotoImage(file='save/resize_out4.png')
        img_4 = img4.subsample(2,2)
        img__4 = img4.subsample(5,5)#小5倍
        root.img4 = img4
        root.img__4 = img__4
     
        bg_img = tkinter.PhotoImage(file='img/show.png')
        root.bg_img = bg_img
        self.canvas = Canvas(master,width=1080,height=1920)
        
        self.background = self.canvas.create_image(0,0,anchor=NW,image = bg_img)

        '''上方選單照片'''
        self.img_menu1 = self.canvas.create_image(450,200,anchor=NW,image = img__1)

        self.img_menu2 = self.canvas.create_image(750,200,anchor=NW,image = img__2)
    
        self.img_menu3 = self.canvas.create_image(1050,200,anchor=NW,image = img__3)
      
        self.img_menu4 = self.canvas.create_image(1350,200,anchor=NW,image = img__4)

        '''半透明'''
        img_b = tk.PhotoImage(file='img/show-b.png')
        root.img_b = img_b
        self.canvas.create_image(0,0,anchor=NW,image = img_b)

        '''左右箭頭'''
        img_left = tk.PhotoImage(file='img/btn_l.png')
        root.img_left = img_left
        self.canvas.create_image(150,300,anchor=NW,image = img_left)

        img_right = tk.PhotoImage(file='img/btn_r.png')
        root.img_right = img_right
        self.canvas.create_image(700,300,anchor=NW,image = img_right)
  

        #中間 主要
        #self.rextangle_main = self.canvas.create_rectangle(40,220,280,580,fill='blue')
        
        self.canvas.pack(anchor='center')



        #監控按鈕
        root.bind('d',self.r_next)
        root.bind('D',self.r_next)
        root.bind('a',self.r_back)
        root.bind('A',self.r_back)
        
        root.bind('n',self.choose)
        root.bind('N',self.choose)
        root.bind('b',self.return_page)
        root.bind('B',self.return_page)

        #中間 主要
        '''設定按鈕畫面'''
        global btm_main
        btm_main = tkinter.Button(self.canvas , text='主畫面',image=img_1,command=self.next_page)
        #Canvas.create_image(0,0,image=img_1)
        btm_main.place(x=260,y=800)
        
#按鈕事件
    def r_back(self,event):
        self.back()
    def r_next(self,event):
        self.next()
    def choose(self,event):
        self.next_page()
    def return_page(self,event):
        self.back_page()


 
    def back( self):
        
        global count
        if count < 0 :
            count += 1

        #音效
        #mixer.music.load("sound_effect/button-21.mp3")
        #mixer.music.play()
    
        if count != 0:
            #移動指令           被移動的物件      移動的x ,y 
            self.canvas.move(self.img_menu1, 1 ,0)
            self.canvas.move(self.img_menu2, 1 ,0)
            self.canvas.move(self.img_menu3, 1 ,0)
            self.canvas.move(self.img_menu4, 1 ,0)
        

        if count == 0:
            btm_main = Button(self.canvas , text='主畫面',image=img_1,command=self.next_page)
            btm_main.place(x=260,y=800)
        if count == -300:
            btm_main2 = Button(self.canvas , text='主畫面',image=img_2,command=self.next_page)
            btm_main2.place(x=260,y=800)
        if count == -600:
            btm_main = Button(self.canvas , text='主畫面',image=img_3,command=self.next_page)
            btm_main.place(x=260,y=800)
        if count == -900:
            btm_main = Button(self.canvas , text='主畫面',image=img_4,command=self.next_page)
            btm_main.place(x=260,y=800)
        if (count % 300) == 0:   
            self.canvas.after_cancel(slove)
        if count <= 0 :
            
            slove = self .canvas.after( 1 , self.back)
        
    def next( self):
        
        
        global count
        if count > -900:
            count -= 1
        

        #移動指令           被移動的物件      移動的x ,y 
        if count != -900:
            self.canvas.move(self.img_menu1, -1 ,0) 
            self.canvas.move(self.img_menu2, -1 ,0)
            self.canvas.move(self.img_menu3, -1 ,0)
            self.canvas.move(self.img_menu4, -1 ,0)
      
        if count == 0:
            btm_main = Button(self.canvas , text='主畫面',image=img_1,command=self.next_page)
            btm_main.place(x=260,y=800)
        if count == -300:
            btm_main2 = Button(self.canvas , text='主畫面',image=img_2,command=self.next_page)
            btm_main2.place(x=260,y=800)
        if count == -600:
            btm_main = Button(self.canvas , text='主畫面',image=img_3,command=self.next_page)
            btm_main.place(x=260,y=800)
        if count == -900:
            btm_main = Button(self.canvas , text='主畫面',image=img_4,command=self.next_page)
            btm_main.place(x=260,y=800)
        if (count % 300) == 0:
  
            self.canvas.after_cancel(slove)
        
        if count > -900 :
            print('now =>',count)
            
            slove = self .canvas.after( 1 , self.next)
    
    def back_page(self):
        self.canvas.destroy()
        shoot_photo(self.master)

    def next_page(self):
        global number
        if count == 0:
            number = 1
        if count == -300:
            number = 2
        if count == -600:
            number = 3
        if count == -900:
            number = 4
        print('number = ',number)
        self.canvas.destroy()
        face3(self.master)

#確定照片
class face3():

    def __init__(self,master):
        self.master = master
        #self.master.config(bg='red')
        self.initface = tk.Frame(self.master)
        self.initface.pack()
      
        #背景2
        photo = tk.PhotoImage(file='img/bg_03.png')
        root.photo = photo
        lab =tk.Label(self.initface,width=1080,height=1920,image=photo)##??
        #global d
        #d = True
        #if d:
        lab.pack()
        
        #中間畫面
    
        global img_o
        if number ==1:
            img_o = img_1
        if number ==2:
            img_o = img_2
        if number ==3:
            img_o = img_3
        if number ==4:
            img_o = img_4
        root.img_o = img_o

        lab1 = tk.Label(lab,width=500,height=800,text='hello',image=img_o,anchor='center')
        lab1.place(x=295,y=800)

        #監聽
        root.bind('n',self.keyN)
        root.bind('N',self.keyN)
        root.bind('b',self.keyB)
        root.bind('B',self.keyB)
    def keyN(self,event):
        self.next()
    def keyB(self,event):
        self.back()
       
    

    def next(self):
        file_name = "upload/upload_pic.png"
        imagetk = img_o
        imgpil = ImageTk.getimage( imagetk )
        imgpil.save(file_name, "PNG")
        #global d
        #d = None
        #face3.lab.destory()

        self.initface.destroy()
        face4(self.master)
        #initface(self.master)
    
    def back(self):
        #global d
        #d = None
        #global count
        #count = 0
        self.initface.destroy()
        face2(self.master)

#qrcode/saveed
class face4():

    def __init__(self,master):
        self.master = master
        #self.master.config(bg='red')
        self.initface = tk.Frame(self.master)
        self.initface.pack()
        #背景2
        photo = tk.PhotoImage(file='img/bg_05.png')
        root.photo = photo
        lab =tk.Label(self.initface,width=1080,height=1920,image=photo)##??
        lab.pack()
        
        root.bind('n',self.keyN)
        root.bind('N',self.keyN)
        root.bind('b',self.keyB)
        root.bind('B',self.keyB)
    
    def keyN(self,event):
        self.next()

    def keyB(self,event):
        self.back()

    def next(self):
        self.initface.destroy()
        initface(self.master)

    def back(self):
        self.initface.destroy()
        face3(self.master)


global bgm
def play_bgm():
    py.mixer.music.load('sound_effect/60S_.mp3')
    py.mixer.music.play(-1)  

if __name__ == '__main__':
    mixer.init()
    
    play_bgm()
    root = tk.Tk()
    basedesk(root)
    
    
    root.mainloop()
