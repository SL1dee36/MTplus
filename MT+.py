#MathTester
import customtkinter as ctk 
import tkinter as tk
import random
from os import system as sys
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import webbrowser
from getpass import getuser
import urllib.request


sys('cls')

root = tk.Tk()
root.title("MATH:TESTER::F0.12")
root.geometry("1300x600")
root.wm_minsize(1300, 600)

score = 0
time_limit = random.randint(3, 90) * 60  # Update time_limit to a random value between 3 and 90 minutes


st_time_limit = time_limit
total_tasks = 1
correct_tasks = 0
timer_id = None  # Initialize the timer_id variable

foil = 0
hints = 3
stop_btn = False

informational_panel_text = r'''    
 > About:

    MathTester is a generator of mathematical examples 
    for learning and repeating and consolidating 
    the acquired knowledge.

----------------------------------------------------

 > Правила:

 1. Вводите ответ с округлением до сотых долей.
    например: Вы получили ответ: 7.135, 
    в поле ввода ответов вводим: 7.14 

    Если вы получили целый ответ, то вводите его 
    как есть, например число 89, в поле ответов,
    мы введём ровно так же как и получили: 89

 2. Если задача, которую вы решаете, слишком сложная,
    то чтобы не тратить на неё время вы можете
    использовать комманду: skip,
    дабы пропустить её и узнать ответ.

----------------------------------------------------

 > Разработчик: Назарян A.K                
                                                    
                                                    '''

help_math = r'''
    [?]    Примеры формул:

    [1]    sin(x) | arcsin(x)
    [2]    cos(x) | arccos(x)
    [3]    tan(x) | arctan(x)
    [4]    sum(x) 
    [5]    exp(-x**3)
    [6]    log(x)
    [7]    ln(x)
    [8]    sqrt(x)
    [9]    power(x, n)
    [10]   abs(x)
    [11]   round(x)
    [12]   floor(x)
    [13]   ceil(x)

    [+]    И др..  
    можете изучить библиотеку NumPy 
    для более подробного разбора
'''

#Functions

def open_link(event):
    webbrowser.open("https://t.me/Slide36")

def theme():  #выбор тем. (Тёмная и светлая)
    pass



def open_site(event):
    webbrowser.open("https://github.com/SL1dee36?tab=repositories")

def stop_btn_clicked():
    global stop_btn
    stop_btn = True

def on_closing():
    print('end task') # Дополнительные операции перед закрытием окна
    try:
        devMenu.destroy()
    except:
        pass
    root.destroy()  # Закрытие окна
    
def Graph_on_closing():
    root.destroy()
    exit()

def restart_test():
    global score, time_limit, total_tasks, correct_tasks, timer_id,hints,tester,st_time_limit  # Add timer_id here
    score = 0
    time_limit = random.randint(3, 90) * 60  # Update time_limit to a random value between 3 and 90 minutes
    total_tasks = 1
    st_time_limit = time_limit
    correct_tasks = 0
    hints = 3
    generate_task()
    update_timer(time_limit)
    user_entry.config(state="normal")
    hint_button.config(state="normal")
    stats_frame.pack_forget()
    task_frame.pack_forget()
    result_frame.pack_forget()
    tester()

def StartButton_():
    global MainLogo,StartButton,SettingsButton,feedback_button, informational_panel,feedback_btn,site_label,MainSubtitle
    print("command started")

    close_menu()

    tester()

def Graph_Button_():
    print("command started")
    close_menu()

    MathGraph()

def hint():
    global score,hints, result
    if score > 0 and hints > 1:
        score -= 1
        hints -= 1
        score_label.config(text="Score: " + str(score))
        hint_button.configure(text=f"Hint: {hints}")
        answer_label.config(text=f'\n{result}\n',font=('Courier New', 12))

