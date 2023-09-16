from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import font

root = Tk()
window_height = 500
window_width = 700
root.resizable(False, False)
root.title("namnamnam")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.configure(bg='pink')
label_font = font.Font(size=20)
msggg = Message( root, text = "(yazacağınız isim)'den Tatlı Kızın Olma Olasılığını hesapla:",bg='pink',font=label_font,anchor=CENTER,width=5000)  
msggg.pack()


msg1 = Message( root, text = "Düşünülüyor...",bg='pink',font=label_font,anchor=CENTER,width=5000)  
msg2 = Message( root, text = "Veriler analiz ediliyor...",bg='pink',font=label_font,anchor=CENTER,width=5000) 
msg3 = Message( root, text = "Beklemeye Devam edin...",bg='pink',font=label_font,anchor=CENTER,width=5000) 


def startPb():
    for i in range(1,101):
        pb['value'] = i
        root.update_idletasks()
        time.sleep(0.07)
        
        if pb['value'] == 5:
         msg1.pack()
    
        if pb['value'] == 45:
         msg2.pack()

        if pb['value'] == 70:
         msg3.pack()

    pb['value'] = 100
    msg.showerror(":)","Hesaplanamadı!!! ")
    msg.askquestion(":)","Gerçekten senden tatlı birinin bulunabileceğini mi düşündün?")
    msg.showinfo(":)","Seni ÇOOOOKK seviyorummm.")
    msg.showinfo(":)"," İyi ki varsın, iyi ki benimsin ağzını yüzünü yediğim her zaman mutlu ol canımın içi <3")
    msg.showinfo(":)","\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f")


pb = ttk.Progressbar(root, max=100.0, length=400)
pb.pack(pady=20)

Button(root, text="Hesapla", command=startPb).pack(pady=20)


root.mainloop()
