import wx
#直接使用wx.App()
app = wx.App()
frame = wx.Frame(parent=None,title="Hello wxPython!")
frame.Show()
app.MainLoop()