import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="用户登录",size=(400,300))
        #创建面板
        panel = wx.Panel(self)
        #创建“确认”和“取消”按钮并绑定事件
        self.bt_confirm = wx.Button(panel,label="确定")
        #绑定事件
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,label="取消")
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        #创建文本，左对齐
        self.titile = wx.StaticText(panel,label="请输入用户名和密码")
        self.label_user = wx.StaticText(panel,label="用户名:")
        self.text_user = wx.TextCtrl(panel,style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,label="密   码:")
        self.text_pwd = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        #添加容器，容器中控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
        hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        hsizer_button.Add(self.bt_cancel,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        #添加容器，容器中的控件纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.titile,proportion=0,flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND | wx.LEFT | wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND | wx.LEFT | wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_button,proportion=0,flag=wx.ALIGN_CENTER | wx.TOP,border=15)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self,event):
        '''单击确定按钮，执行方法'''
        message = ""
        username = self.text_user.GetValue()     #获取输入的用户名
        password = self.text_pwd.GetValue()      #获取输入的密码
        if username == "" or password == "":
            message = "用户名和密码不能为空"
        elif username == "admin" and password == "admin123":
            message = "登录成功"
        else:
            message = "用户名和密码不匹配"
        #弹出提示框
        wx.MessageBox(message)
    def OnclickCancel(self,event):
        "单击取消按钮，执行方法"
        self.text_user.SetValue("")
        self.text_pwd.SetValue("")





if __name__ == '__main__':
    app = wx.App()                       #初始化
    frame = MyFrame(parent=None,id=-1)   #实例MyFrame类，并传递参数
    frame.Show()                         #显示窗口
    app.MainLoop()                       #调用主循环


