# -*- coding:utf-8 -*-

import tkinter as tk

def e2j(en):
    if en=='red':
        return u'빨강'
    elif en=='green':
        return u'초록'
    else:
        return u'파랑'


def change_bg(item, color):
    item.config(bg=color)
    for child in item.winfo_children():
        change_bg(child, color)

    
    
class MyWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)    
        
        
        info = tk.Label(self, text=u'색상 변화를 보세요 ', font=('궁서체', '12', 'bold'))
        info.pack(padx=10, pady=5)
        
        f = tk.Frame(self)
        f.pack(padx=5, pady=5)
        
        self.sc = dict()
        for i, color in enumerate(['red', 'green', 'blue']):
            print(i)
            la = tk.Label(f, text=e2j(color), fg=color)
            la.grid(row=0, column=i, padx=10, pady=5)
            self.sc[color] = tk.Scale(f, from_=0, to=255, orient='v', command=self.M_change)
            self.sc[color].set(255)
            self.sc[color].grid(row=1, column=i, padx=10, pady=5)
            

    def M_change(self, event):
        color = '#%02X%02X%02X' % (self.sc['red'].get(), self.sc['green'].get(), self.sc['blue'].get())
        change_bg(self, color)

        

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('tk')
    
    app = MyWindow(root)
    
    #root.geometry("500x300+0+0")
    
    root.mainloop()



#https://m.blog.naver.com/PostView.nhn?blogId=dudwo567890&logNo=130168372508&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F
#https://076923.github.io/posts/Python-tkinter-19/
#https://gist.github.com/withover/de66642df13cd8e1c5e6117f35001444
