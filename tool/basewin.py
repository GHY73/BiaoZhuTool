# -*- coding: utf-8 -*-
# @Time :   19-5-2 下午5:07 
# @Author :     HaiYang Gao
# @OS：  ubuntu 16.04
# @File :   basewin.py 

import wx

"""
=============================step2:修改tag按钮的值=================================
选择性更改从line43到line108的‘自定义按钮区’的按钮值
1个修改的例子：
原句：
self.m_toggleBtn1 = wx.ToggleButton(self, wx.ID_ANY, u"1.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
要改的参数：u"1.自定义按钮"--->u"体育"
"""


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(748, 748), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHint(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        fgSizer3 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        main_text = wx.FlexGridSizer(2, 1, 0, 0)
        main_text.SetFlexibleDirection(wx.BOTH)
        main_text.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.title = wx.StaticText(self, wx.ID_ANY, u"title", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.title.Wrap(-1)
        self.title.SetMinSize(wx.Size(730, -1))

        main_text.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.content = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(730, 200),
                                   wx.TE_MULTILINE | wx.TE_RICH | wx.TE_RICH2)
        main_text.Add(self.content, 0, wx.ALL, 5)

        fgSizer3.Add(main_text, 1, wx.ALIGN_CENTER, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"tag类别"), wx.VERTICAL)

        gSizer8 = wx.GridSizer(4, 5, 0, 0)

        """
        ========================自定义按钮区=========================================
        自己修改tag按钮的名字，本次提供20个可选的tag。
        其余代码不要变动有任何变动，包括顺序
        """
        self.m_toggleBtn1 = wx.ToggleButton(self, wx.ID_ANY, u"1.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)

        gSizer8.Add(self.m_toggleBtn1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn2 = wx.ToggleButton(self, wx.ID_ANY, u"2.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn3 = wx.ToggleButton(self, wx.ID_ANY, u"3.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn4 = wx.ToggleButton(self, wx.ID_ANY, u"4.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn5 = wx.ToggleButton(self, wx.ID_ANY, u"5.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn6 = wx.ToggleButton(self, wx.ID_ANY, u"6.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn6, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn7 = wx.ToggleButton(self, wx.ID_ANY, u"7.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn8 = wx.ToggleButton(self, wx.ID_ANY, u"8.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn8, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn9 = wx.ToggleButton(self, wx.ID_ANY, u"9.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn9, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn10 = wx.ToggleButton(self, wx.ID_ANY, u"10.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn10, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn11 = wx.ToggleButton(self, wx.ID_ANY, u"11.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn12 = wx.ToggleButton(self, wx.ID_ANY, u"12.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn12, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn13 = wx.ToggleButton(self, wx.ID_ANY, u"13.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn13, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn14 = wx.ToggleButton(self, wx.ID_ANY, u"14.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn14, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn15 = wx.ToggleButton(self, wx.ID_ANY, u"15.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn15, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn16 = wx.ToggleButton(self, wx.ID_ANY, u"16.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn16, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn17 = wx.ToggleButton(self, wx.ID_ANY, u"17.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn17, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn18 = wx.ToggleButton(self, wx.ID_ANY, u"18.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn18, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn19 = wx.ToggleButton(self, wx.ID_ANY, u"19.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn19, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_toggleBtn20 = wx.ToggleButton(self, wx.ID_ANY, u"20.自定义按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self.m_toggleBtn20, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        """
        ========================自定义按钮区末尾=========================================
        =======step2调整结束，step3在mainwin.py中，对write_a_record()函数进行更改==========
        """

        self.m_toggleBtn1.SetValue(True)

        sbSizer12.Add(gSizer8, 1, wx.EXPAND, 5)

        fgSizer3.Add(sbSizer12, 1, wx.EXPAND, 5)

        sbSizer13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"关键词抽取"), wx.VERTICAL)

        gSizer12 = wx.GridSizer(6, 1, 0, 0)

        self.address_radio = wx.RadioButton(self, wx.ID_ANY, u"地名: ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer12.Add(self.address_radio, 0, wx.ALL, 5)

        self.add_words = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     0 | wx.NO_BORDER)
        self.add_words.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        self.add_words.SetMinSize(wx.Size(710, -1))

        gSizer12.Add(self.add_words, 0, wx.ALL, 5)

        self.name_radio = wx.RadioButton(self, wx.ID_ANY, u"人员: ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer12.Add(self.name_radio, 0, wx.ALL, 5)

        self.name_words = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(710, 20),
                                      0 | wx.NO_BORDER)
        self.name_words.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gSizer12.Add(self.name_words, 0, wx.ALL, 5)

        self.keyword_radio = wx.RadioButton(self, wx.ID_ANY, u"中心词: ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer12.Add(self.keyword_radio, 0, wx.ALL, 5)

        self.key_words = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(710, -1),
                                     0 | wx.NO_BORDER)
        self.key_words.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gSizer12.Add(self.key_words, 0, wx.ALL, 5)

        sbSizer13.Add(gSizer12, 1, wx.EXPAND, 5)

        fgSizer3.Add(sbSizer13, 1, wx.EXPAND, 5)

        gSizer9 = wx.GridSizer(1, 2, 10, 0)

        gSizer9.SetMinSize(wx.Size(-1, 50))
        self.m_button40 = wx.Button(self, wx.ID_ANY, u"下一条", wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer9.Add(self.m_button40, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"重载(暂时无用)", wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer9.Add(self.m_button41, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer3.Add(gSizer9, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.content.Bind(wx.EVT_LEFT_UP, self.get_sellect_words)
        self.m_toggleBtn1.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn2.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn3.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn4.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn5.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn7.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn9.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn10.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn11.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn13.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn14.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn15.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn17.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn19.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.m_toggleBtn20.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_label)
        self.address_radio.Bind(wx.EVT_RADIOBUTTON, self.select_address)
        self.name_radio.Bind(wx.EVT_RADIOBUTTON, self.select_name)
        self.keyword_radio.Bind(wx.EVT_RADIOBUTTON, self.select_keyword)
        self.m_button40.Bind(wx.EVT_BUTTON, self.next_doc)
        self.m_button41.Bind(wx.EVT_BUTTON, self.reload)

    def __del__(self):
        pass

    def get_sellect_words(self, event):
        event.Skip()

    def toggle_label(self, event):
        event.Skip()

    def select_address(self, event):
        event.Skip()

    def select_name(self, event):
        event.Skip()

    def select_keyword(self, event):
        event.Skip()

    def next_doc(self, event):
        event.Skip()

    def reload(self, event):
        event.Skip()
