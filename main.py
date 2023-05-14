import random
import tkinter
import threading
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox

lift = [{'level': 0, 'state': 0, 'aim': []}, {'level': 1, 'state': 0, 'aim': []}, {'level': 20, 'state': 0, 'aim': []},
        {'level': 20, 'state': 0, 'aim': []}]

state = [{'dir': 0, 'flag': 0} for _ in range(21)]


def main():  # 定义主函数
    window = Tk()  # 创建一个tk窗口
    window.title("电梯控制系统")  # 设置窗口的标题
    window.geometry("250x150")  # 设置窗口的长宽为300,200

    label = Label(window, text="欢迎使用智能电梯控制系统", fg="green")  # 放置欢迎标签在窗口
    label.pack()

    frame = Frame(window)  # 放置框架在窗口
    frame.pack()

    buAction = Button(frame, text="动画演示", command=pressAction, fg="red")
    buRule = Button(frame, text="规则", command=pressRule, fg="brown")
    buExit = Button(frame, text="退出", command=pressExit, fg="black")

    buAction.grid(row=1, column=3)
    buRule.grid(row=2, column=3)
    buExit.grid(row=3, column=3)

    window.mainloop()  # 循环接受消息


def pressUp(level):
    if level != 20:
        state[level]['dir'] = 1
        state[level]['flag'] = 1
        set_state()


def pressDown(level):
    if level != 0:
        state[level]['dir'] = -1
        state[level]['flag'] = 1
        set_state()


def pressAction():  # 按下动画演示按钮
    newWindow = Tk()

    newWindow.title("模拟运行参数设定")
    newWindow.geometry("300x400")  # 设置窗口的长宽为300,200
    frame = Frame(newWindow)
    frame.pack()

    label = Label(newWindow, text="初始化设置四个电梯的位置")
    label.pack()

    var = IntVar(master=newWindow, value=2)
    rd1 = Radiobutton(newWindow, text="随机", variable=var, value=1)
    rd2 = Radiobutton(newWindow, text="手动设定", variable=var, value=2)
    rd1.pack()
    rd2.pack()

    option1 = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]

    option2 = [
        1, 3, 5, 7, 9, 11, 13, 15, 17, 19
    ]

    option3 = [
        0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
    ]

    option4 = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]

    lift1 = Label(newWindow, text="电梯1")
    lift2 = Label(newWindow, text="电梯2")
    lift3 = Label(newWindow, text="电梯3")
    lift4 = Label(newWindow, text="电梯4")

    # 创建下拉列表的 IntVar 变量
    selected_option1 = IntVar(newWindow)
    selected_option2 = IntVar(newWindow)
    selected_option3 = IntVar(newWindow)
    selected_option4 = IntVar(newWindow)

    # 创建带有滑动条的下拉列表
    combo_box1 = Combobox(newWindow, textvariable=selected_option1, values=option1, state="readonly")
    combo_box2 = Combobox(newWindow, textvariable=selected_option2, values=option2, state="readonly")
    combo_box3 = Combobox(newWindow, textvariable=selected_option3, values=option3, state="readonly")
    combo_box4 = Combobox(newWindow, textvariable=selected_option4, values=option4, state="readonly")
    combo_box1.set(0)
    combo_box2.set(1)
    combo_box3.set(20)
    combo_box4.set(20)
    combo_box1.bind()

    lift1.pack()
    combo_box1.pack()
    lift2.pack()
    combo_box2.pack()
    lift3.pack()
    combo_box3.pack()
    lift4.pack()
    combo_box4.pack()

    buDemo = Button(newWindow, text="演示", command=lambda: Demo(var.get(), selected_option1.get(),
                                                                 selected_option2.get(), selected_option3.get(),
                                                                 selected_option4.get())
                    )
    buDemo.pack()


base = 440
grid = 30


def Demo(var, option1, option2, option3, option4):
    if var == 1:
        list1 = [
            1, 3, 5, 7, 9, 11, 13, 15, 17, 19
        ]
        list2 = [
            0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
        ]
        lift[0]['level'] = random.randint(0, 20)
        lift[1]['level'] = random.choice(list1)
        lift[2]['level'] = random.choice(list2)
        lift[3]['level'] = random.randint(0, 20)
    else:
        lift[0]['level'] = option1
        lift[1]['level'] = option2
        lift[2]['level'] = option3
        lift[3]['level'] = option4

    window = Tk()
    window.title("动画演示")

    canvas = Canvas(window, width=1000, height=700, bg="white")
    canvas.pack()

    frame = Frame(window)
    frame.pack()

    label = Label(frame, text="当前所在楼层:")
    label.pack()

    # 定义下拉框列表选项
    options = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]

    # 创建下拉列表的 IntVar 变量
    selected_option = IntVar(frame)

    # 创建带有滑动条的下拉列表
    combo_box = Combobox(frame, textvariable=selected_option, values=options, state="readonly")
    combo_box.pack()

    buUp = Button(frame, text="↑", command=lambda: pressUp(selected_option.get()))
    buDown = Button(frame, text="↓", command=lambda: pressDown(selected_option.get()))
    buUp.pack()
    buDown.pack()

    create_timer(canvas)

    window.mainloop()