def update_plot():
    formula = input_entry.get()

    if '^' in formula:
        formula = formula.replace('^', '**')
    elif ':' in formula:
        formula = formula.replace(':', '/')


    try:
        x = np.linspace(-10, 10, 400)
        y = eval(formula, {'__builtins__': None}, {'x': x, 'np': np, 'sin': np.sin, 'cos': np.cos, 
                                                   'tan': np.tan, 'pi': np.pi, 'sqrt': np.sqrt, 'arctan': np.arctan, 'arcsin': np.arcsin, 
                                                   'arccos': np.arccos, 'exp': np.exp, 'abs': np.absolute, 'round': np.round, 
                                                   'floor': np.floor, 'ceil': np.ceil, 'sum': np.sum, 'log': np.log, 'ln': np.log10, 'power': np.power})
        plot_ax.clear()
        plot_ax.plot(x, y)
        plot_canvas.draw()

        error_label.pack_forget()
    except Exception as e:
        print(e)
        plot_ax.clear()
        plot_canvas.draw()
        error_label.pack()

def MathGraph():
    global input_entry,error_label,plot_canvas,plot_ax,left_frame,input_label,hints_label,hints_text,right_frame,figure,feedback_btn,update_button

    root.protocol("WM_DELETE_WINDOW", Graph_on_closing)
    left_frame = tk.Frame(root,bg='white')
    left_frame.pack(side="left")

    input_label = tk.Label(left_frame, text="Введите формулу:", font=("Courier New", 12),bg='white')
    input_label.pack(pady=10)

    input_entry = tk.Entry(left_frame, font=("Courier New", 12), width=40,relief='sunken',bg='white')
    input_entry.pack(padx=5)
    input_entry.configure(justify="center")

    hints_label = tk.Label(left_frame, text="Подсказки интересных формул:", font=("Courier New", 12),bg='white')
    hints_label.pack(pady=10)

    hints_text = tk.Text(left_frame, height=10, width=40, font=("Courier New", 12),bg='white')
    hints_text.pack()
    hints_text.insert(tk.END, f"{help_math}")
    hints_text.config(state="disabled")

    right_frame = tk.Frame(root,bg='white')
    right_frame.pack(side="right")

    error_label = tk.Label(right_frame, text="Ошибка в формуле", font=("Courier New", 12), fg="red",relief='sunken',bg='white')
    error_label.pack(pady=10)
    error_label.pack_forget()

    figure = plt.figure(figsize=(8, 6))
    plot_ax = figure.add_subplot(1, 1, 1)
    plot_canvas = FigureCanvasTkAgg(figure, master=right_frame)
    plot_canvas.get_tk_widget().pack()

    update_button = ctk.CTkButton(left_frame, text="Обновить", font=("Courier New", 16),corner_radius=12, command=update_plot,fg_color=('white','#6b26b1'),hover_color=('black','#b026b1'))
    update_button.pack(pady=10)
    Exit_button = ctk.CTkButton(left_frame, text="Back 2 Menu", font=("Courier New", 16),corner_radius=12, command=mainmenu,fg_color=('white',"#581845"),hover_color=('black','#900C3F'))
    Exit_button.pack(pady=10)

    feedback_btn = tk.Label(left_frame, text="feedback", fg="#0064ff", cursor="hand2", width=13, font=("Courier New", 12),bg='white')
    feedback_btn.pack(pady=50)
    feedback_btn.bind("<Button-1>", open_link)
#MainFunction

