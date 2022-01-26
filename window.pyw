# coding = utf-8
import wx
import webbrowser
import sys

try:
    import program
except ImportError:
    wx.MessageBox('抱歉，恐怕您缺失了一个文件：program.py，请获取该文件的拷贝，并放至本程序的工作目录。')
    sys.exit(0)


class MainWindow(wx.Frame):
    def __init__(self, parent, window_id):
        wx.Frame.__init__(self, parent, window_id, '幻塔评论制造机 5.0 GUI Edition', size=(640, 480))
        wx.Frame.SetMaxSize(self, size=(640, 480))
        wx.Frame.SetMinSize(self, size=(640, 480))
        panel = wx.Panel(self)
        wx.StaticText(panel, label='欢迎来到幻塔评论制造机 5.0', pos=(5, 5))
        wx.StaticText(panel, label='在这里，你可以批量将原神的评论制造成幻塔评论。', pos=(5, 25))
        wx.StaticText(panel, label='待处理的原神评分区评论：', pos=(5, 65))
        wx.StaticText(panel, label='输出的幻塔奇葩评论：', pos=(100, 200))
        url = wx.StaticText(panel, label='版权所有，Advanced_Killer，点击进入B站主页', pos=(5, 400))
        url2 = wx.StaticText(panel, label='本程序遵循GPL许可证协议（首发至GitHub，点击进入）', pos=(5, 420))
        self.keyboard = wx.TextCtrl(panel, pos=(5, 85), size=(610, 100), style=wx.TE_MULTILINE)
        self.after = wx.TextCtrl(panel, value='', pos=(5, 225), size=(610, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.exc = wx.Button(panel, label='转换', pos=(5, 195))
        self.exc.Bind(wx.EVT_BUTTON, self.Transfer)
        url.Bind(wx.EVT_LEFT_DOWN, self.OpenUrl)
        url2.Bind(wx.EVT_LEFT_DOWN, self.OpenUrl2)

    def Transfer(self, event):
        genshin = self.keyboard.GetValue()
        hotta = program.exchange(genshin)
        self.after.SetValue(hotta)

    @staticmethod
    def OpenUrl(event):
        webbrowser.open('https://space.bilibili.com/477677552')

    @staticmethod
    def OpenUrl2(event):
        webbrowser.open('https://github.com/ThirdBlood/CommentCreator')


if __name__ == '__main__':
    app = wx.App()
    main = MainWindow(parent=None, window_id=-1)
    main.Show()
    app.MainLoop()
