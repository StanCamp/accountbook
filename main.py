import tkinter as tk
import dataBase
from tkinter import messagebox


class baseview():

    def __init__(self, master):
        self.root = root
        self.root.config()
        root.title('base')
        # 得到屏幕宽度
        sw = root.winfo_screenwidth()
        # 得到屏幕高度
        sh = root.winfo_screenheight()
        ww = sw / 2
        wh = sh / 2
        # 窗口宽高为取窗口宽高的一半为登陆界面的宽和高
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        login_view(self.root)


class login_view():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.login_view = tk.Frame(self.master, )
        self.login_view.pack()
        master.title('登陆界面')

        # 得到屏幕宽度
        sw = master.winfo_screenwidth()
        # 得到屏幕高度
        sh = master.winfo_screenheight()
        ww = sw / 2
        wh = sh / 2
        # 窗口宽高为取窗口宽高的一半为登陆界面的宽和高
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        frame_a = tk.Frame(master)
        frame_a.pack()

        # 登陆字体
        login_label = tk.Label(frame_a, text='登录', font=('宋体', 20, 'bold'))
        login_label.grid(row=0, columnspan=2)

        um_laber = tk.Label(frame_a, text='用户名', font=('宋体', 15))
        um_laber.grid(row=1, column=0)

        # 创建字符串变量和文本输入框组件，同时设置关联的变量
        varName = tk.StringVar(frame_a, value='')
        entryName = tk.Entry(frame_a, textvariable=varName)
        entryName.grid(row=1, column=1)

        pwd_label = tk.Label(frame_a, text='密码', font=('宋体', 15), justify=tk.RIGHT)
        pwd_label.grid(row=2, column=0)

        # 创建密码输入框
        varPwd = tk.StringVar(frame_a, value='')
        entryPwd = tk.Entry(frame_a, show='*', textvariable=varPwd)
        entryPwd.grid(row=2, column=1)

        # 登录按钮
        login_button = tk.Button(frame_a, height=int(sw / 1024), width=int(sh / 32), text='登录',
                                 bg='CornflowerBlue',
                                 fg='white',
                                 command=lambda: login(self, varName.get(), varPwd.get()))
        login_button.grid(row=3, column=0)

        # 注册按钮
        login_button = tk.Button(frame_a, height=int(sw / 1024), width=int(sh / 32), text='注册',
                                 bg='CornflowerBlue',
                                 fg='white',
                                 command=lambda: zhuce(self))
        login_button.grid(row=3, column=1)

        def login(self, username, password):
            sql = "select * from T_user where username='" + username + "'"
            result = dataBase.executeQuery(sql)
            if password == result[0][1]:
                messagebox.showinfo('提示', '登陆成功')
                frame_a.destroy()
                option(self.master)
            else:
                messagebox.showerror('错误', '用户名或者密码错误')

        def zhuce(self):
            frame_a.destroy()
            register(self.master)


class register():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.login_view = tk.Frame(self.master, )
        self.login_view.pack()
        master.title('注册界面')
        # 得到屏幕宽度
        sw = master.winfo_screenwidth()
        # 得到屏幕高度
        sh = master.winfo_screenheight()
        ww = sw / 2
        wh = sh / 2
        # 窗口宽高为取窗口宽高的一半为登陆界面的宽和高
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        frame_a = tk.Frame(master)
        frame_a.pack()
        # 登陆字体
        register_label = tk.Label(frame_a, text='注册', font=('宋体', 20, 'bold'))
        register_label.grid(row=0, columnspan=2)

        um_laber = tk.Label(frame_a, text='用户名', font=('宋体', 15))
        um_laber.grid(row=1, column=0)

        # 创建字符串变量和文本输入框组件，同时设置关联的变量
        varName = tk.StringVar(frame_a, value='')
        entryName = tk.Entry(frame_a, textvariable=varName)
        entryName.grid(row=1, column=1)

        pwd_label = tk.Label(frame_a, text='密码', font=('宋体', 15), justify=tk.RIGHT)
        pwd_label.grid(row=2, column=0)

        # 创建密码输入框
        varPwd = tk.StringVar(frame_a, value='')
        entryPwd = tk.Entry(frame_a, show='*', textvariable=varPwd)
        entryPwd.grid(row=2, column=1)
        register_button = tk.Button(frame_a, height=int(sw / 1024), width=int(sh / 32), text='注册',
                                    bg='CornflowerBlue',
                                    fg='white',
                                    command=lambda: submit_user(self, varName.get(), varPwd.get()))
        register_button.grid(row=3, columnspan=1)

        # 提交函数
        def submit_user(self, username, password):
            sql = "insert into T_user (username,password) values ('{0}','{1}')".format(username, password)
            if dataBase.executeUpdate(sql):
                messagebox.showinfo('提示', '插入成功')
                frame_a.destroy()
                login_view(self.master)
            else:
                messagebox.showerror('错误', '插入失败')