def create_timer(c):
    timer = threading.Timer(2, lambda: call(c))
    timer.start()


def call(c):
    c.delete(tkinter.ALL)
    draw(c)
    change_lift()
    create_timer(c)


def draw(canvas):
    for i in range(4):
        canvas.create_text(base + i * grid + grid / 2, 50 - grid / 2, text=lift[i]['level'])
        for j in range(21):
            if i == 1:
                if j % 2 != 0:
                    if j == lift[i]['level']:
                        canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                                (20 - j) * grid + 50, fill="red")
                    else:
                        canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                                (20 - j) * grid + 50, fill="green")
            elif i == 2:
                if j % 2 == 0:
                    if j == lift[i]['level']:
                        canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                                (20 - j) * grid + 50, fill="red")
                    else:
                        canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                                (20 - j) * grid + 50, fill="green")
            else:
                if j == lift[i]['level']:
                    canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                            (20 - j) * grid + 50, fill="red")
                else:
                    canvas.create_rectangle(base + i * grid, (20 - j) * grid + grid + 50, base + i * grid + grid,
                                            (20 - j) * grid + 50, fill="green")

    for i in range(21):
        canvas.create_text(base - 20, i * grid + 50 + grid / 2, text=20 - i)
        if state[i]['dir'] == 1:
            canvas.create_text(base - 40, (20 - i) * grid + 50 + grid / 2, text="↑")
        elif state[i]['dir'] == -1:
            canvas.create_text(base - 40, (20 - i) * grid + 50 + grid / 2, text="↓")
    canvas.create_text(base - 20, 50 - grid / 2, text="楼层")


def pressRule():
    window = Tk()
    window.title("规则")
    text = Text(window, height=30)
    text.grid(row=1, column=1)
    text.insert(END, "现有一新建办公大厦，共有21层，共有四部电梯，所有电梯基本参数如下表所示，其使用规定如下：\n"
                     "①　楼层号为0~20，其中0号为地下一层\n"
                     "②　有楼层限制的电梯不在相应楼层停靠，如单双层\n"
                     "③　所有电梯采用统一按钮控制\n"
                     "④　请根据上述要求设计并实现一个电梯控制程序，使得用户平均等待时间尽可能小，如果有图形显示就更好了。\n"
                     "电梯编号\t可服务楼层\t最大乘客数量\t最大载重量\n"
                     "1\t全部楼层\t10\t800\tkg\n"
                     "2\t单层\t10\t800\tkg\n"
                     "3\t双层\t10\t800\tkg\n"
                     "4\t全部楼层\t20\t2000\tkg\n")


def pressExit():
    exit(0)


def set_state():
    min = {'dis': 30, 'lift': 0}
    for i in range(21):
        if state[i]['flag'] == 1:  # 按下标志
            for j in range(4):  # 遍历所有电梯
                if (i % 2 != 0 and j == 2) or (i % 2 == 0 and j == 1):
                    continue
                if lift[j]['state'] == 0 or (lift[j]['state'] == 1 and i >= j and state[i]['dir'] == 1) or \
                        (lift[j]['state'] == -1 and i <= j and state[i]['dir'] == -1):  # 如果该楼层在电梯运行路径上且方向相同/该电梯静止
                    if i >= lift[j]['level']:
                        distance = i - lift[j]['level']
                    else:
                        distance = lift[j]['level'] - i
                    if min['dis'] > distance:
                        min['dis'] = distance
                        min['lift'] = j

            lift[min['lift']]['aim'].append(i)  # 加入到要访问的路径上去
            if i > lift[min['lift']]['level']:
                lift[min['lift']]['state'] = 1  # 设置电梯方向
            else:
                lift[min['lift']]['state'] = -1  # 设置电梯方向
            state[i]['flag'] = 0  # 清除标志位，代表已经有电梯将该楼层设为访问路径


def change_lift():
    for i in range(4):
        if lift[i]['state'] != 0:
            if lift[i]['state'] == 1:
                if i == 1 or i == 2:
                    lift[i]['level'] += 2
                else:
                    lift[i]['level'] += 1
            else:
                if i == 1 or i == 2:
                    lift[i]['level'] -= 2
                else:
                    lift[i]['level'] -= 1
            for j in lift[i]['aim']:
                if lift[i]['level'] == j:  # 如果已经到了相应楼层
                    state[j]['dir'] = 0  # 该楼层方向清零
                    lift[i]['aim'].remove(j)  # 在列表中移出该楼层
            if not lift[i]['aim']:  # 访问列表为空
                lift[i]['state'] = 0


main()  # 主函数
