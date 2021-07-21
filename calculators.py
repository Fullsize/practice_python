import tkinter
import math
window = tkinter.Tk()
window.title('计算器')
window.geometry('320x420')
# 显示文本
text = tkinter.StringVar()
text.set('0')
# 是否运算
is_calc = False
# 存储
storage = []
# 最多显示字符
maxShowLen = 18


def a(a):
    print(a)
    return a

# 数字键


def pressNumber(number: str) -> None:
    if text.get() == '0':
        text.set(number)
    else:
        if len(text.get()) < maxShowLen:
            text.set(text.get()+number)


buttons = [{
    'type': 'MC',
    'bg': '#666',
    'x': 20,
    'y': 110,
    'width': 50,
    'height': 35,
    'command': a
}, {
    'type': 'MR',
    'bg': '#666',
    'x': 77.5,
    'y': 110,
    'width': 50,
    'height': 35,
    'command': a
}, {
    'type': 'MS',
    'bg': '#666',
    'x': 135,
    'y': 110,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'M+',
    'bg': '#666',
    'x': 192.5,
    'y': 110,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'M-',
    'bg': '#666',
    'x': 250,
    'y': 110,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'del',
    'bg': '#666',
    'x': 20,
    'y': 155,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'CE',
    'bg': '#666',
    'x': 77.5,
    'y': 155,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'C',
    'bg': '#666',
    'x': 135,
    'y': 155,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '+/-',
    'bg': '#666',
    'x': 192.5,
    'y': 155,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': 'sqrt',
    'bg': '#666',
    'x': 250,
    'y': 155,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '7',
    'bg': '#666',
    'x': 20,
    'y': 200,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '8',
    'bg': '#666',
    'x': 75.5,
    'y': 200,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '9',
    'bg': '#666',
    'x': 135,
    'y': 200,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '/',
    'bg': '#708069',
    'x': 192.5,
    'y': 200,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '%',
    'bg': '#708069',
    'x': 250,
    'y': 200,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '4',
    'bg': '#666',
    'x': 20,
    'y': 245,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '5',
    'bg': '#666',
    'x': 75.5,
    'y': 245,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '6',
    'bg': '#666',
    'x': 135,
    'y': 245,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': 'x',
    'bg': '#708069',
    'x': 192.5,
    'y': 245,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '1/x',
    'bg': '#708069',
    'x': 250,
    'y': 245,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '3',
    'bg': '#666',
    'x': 20,
    'y': 290,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '2',
    'bg': '#666',
    'x': 75.5,
    'y': 290,
    'width': 50,
    'height': 35,
    'command': pressNumber
}, {
    'type': '1',
    'bg': '#666',
    'x': 135,
    'y': 290,
    'width': 50,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '-',
    'bg': '#708069',
    'x': 192.5,
    'y': 290,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '=',
    'bg': '#708069',
    'x': 250,
    'y': 290,
    'width': 50,
    'height': 80,
    'command': a
},
    {
    'type': '0',
    'bg': '#666',
    'x': 20,
    'y': 335,
    'width': 107.5,
    'height': 35,
    'command': pressNumber
},
    {
    'type': '.',
    'bg': '#666',
    'x': 135,
    'y': 335,
    'width': 50,
    'height': 35,
    'command': a
},
    {
    'type': '+',
    'bg': '#666',
    'x': 192.5,
    'y': 335,
    'width': 50,
    'height': 35,
    'command': a
}]


def renderBtn(btn: dict) -> None:
    x = tkinter.Button(window, text=btn['type'], bg=btn['bg'], bd=2,
                       command=lambda:  btn['command'](btn['type']))
    x.place(x=btn['x'], y=btn['y'],
            width=btn['width'], height=btn['height'])


def Body():
    window.minsize(320, 420)
    label = tkinter.Label(window, textvariable=text,
                          bg='black', anchor='e', bd=5, fg='white')
    label.place(x=20, y=50, width=280, height=50)
    for btn in buttons:
        renderBtn(btn)


Body()
window.mainloop()