class option():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.option = tk.Frame(self.master, )
        self.option.pack()
        master.title('操作界面')
        # 得到屏幕宽度
        sw = master.winfo_screenwidth()
        # 得到屏幕高度
        sh = master.winfo_screenheight()
        ww = sw / 2
        wh = sh / 2
        # 窗口宽高为取窗口宽高的一半为登陆界面的宽和高
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        frame_a = tk.Frame(master)
        frame_a.pack()

        um_laber = tk.Label(frame_a, text='日期', font=('宋体', 15))
        um_laber.grid(row=1, column=0)

        # 创建字符串变量和文本输入框组件，同时设置关联的变量，日期输入框
        varDate = tk.StringVar(frame_a, value='')
        entryDate = tk.Entry(frame_a, textvariable=varDate)
        entryDate.grid(row=1, column=1)

        event_label = tk.Label(frame_a, text='事件', font=('宋体', 15), justify=tk.RIGHT)
        event_label.grid(row=2, column=0)

        # 创建事件输入框
        varEvent = tk.StringVar(frame_a, value='')
        entryEvent = tk.Entry(frame_a, textvariable=varEvent)
        entryEvent.grid(row=2, column=1)

        consumption_label = tk.Label(frame_a, text='消费金额', font=('宋体', 15), justify=tk.RIGHT)
        consumption_label.grid(row=3, column=0)

        # 创建事件输入框
        varConsumption = tk.StringVar(frame_a, value='')
        entryConsumption = tk.Entry(frame_a, textvariable=varConsumption)
        entryConsumption.grid(row=3, column=1)

        # 创建下拉菜单
        option_label = tk.Label(frame_a, text='选项', font=('宋体', 15), justify=tk.RIGHT)
        option_label.grid(row=4, column=0)

        # 创建下拉菜单
        varOption = tk.StringVar(frame_a, value='')
        option_Menu = tk.OptionMenu(frame_a, varOption, 'insert', 'delete', 'update', 'query', 'showall')
        option_Menu.grid(row=4, column=1)

        submit_button = tk.Button(frame_a, text='提交', height=int(sw / 1024), width=int(sh / 32), bg='CornflowerBlue',
                                  fg='white',
                                  command=lambda: submit(varDate.get(), varEvent.get(), varConsumption.get(),
                                                         varOption.get(), self))
        submit_button.grid(row=4, columnspan=1)

        def submit(date, event, consumpution, option_choose, self):
            if option_choose == 'insert':
                sql = "insert into T_information (date,event,consumption) values ('{0}','{1}',{2})".format(date, event,
                                                                                                           float(
                                                                                                               consumpution))
                if dataBase.executeUpdate(sql):
                    messagebox.showinfo('提示', '插入成功')
                else:
                    messagebox.showerror('错误', '插入失败')
            elif option_choose == 'delete':
                sql = "delete from T_information where date='{0}'".format(date)
                if dataBase.executeUpdate(sql):
                    messagebox.showinfo('提示', '删除成功')
                else:
                    messagebox.showerror('错误', '删除失败')
            elif option_choose == 'update':
                sql = "update T_information set event='{0}',consumption={1} where date='{2}'".format(event, float(
                    consumpution), date)
                if dataBase.executeUpdate(sql):
                    messagebox.showinfo('提示', '修改成功')
                else:
                    messagebox.showerror('错误', '修改失败')
            elif option_choose == 'query':
                sql = "select * from T_information where date='{}'".format(date)
                cur = dataBase.executeQuery(sql)
                frame_a.destroy()
                show(self.master, cur)
            elif option_choose == 'showall':
                sql = 'select * from T_information'
                cur = dataBase.executeQuery(sql)
                frame_a.destroy()
                show(self.master, cur)


class show():
    def __init__(self, master, curor):
        # 得到屏幕宽度
        sw = master.winfo_screenwidth()
        # 得到屏幕高度
        sh = master.winfo_screenheight()
        self.master = master
        self.master.config()
        self.option = tk.Frame(self.master, )
        self.option.pack()
        self.master.title('操作界面')
        frame_a = tk.Frame(master)
        frame_a.pack()

        back_button = tk.Button(frame_a, text='返回', bg='CornflowerBlue',
                                fg='white',
                                command=lambda: back(self))
        back_button.grid(row=0, columnspan=2)

        # 返回按钮
        def back(self):
            frame_a.destroy()
            option(self.master)

        date_label = tk.Label(frame_a, text='日期', font=('宋体', 15, 'bold'), justify=tk.RIGHT)
        date_label.grid(row=1, column=0)

        event_label = tk.Label(frame_a, text='事件', font=('宋体', 15, 'bold'), justify=tk.RIGHT)
        event_label.grid(row=1, column=1)

        consumption_label = tk.Label(frame_a, text='消费', font=('宋体', 15, 'bold'), justify=tk.RIGHT)
        consumption_label.grid(row=1, column=2)
        j = 2
        for i in curor:
            # 列表中的日期
            date = tk.Label(frame_a, text=i[0], justify=tk.RIGHT)
            date.grid(row=j, column=0)
            # 列表中的事件
            event = tk.Label(frame_a, text=i[1], justify=tk.RIGHT)
            event.grid(row=j, column=1)
            # 列表中的金额
            consum = tk.Label(frame_a, text=i[2], justify=tk.RIGHT)
            consum.grid(row=j, column=2)
            j = j + 1


if __name__ == '__main__':
    root = tk.Tk()
    baseview(root)
    root.mainloop()