def mainmenu():
    global MainLogo,StartButton,SettingsButton,feedback_button, informational_panel,feedback_btn,site_label,MainSubtitle,Graph_Button

    close_menu()

    try:
        stats_frame.pack_forget()
    except:
        pass

    MainLogo=tk.Label(root, bg="white", font=("Courier New", 46),width=80, justify="center", text='MΔTH:TΣSTΣR')
    MainLogo.place(x=30,y=50,width=425,height=50)
    MainSubtitle=tk.Label(root, bg="white", font=("Courier New", 16),width=80, justify="center", text='"version F0.12"')
    MainSubtitle.place(x=30,y=105,width=400,height=25)

    StartButton=ctk.CTkButton(root,text='Начать тестирование',corner_radius=10,width=300,height=75,fg_color=("white", "#581845"),hover_color='#900C3F',font=('Courier New', 16),command=StartButton_)
    StartButton.place(x=80,y=280)

    Graph_Button=ctk.CTkButton(root,text='Построить график',corner_radius=10,width=300,height=75,fg_color=("white", "#581845"),hover_color='#900C3F',font=('Courier New', 16),command=Graph_Button_)
    Graph_Button.place(x=80,y=365)

    informational_panel=tk.Text(root, height=16, width=45, font=("consolas", 11), relief='solid')
    informational_panel.place(x=690,y=30,width=470,height=530)
    informational_panel.insert(tk.END, informational_panel_text)
    informational_panel.config(state="disabled")

    site_label=tk.Label(root,text=f'www.github.com', bg='white', font=('Courier New', 12), justify='left', relief='flat', fg="#0064ff",cursor="hand2")
    site_label.place(x=80,y=500,width=300,height=18)
    site_label.bind("<Button-1>", open_site)

    devMenu_label=tk.Label(root,text='…', bg='white', font=('Courier New', 8), justify='left', relief='flat', fg="black",cursor="hand2")
    devMenu_label.place(x=1200,y=20,width=60,height=40)
    devMenu_label.bind("<Button-1>", devMenu_)

    feedback_btn = tk.Label(root, text="⌬ send feedback", fg="#0064ff", cursor="hand2", width=13, font=("Courier New", 12),bg='white')
    feedback_btn.place(x=80,y=460,width=300,height=15)
    feedback_btn.bind("<Button-1>", open_link)

    root.configure(bg="white")
    root.mainloop()

def close_menu():
    try:
        MainLogo.place_forget()
        StartButton.place_forget()
        informational_panel.place_forget()
        site_label.place_forget()
        MainSubtitle.place_forget()
        feedback_btn.place_forget()
        Graph_Button.place_forget()
    except:
        pass

    try:
        left_frame.pack_forget()
        error_label.pack_forget()
        left_frame.pack_forget()
        input_label.pack_forget()
        hints_label.pack_forget()
        hints_text.pack_forget()
        right_frame.pack_forget()
        feedback_btn.pack_forget()
        update_button.pack_forget()
    except:
        pass

    try:
        stats_frame.pack_forget()
    except:
        pass

def tester():
    global stats_frame,user_entry,hint_button,task_frame,total_tasks,correct_tasks,result_frame,score_label,timer_label,task_label,answer_label
    global correct_label,feedback_btn,site_label,score, time_limit, total_tasks, correct_tasks, timer_id,hints,st_time_limit,MainSubtitle
    
    close_menu()

    try:
        score = 0
        time_limit = random.randint(3, 90) * 60  # Update time_limit to a random value between 3 and 90 minutes
        total_tasks = 1
        st_time_limit = time_limit
        correct_tasks = 0
        hints = 3
    except:
        pass

    task_frame = tk.Frame(root, bg="white")
    task_frame.pack(side="left", padx=20, pady=20)

    result_frame = tk.Frame(root, bg="white",relief='solid')
    result_frame.pack(side="right", padx=20, pady=20)


    task_label = tk.Label(task_frame, text="", font=("Courier New", 24), bg="white")
    task_label.pack(padx=50)

    user_entry = tk.Entry(task_frame, font=("Courier New", 24), width=32, justify='center', relief='solid')
    user_entry.pack()

    check_button = tk.Button(task_frame, text="Send answer", font=("Courier New", 16), command=check_answer, width=15, relief='groove',activebackground='white',background='white')
    check_button.pack(pady=10, padx=50)

    score_label = tk.Label(result_frame, text="Score: 0", font=("Courier New", 24), bg="white")
    score_label.pack(pady=10)

    timer_label = tk.Label(result_frame, text="Time left: " + str(time_limit) + "s", font=("Courier New", 20), bg="white")
    timer_label.pack(padx=50)

    answer_label = tk.Label(result_frame, text="", font=("Courier New", 20), bg="white")
    answer_label.pack(padx=50)

    result_text = '\nText\n'
    answer_label.config(text=result_text, fg='white', font=('Courier New', 12))

    hint_button = tk.Button(result_frame, text=f"Hints: {hints}", font=("Courier New", 16), command=hint, width=15,activebackground='white',background='white',relief='solid')
    hint_button.pack(pady=10, padx=50)

    stop_button = tk.Button(result_frame, text="Finish early", font=("Courier New", 16), command=stop_btn_clicked, width=15,activebackground='white',background='white',relief='solid')
    stop_button.pack(pady=10, padx=50)

    generate_task()
    update_timer(time_limit)

    root.configure(bg="white")
    task_frame.configure(bg="white")
    result_frame.configure(bg="white")

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Привязка обработчика события закрытия окна
    root.mainloop()

