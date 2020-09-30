import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="创建Frame框架",pos=(100,100),size=(400,300))

if __name__ == '__main__':
    app = wx.App()                       #初始化
    frame = MyFrame(parent=None,id=-1)   #实例MyFrame类，并传递参数
    frame.Show()                         #显示窗口
    app.MainLoop()                       #调用主循环


