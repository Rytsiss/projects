import tkinter as tk
import os
import random
from tkinter import messagebox
import winsound

if  not os.path.isfile('mathsGameLeaderboardEasy.txt'):
    print('File does not exist')
    with open('mathsGameLeaderboardEasy.txt','w') as f:
        f.write('')
    with open('mathsGameLeaderboardIntermediate.txt','w') as f:
        f.write('')
    with open('mathsGameLeaderboardAdvanced.txt','w') as f:
        f.write('')


score=0
GameLevel=0
class myapp():
    def __init__(self,root):
        self.window1=root
        self.entryName()#must move after the end of quenstions
        self.leaderboard()
        self.background()
        self.playbut()
    def background(self):
        width= self.window1.winfo_screenwidth()               
        height= self.window1.winfo_screenheight()               
        self.window1.geometry(f"{width}x{height}")
        self.window1.title("math games")
        self.window1.configure(background="RoyalBlue")
        label1=tk.Label(self.window1, text="MATH GAMES", font=("Rockwell Extra Bold", 50), background="RoyalBlue", foreground="DarkOrange")
        label1.pack()


  #play button and difficulty select

    def playbut (self):

        playbutton=tk.Button(self.window1, text="PLAY", font=("Rockwell Extra Bold", 25), width=17, height=2, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        playbutton.place(x=550, y=300)
        playbutton.configure(command=self.play)

    def play(self):
        winsound.Beep(1000,100)
        self.window=tk.Toplevel()
        width= self.window.winfo_screenwidth()               
        height=self.window.winfo_screenheight()               
        self.window.geometry(f"{width}x{height}")
        self.window.title("math games")
        self.window.configure(background="RoyalBlue")

        buttonframe=tk.Frame(self.window, pady=150, background="RoyalBlue")
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        label=tk.Label(self.window, text="MATH GAMES", font=("Rockwell Extra Bold", 50), background="RoyalBlue", foreground="DarkOrange")
        label.pack()


        inslabel=tk.Label(self.window, text="select difficulty", font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue")
        inslabel.place(x=0, y=190)

    
        button1=tk.Button(buttonframe, text="Easy", font=("Rockwell Extra Bold", 25), width=20, height=3, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        button1.grid(row=0, column=0, sticky=tk.W+ tk.E)
        button1.configure(command=self.button1_pushed)    
        button2=tk.Button(buttonframe, text="Intermediate", font=("Rockwell Extra Bold", 25), width=20, height=3, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        button2.grid(row=0, column=1, sticky=tk.W+ tk.E)
        button2.configure(command=self.button2_pushed)
        button3=tk.Button(buttonframe, text="Advanced", font=("Rockwell Extra Bold", 25), width=20, height=3, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        button3.grid(row=0, column=2, sticky=tk.W+ tk.E)
        button3.configure(command=self.button3_pushed)
        buttonframe.pack(fill="x")

   
    def button1_pushed(self):
        winsound.Beep(1000,100)
        global GameLevel,score
        score=0
        GameLevel=1
        self.window.destroy()
        root = tk.Tk()
        MathQuizGame(root)
        root.mainloop()
        self.window.destroy()
        


    def button2_pushed(self):
        winsound.Beep(1000,100)
        global GameLevel,score
        GameLevel=2
        score=0
        self.window.destroy()
        root = tk.Tk()
        MathQuizGame(root)
        root.mainloop()
        


    def button3_pushed(self):
        winsound.Beep(1000,100)
        global GameLevel,score
        GameLevel=3 
        score=0
        self.window.destroy()
        root = tk.Tk()
        MathQuizGame(root)
        root.mainloop()
        
        
    def difficultySelect(self):
        global GameLevel
        if GameLevel==1:
            difficultySelect='mathsGameLeaderboardEasy'
        elif GameLevel==2:
            difficultySelect='mathsGameLeaderboardIntermediate'
        else :
            difficultySelect='mathsGameLeaderboardAdvanced'
        return difficultySelect 
            


 #enty and get users name and checks if username already exist

    def entryName(self):
        entrytext=tk.Label(self.window1,text='name and save your score:',font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue")
        entrytext.place(x=0,y=65)
        self.entr=tk.Entry(self.window1,text='name:',font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue")
        self.entr.place(x=0,y=101)
        self.button=tk.Button(self.window1,text='✓',font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue",command=self.displayPlayer)
        self.button.place(x=200,y=93)

    def displayPlayer(self): 
        winsound.Beep(1000,100)  
        global score
        
        name=self.entr.get()
        with open(f'{self.difficultySelect()}.txt', 'r') as file:
            rd=file.read()
            if not name in rd:
                okname=tk.Label(self.window1,text='                              ',font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue",fg='red')
                okname.place(x=0,y=150)
                with open(f'{self.difficultySelect()}.txt','a') as f:
                    field_length = 15
                    padded_name = name.ljust(field_length)
                    f.write(f'\n{padded_name}')
                    f.write(f'{score}')

                    
            else:
                changeName=tk.Label(self.window1,text='this name already exist',font=("Rockwell Condensed", 17, "bold"), background="RoyalBlue",fg='red')
                changeName.place(x=0,y=150)  
                

 #leaderboad general 


    def leaderboard(self):   
        self.leadbutton=tk.Button(self.window1, text="LEADERBOARD", font=("Rockwell Extra Bold", 25), width=17, height=2, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        self.leadbutton.place(x=550, y=400)
        self.leadbutton.configure(command=self.leadbutton_pushed)

        
    def leadbutton_pushed(self):
        winsound.Beep(1000,100)
        window2=tk.Toplevel()             
        window2.geometry("500x500")
        window2.title("leaderboard")
        window2.configure(background="dodgerblue1")
        label2=tk.Label(window2, text=" SELECT LEADERBOARD", font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")

        label2.place(x=60)
        lead_e_button=tk.Button(window2, text="Easy", font=("Rockwell Extra Bold", 15), width=12, height=2, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        lead_e_button.place(x=155, y=129)
        lead_e_button.configure(command=self.leadbutton_pushedEZ)
        lead_i_button=tk.Button(window2, text="Intermediate", font=("Rockwell Extra Bold", 15), width=12, height=2, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        lead_i_button.place(x=155, y=200)
        lead_i_button.configure(command=self.leadbutton_pushedINT)
        lead_a_button=tk.Button(window2, text="Advanced", font=("Rockwell Extra Bold", 15), width=12, height=2, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise")
        lead_a_button.place(x=155, y=270)
        lead_a_button.configure(command=self.leadbutton_pushedADV)
    
        
    def leadbutton_pushedEZ(self): 
        winsound.Beep(1000,100)
        newwindow=tk.Toplevel()
        newwindow.geometry('320x500')
        newwindow.title("Leaderboard(Easy)")
        newwindow.configure(background="dodgerblue1")  
        label2=tk.Label(newwindow, text=self.usersReader1(), font=("Courier", 20,'bold'), background="dodgerblue1", foreground="black")
        label2.place(x=1)
        label3=tk.Label(newwindow, text='NAME:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label3.place(x=1)
        label4=tk.Label(newwindow, text='SCORE:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label4.place(x=200)
        

    def usersReader1(self):
            filename='mathsGameLeaderboardEasy.txt'
            with open(filename, 'r') as f:
                data=f.read()
                return data
            
    def leadbutton_pushedINT(self): 
        winsound.Beep(1000,100)
        newwindow=tk.Toplevel()
        newwindow.geometry('320x500')
        newwindow.title("Leaderboard(Intermediate)")
        newwindow.configure(background="dodgerblue1")  
        label2=tk.Label(newwindow, text=self.usersReader2(), font=("Courier", 20,'bold'), background="dodgerblue1", foreground="black")
        label2.place(x=1)
        label3=tk.Label(newwindow, text='NAME:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label3.place(x=1)
        label4=tk.Label(newwindow, text='SCORE:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label4.place(x=200)

    def usersReader2(self):
            filename='mathsGameLeaderboardIntermediate.txt'
            with open(filename, 'r') as f:
                data=f.read()
                return data

    def leadbutton_pushedADV(self): 
        winsound.Beep(1000,100)
        newwindow=tk.Toplevel()
        newwindow.geometry('320x500')
        newwindow.title("Leaderboard(Advanced)")
        newwindow.configure(background="dodgerblue1")  
        label2=tk.Label(newwindow, text=self.usersReader3(), font=("Courier", 20,'bold'), background="dodgerblue1", foreground="black")
        label2.place(x=1)
        label3=tk.Label(newwindow, text='NAME:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label3.place(x=1)
        label4=tk.Label(newwindow, text='SCORE:', font=("Rockwell Extra Bold", 20), background="dodgerblue1", foreground="DarkOrange")
        label4.place(x=200)

    def usersReader3(self):
            filename='mathsGameLeaderboardAdvanced.txt'
            with open(filename, 'r') as f:
                data=f.read()
                return data   



    
            

num1=0
num2=0
operator=''
class MathQuizGame():
    def __init__(self, root):
        self.root = root
        width= root.winfo_screenwidth()               
        height= root.winfo_screenheight() 
        self.root.geometry((f"{width}x{height}"))
        self.root.configure(background="RoyalBlue")
        self.root.title("Math Quiz Game")
        self.difficulty_var = tk.StringVar()
        self.current_question()
        self.generate_question()
        self.display_question()


    def generate_question(self):
        global GameLevel,num1,num2,operator

        if GameLevel == 1:
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
        elif GameLevel == 2:
            num1 = random.randint(5, 10)
            num2 = random.randint(5, 10)
        else:
            num1 = random.randint(10, 15)
            num2 = random.randint(10, 15)

        operator = random.choice(['+', '-', '*', '/'])
        return operator,num1,num2
    

        
    def current_question(self):
        global num1,num2,operator
        current_question=f"{num1} {operator} {num2}"
        return current_question

    def display_question(self):
        question_label = tk.Label(self.root, text=f"What is {self.current_question()}  ?  ", font=("Rockwell Condensed", 40, "bold"), background="RoyalBlue" )
        question_label.place(x=580,y=270)

        answer_entry = tk.Entry(self.root, width=20, font=("Rockwell Condensed", 35))
        answer_entry.place(x=580,y=330)

        submit_button = tk.Button(self.root, text="Submit Answer", command=lambda: self.check_answer(answer_entry.get()), font=("Rockwell Condensed", 30), width=16, height=1, borderwidth=5, background="SandyBrown", activebackground="orangered", relief="raise") 
        submit_button.place(x=620,y=410)

    def check_answer(self, user_answer):
        winsound.Beep(1000,100)
        global score
        try:
            user_answer = float(user_answer)
            correct_answer = round(eval(self.current_question()), 1)

            if user_answer == correct_answer:
                tk.Label(self.root,text='correct!',fg='darkgreen', bg="RoyalBlue", font=("Arial", 40, "bold")).place(x=650,y=550)
                score+=1
                self.generate_question()
                self.display_question()#Εδω εκανα την αλλαγη για δινει νεα ερωτηση
            else:
                messagebox.showerror("Incorrect", f"Sorry, the correct answer was {correct_answer}. Your current score is {score}.")
                self.root.destroy()
                
                
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid numerical answer.")
    
            

            
if __name__ == "__main__":
    root = tk.Tk()
    myapp(root)
    root.mainloop()