def update_timer(time_limit):
    global stop_btn
    timer_label.config(text="Time left: " + str(time_limit) + "s")
    
    if time_limit <= 0 or stop_btn == True:
        global score,total_tasks,correct_tasks, foil,hints,stats_frame
        #root.after_cancel(timer_id)
        
        if correct_tasks == 0 and total_tasks == 0 or 1:
            foil = 2
        if correct_tasks > total_tasks:
            foil = 2
        else:
            foil = round(5*(correct_tasks/total_tasks), 2)
            if foil <= 2:
                foil = 2
            elif foil >=5:
                foil = 5

        stop_btn = False
        

        user_entry.config(state="disabled")
        hint_button.config(state="disabled")
        task_frame.pack_forget()
        result_frame.pack_forget()
        stats_frame = tk.Frame(root, bg="white")
        stats_frame.pack(padx=20, pady=20)

        if total_tasks > 1: #Убираем заданее, которое может появится на последней секунде ("Оценка в пользу ученика")
            total_tasks -= 1

        stats_label = tk.Label(stats_frame, text=f"Вы решили {total_tasks} задач за {st_time_limit} секунд! \n{correct_tasks} из них были правильными.\n\nОценка: {foil}", font=("Courier New", 24), bg="white")
        stats_label.pack()
        restart_button = tk.Button(stats_frame, text="🜆 Restart?", font=("Courier New", 16), command=restart_test, width=20, relief='ridge',activebackground='white',background='white')
        restart_button.pack(pady=10)
        menu_button = tk.Button(stats_frame, text="🜅 back to menu", font=("Courier New", 16), command=mainmenu, width=20, relief='groove',activebackground='white',background='white')
        menu_button.pack(pady=10)
    else:
        time_limit -= 1
        timer_id = root.after(1000, update_timer, time_limit)  # Initialize timer_id here

def generate_task():
    global numbers, operators, result
    
    num_count = random.randint(2, 5)
    numbers = [random.randint(-64, 256) for _ in range(num_count)]

    if total_tasks <= 5:
        operators = [random.choice(["+", "-"]) for _ in range(num_count-1)]
    else:
        operators = [random.choice(["+", "-", "*", "/"]) for _ in range(num_count-1)]

    expr = ""
    expr_print = ""

    for i in range(num_count-1):
        operator = operators[i]
        
        if operator == '/':
            operator = ':'
        elif operator == '3.14':
            operator = 'π'
        
        expr += f"({numbers[i]} {operators[i]} "
        expr_print += f"({numbers[i]} {operator} "
    
    expr += f"{numbers[-1]}" + ")" * (num_count-1)
    expr_print += f"{numbers[-1]}" + ")" * (num_count-1)
    
    try:
        result = round(eval(expr), 2)
        
        if result > 256000 or result < -256000:
            print('Ответ превышает стандарт, повторная генерация!')
            generate_task()  # Выбираем другие числа
            return

        print(result)
        
    except ZeroDivisionError:
        generate_task()
        return
    
    numbers_str = " ".join(str(num) for num in numbers)
    task_label.config(text=f"Текущий пример #{total_tasks}\n\n{expr_print} =")

