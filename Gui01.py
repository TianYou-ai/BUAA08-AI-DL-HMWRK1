import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import RulesMatcher as Rm


wind = tk.Tk()
wind.title("动物识别 v1.0")
wind.geometry('800x600')
#打开指定的图片，缩放
def get_image(filename, width, height):
        im = Image.open(filename).resize((width,height))
        return ImageTk.PhotoImage(im)

canvas = tk.Canvas(wind, width=800,height=600,bd=0, highlightthickness=0)
filename = r'background.jpg'
photo = get_image(filename, 800,600)
canvas.create_image(400, 300, image=photo)
canvas.pack()

l = tk.Label(wind, text="你好，欢迎来到动物识别系统",\
         font=('Arial', 17), width=60, height=1)
l.place(x=10,y=10)

var1 = tk.StringVar() 
tk.Label(wind, text="判断结果", font=('Arial', 17),\
        bg='light green', width=25, height=1).place(x=430,y=50)

#选择规则
tk.Label(wind, text="请选择规则", font=('Arial', 17),\
        bg='light green', width=25, height=1).place(x=30,y=50)


tk.Label(wind, textvariable=var1, bg='light blue', font=('Arial', 12),\
        width=40, height=4).place(x=430,y=100)

rpath = 'Rules.xlsx'
InputPromise = {'有羽毛', '会游泳', '有黑白二色', '不会飞'}
testr = {'会游泳', '有黑白二色', '不会飞'}

var2 = tk.StringVar()

def update_selection():
    print(Rm.Premises(rpath))
    var2.set(tuple(Rm.Premises(rpath)))
    return var2

def print_selection():
    value = lb.get(lb.curselection())   # 获取当前选中的文本
    print(value)
    t.insert('end', str(value)+" ")

def clear_selection():
    var1.set("")  
    t.delete('1.0','end')

def do_it():
    search_data = t.get('1.0','end')
    print(search_data)
    InputPromise = set(search_data.split())
    print(InputPromise)
    conclusion = Rm.Rules_matcher(InputPromise, RulesPath = rpath) 
    str2 = ""
    for key in conclusion:
        str1 = ""
        for data1 in conclusion[key]:
            str1 += data1
            str1 += "、"
        str2 +=  str1 + "-> " + key + "\n" 
    print(str2)
    if (str2 == ""):
        var1.set("什么也推断不出来")
    else:
        var1.set(str2)

def add_it():
    sp = t_sp.get('1.0','end')
    sp = set(sp.split())
    if (len(sp)==0):
        tkinter.messagebox.showerror(title='空值错误', message='要添加的特征不能为空！')
        return 
    print(sp)
    cl = t_cl.get('1.0','end')
    if (len(cl.split())==0):
        tkinter.messagebox.showerror(title='空值错误', message='要添加的结论不能为空！')
        return
    cl = '是'+cl.split()[0]
    newrule = {cl : sp}
    print(newrule)
    result = 1
    result = Rm.Rules_adder(RulesPath = rpath, NewRule=newrule)
    print(result)
    if (result):
        tkinter.messagebox.showinfo(title='提示', message='添加成功！') 
    else:
        tkinter.messagebox.showinfo(title='提示', message='条件已经存在！') 
    var2 = update_selection()
    pass

def del_it():
    sp = t_sp.get('1.0','end')
    sp = set(sp.split())
    if (len(sp)==0):
        tkinter.messagebox.showerror(title='空值错误', message='要删除的特征不能为空！')
        return
    print(sp)
    cl = t_cl.get('1.0','end')
    if (len(cl.split())==0):
        tkinter.messagebox.showerror(title='空值错误', message='要删除的结论不能为空！')
        return
    cl = '是'+cl.split()[0]
    newrule = {cl : sp}
    print(newrule)
    result = 1
    result = Rm.Rules_deleter(RulesPath = rpath, OldRule=newrule)
    if (result):
        tkinter.messagebox.showinfo(title='提示', message='删除成功！') 
    else:
        tkinter.messagebox.showinfo(title='提示', message='要删除的数据不存在！') 
    var2 = update_selection()

var2 = update_selection()

lb = tk.Listbox(wind, font=('Arial', 17), height = 10, width=25, listvariable = var2)
lb.place(x=30,y=100)

b1 = tk.Button(wind, text='选择特征', font=('Arial', 17),\
        width=10, height=1, command=print_selection)
b1.place(x=30,y=400)

b2 = tk.Button(wind, text='清空内容',font=('Arial', 17),\
        width=10, height=1, command=clear_selection)
b2.place(x=230,y=400)

t = tk.Text(wind,font=('Arial', 17), width=50, height=1)
t.place(x=30,y=450)

b3 = tk.Button(wind,font=('Arial', 17), text='判断',\
        width=25, height=2, command=do_it)
b3.place(x=30,y=500)


tk.Label(wind, text="添加特征", bg='light green', font=('Arial', 13),\
        width=10, height=1).place(x=430,y=250)

tk.Label(wind, text="添加结论", bg='light green', font=('Arial', 13),\
        width=10, height=1).place(x=430,y=300)

t_sp = tk.Text(wind,font=('Arial', 13), width=25, height=1)
t_sp.place(x=530,y=250)
t_cl = tk.Text(wind,font=('Arial', 13), width=25, height=1)
t_cl.place(x=530,y=300)

b3 = tk.Button(wind,font=('Arial', 17), text='添加规则',\
        width=10, height=1, command=add_it)
b3.place(x=430,y=350)

b3 = tk.Button(wind,font=('Arial', 17), text="删除规则",\
        width=10, height=1, command=del_it)
b3.place(x=630,y=350)

wind.mainloop()