def check_answer():
    global time_limit, total_tasks,score, correct_tasks, foil,hints,score,total_tasks,correct_tasks, foil,hints,stats_frame
    try:
        user_answer = (user_entry.get())
        if user_answer == 'skip':
            answer_label.config(text="\nПропущено!\nОтвет: " + str(result), fg='red', font=('consolas', 12))
        else:
            user_answer = float(user_answer)

            if user_answer == result:
                score += 1
                hints += 0.25
                time_limit = max(time_limit+10, 90*60)  # Update the maximum time_limit value to 90 minutes
                correct_tasks += 1
                total_tasks += 1
                score_label.config(text="Score: " + str(score))
                result_text = f"\nCorrect!\n"
                hint_button.configure(text=f"Hint: {hints}")
                answer_label.config(text=result_text, fg='green', font=('Courier New', 12))

            else:
                result_text = f"Incorrect!\nYour answer: {user_answer}\nCorrect answer: {result}"
                total_tasks += 1
                hint_button.configure(text=f"Hint: {hints}")
                answer_label.config(text=result_text, fg='red', font=('Courier New', 12))

        user_entry.delete(0, tk.END)
        generate_task()

    except ValueError:
        result_text = '\nThe received response is not supported!\n'
        answer_label.config(text=result_text, fg='red', font=('Courier New', 12))

        user_entry.delete(0, tk.END)

#devMenu

def devMenu_(event):
    global devMenu,devMenu_logs,score,hints,result

    print('devMenu - open')
    devMenu = tk.Tk()
    devMenu.title("")
    devMenu.geometry("400x300")
    devMenu.wm_minsize(400, 300)
    devMenu.resizable(False,False)
    devMenu.configure(background='black')

    #devMenu - labels
    
    devLabel=tk.Label(devMenu, text='ДебагМеню: {',background='black',foreground='white',relief='flat',font=('Courier New', 16))
    devLabel.place(y='20',x='20')

    #devMenu - buttons

    score_hack=tk.Button(devMenu, text='+1 score',background='black',foreground='white',relief='flat',activebackground='black',activeforeground='green',font=('Courier New', 10),command=scoreHack)
    score_hack.place(y='60',x='20')
    hint_hack=tk.Button(devMenu, text='+1 hints',background='black',foreground='white',relief='flat',activebackground='black',activeforeground='green',font=('Courier New', 10),command=hintHack)
    hint_hack.place(y='60',x='120')
    answ_hack=tk.Button(devMenu, text='Open answers',background='black',foreground='white',relief='flat',activebackground='black',activeforeground='green',font=('Courier New', 10),command=answerHack)
    answ_hack.place(y='60',x='240')

    #devMenu - logs

    devMenu_logs=tk.Text(devMenu, height=9, width=9, font=("Courier New", 11), relief='ridge',background='black',foreground='white')
    devMenu_logs.place(y='90',x='20',height='200',width='360')
    devMenu_logs.insert(tk.END, 'logs open')

    devMenu.protocol("WM_DELETE_WINDOW", devMenu_close)  # Привязка обработчика события закрытия окна
    devMenu.mainloop()

def devMenu_close():
    print('devMenu - close')
    devMenu.destroy()

#Dev Menu Functions
def scoreHack():
    global score,score_label
    score += 1
    score_label.config(text="Score: " + str(score))
    devMenu_logs.insert(tk.END, f'> score added: now = {score}')
    
def hintHack():
    global hints,hint_button
    hints += 1
    hint_button.configure(text=f"Hint: {hints}")
    devMenu_logs.insert(tk.END, f'> hint added: now = {hints}')
    
def answerHack():
    global correct_tasks,user_entry,total_tasks
    user_entry.delete(0, tk.END)
    devMenu_logs.insert(tk.END, f'> Answer = {result}')

#StartWindow()

mainmenu()

##########