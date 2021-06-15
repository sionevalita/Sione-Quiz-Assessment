from tkinter import*
import random
from PIL import ImageTk, Image
global score

names_list=[]
asked_algebra=[]
asked_trig=[]
asked_calculus=[]

algebra_questions_answers ={
  1:["What does a linear graph look like?",
  'A donut',
  'A straight line',
  'A long curve',
  'Squilliams forehead wrinkles',
  'A straight line',
  2], #index 6 will show the index position of the right answer

  2:["What shape is a parabolic graph?",
  'A straight line',
  'A circle',
  'A curve',
  'Godzilla',
  'A curve',
  3],#index 6 will show the index position of the right answer

  3:["12=3x, To solve for x what do you do?",
  'multiply x by 3',
  'divide 3 to both sides',
  'divide 3 to just 3x',
  'run around the street',
  'divide 3 to both sides',
  2],#index 6 will be the index position of the right algebra_questions_answers

  4:["When solving for a variable in an equation, what do you use?",
  'A car',
  'BEDMAS',
  'Trigonometry',
  'Statistics',
  'BEDMAS',
  2],#index 6 will be the index position of the right algebra_questions_answers

  5:["Solve for y: 3y=18",
  'y=2',
  'no possible answer',
  'y=6',
  'y=8',
  'y=6',
  3]#index 6 will be the index position of the right answer
}


trigonometry_questions_answers={
1:["What is a more efficient way of remembering the trigonometry functions?",
'Google it',
'S0H CUT T0@',
'SOH CAH TOA',
'BEDMAS',
'SOH CAH TOA',
3],#index 6 will be the index position of the right algebra_questions_answers

2:["What is the longest side of a triangle called?",
'hypotenuse',
'adjacent',
'the longest side',
'opposite',
'hypotenuse',
1],#index 6 will be the index position of the right algebra_questions_answers

3:["What does the theta symbol Ø mean?",
'A zero',
'Angle of the triangle',
'It means nothing',
'The tallest point in a triangle',
'Angle of the triangle',
2],#index 6 item 7 is the index position of the right answer

4:["If the angle of a triangle is 90° and the hypotenuse is 30cm, how do you calculate opposite and how long is it??",
'Opposite = 30 x cos90 = 0cm',
'Opposite = 90 x tan30 = 51.96cm',
'Opposite = 60cm because I said so',
'Opposite = 30 x sin90= 30cm',
'Opposite = 30 x cos90 = 0cm',
1],#index 6 item 7 will be the index position of the right answer

5:["The side next to the angle is the ________ and the side opposite to the angle is ________",'hypotenuse and opposite',
'adjacent and opposite',
'opposite and hypotenuse',
'opposite and opposite',
'adjacent and opposite',
1],#index 6 item 7 will be the index position of the right answer
}


calculus_questions_answers={
1:["Based on Degree two function: ? x (? f) = ?",
'0',
'1',
'-1',
'None of these',
'0',
1],#index 6 item 7 will be the index position of the right answer

2:["Onto function is also called",
'Injective function',
'Surjective function',
'Bijective function',
'None of these',
'Surjective function',
2],#index 6 item 7 will be the index position of the right answer

3:["An ordered pair is represented by",
'(Output, Output)',
'(Input, Input)',
'(Output, Input)',
'(Input, Output)',
'(Input, Output)',
4],#index 6 item 7 will be the index position of the right answer

4:["Bijective function is also called as",
'One to one function',
'Many to one function',
'Onto Function',
'One-one correspondence',
'One-one correspondence',
4],#index 6 item 7 will be the index position of the right answer

5:["If (a, b) ∈ R then (b, a) ∈ R, for all a & b ∈ A, then a relation R on a set A is",
'Inverse Relation',
'Reflexive Relation',
'Symmetric Relation',
'Transitive Relation',
'Symmetric Relation',
3],#index 6 item 7 will be the index position of the right answer
}

def algebra_randomiser():
  global algebra_qnum
  algebra_qnum = random.randint(1,5)
  if algebra_qnum not in asked_algebra:
    asked_algebra.append(algebra_qnum)
  elif algebra_qnum in asked_algebra:
    algebra_randomiser()

def trig_randomiser():
  global trig_qnum
  trig_qnum = random.randint(1,5)
  if trig_qnum not in asked_trig:
    asked_trig.append(trig_qnum)
  elif trig_qnum in asked_trig:
    trig_randomiser() 

def calculus_randomiser():
  global calculus_qnum
  calculus_qnum = random.randint(1,5)
  if calculus_qnum not in asked_calculus:
    asked_calculus.append(calculus_qnum)
  elif calculus_qnum in asked_calculus:
    calculus_randomiser()
  


class QuizStarter:
    def __init__(self, master):
        background_color="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label widget for heading
        self.heading_label = Label(self.quiz_frame, text = "MRGS Math Quiz", font = ("Tw Cent Mt", "18", "bold"),bg = background_color)
        self.heading_label.grid(row=0)

        #Label for user prompt
        self.user_label = Label (self.quiz_frame, text = "Please enter your name:", font =("Tw Cent Mt", "10"),bg = background_color)
        self.user_label.grid(row=2,pady=9)

        #users input is taken by an entry Widget
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3, pady=10)

        #exit button for rage quitters      
        self.exit_button = Button(self.quiz_frame, text="Exit", bg= "red", command=self.quiz_exit)
        self.exit_button.grid(row=5)
        #self.exit_button.place(x=-90, y=208)

        #continue Button
        self.continue_button = Button(self.quiz_frame, text="continue", bg="#d3d3d3", command=self.name_collection)
        self.continue_button.grid(row=4)

        #image
        self.heading_image = Image.open("mrgs_logo.png")
        self.heading_image = self.heading_image.resize((100,100), Image.ANTIALIAS)
        self.heading_image = ImageTk.PhotoImage(self.heading_image)

       #image Label
        self.image_label = Label(self.quiz_frame, image=self.heading_image, bg=background_color)
       #self.heading_image.grid(row=0, column=1)
        self.image_label.grid(row=1)

    #command for continue button
    def name_collection(self):
       name = self.entry_box.get()
       names_list.append(name)
       print(names_list)
       self.quiz_frame.destroy()
       QuizPicker(root)
    
    #command for exit button
    def quiz_exit(self):
      exit()



#page where user will pick which topic they want to learn
class QuizPicker:
    def __init__(self, master):
        background_color="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label=Label(self.quiz_frame, text="Hello " + names_list[0] + ", what topic do you want to learn about?",font=("Tw Cent Mt", "14", "bold"))
        self.heading_label.grid(row=1)

        self.algebra_button = Button(self.quiz_frame, text="Algebra(Level 1)", command=self.quiz_algebra)
        self.algebra_button.grid(row= 2)

        self.trigonometry_button = Button(self.quiz_frame, text="Trigonometry", command=self.quiz_trig)
        self.trigonometry_button.grid(row=3)

        self.calculus_button = Button(self.quiz_frame, text="Calculus", command = self.Quiz_calculus)
        self.calculus_button.grid(row=4)

        #command for algebra button that directs the user to the algebra quiz 
    def quiz_algebra(self):
        self.quiz_frame.destroy()
        QuizAlgebra(root)

        #command for trig button that directs the user to the trigonometry quiz
    def quiz_trig(self):
        self.quiz_frame.destroy()
        QuizTrig(root)

        #command for calculus button that directs the user to the calculus quiz 
    def Quiz_calculus(self):
        self.quiz_frame.destroy()
        QuizCalculus(root)




class QuizAlgebra:
    def __init__(self, master):
        background_color="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #randomiser will randomly pick a question number
        algebra_randomiser()

        #Question label widget 
        self.question_label = Label(self.quiz_frame, text = algebra_questions_answers[algebra_qnum][0],bg=background_color, font=("Tw Cent Mt", "11", "bold", "italic"))
        self.question_label.grid(row = 0)

        #holds the value of radio buttons
        self.var1 = IntVar()

        #radio button 1
        self.ac1 = Radiobutton(self.quiz_frame, text=algebra_questions_answers[algebra_qnum][1], font = ("Tw Cent Mt", "11", "bold"),value = 1, pady = 10,variable=self.var1, indicator = 0)
        self.ac1.grid(row = 1)

        #radio button 2
        self.ac2 = Radiobutton(self.quiz_frame, text = algebra_questions_answers[algebra_qnum][2], font = ("Tw Cent Mt", "11", "bold"),value = 2, pady = 10,variable=self.var1, indicator = 0)
        self.ac2.grid(row = 2)

        #radio button 3
        self.ac3= Radiobutton(self.quiz_frame, text=algebra_questions_answers[algebra_qnum][3], font = ("Tw Cent Mt", "11", "bold"),value = 3, pady = 10, variable=self.var1, indicator = 0)
        self.ac3.grid(row = 3)

        #radio button 4
        self.ac4 = Radiobutton(self.quiz_frame, text=algebra_questions_answers[algebra_qnum][4], font = ("Tw Cent Mt", "11", "bold"),value=4, pady=10, variable=self.var1, indicator = 0)
        self.ac4.grid(row=4)

        #confirm Button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", command = self.algebra_test_progress)
        self.confirm_button.grid(row=5)

        #score label
        self.score_label = Label(self.quiz_frame, text="SCORE", bg=background_color)
        self.score_label.grid(row=6, pady=10)

    #Method to randomise question label and radio buttons 
    def algebra_questions_setup(self):
      algebra_randomiser()
      self.var1.set(0)
      self.question_label.config(text=algebra_questions_answers[algebra_qnum][0])
      self.ac1.config(text=algebra_questions_answers[algebra_qnum][1])
      self.ac2.config(text=algebra_questions_answers[algebra_qnum][2])
      self.ac3.config(text=algebra_questions_answers[algebra_qnum][3])
      self.ac4.config(text=algebra_questions_answers[algebra_qnum][4])

    #This is the confirm button method that will take care of the quiz progress and will check if the answer choice the user picked is right or wrong
    def algebra_test_progress(self):
      score=0
      score_label = self.score_label
      choice = self.var1.get()
      if len(asked_algebra)>4:
        if choice == algebra_questions_answers[algebra_qnum][6]:
          score+=1
          score_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          #self.algebra_questions_setup()
        else:
          score+=0
          score_label.configure(text="The correct answer was: " + algebra_questions_answers[algebra_qnum][5])
          self.confirm_button.config(text = "Confirm")
          #self.algebra_questions_setup()
          
      else:
        if choice == 0:
          score_label.configure(text = "You have not selected an option.")
          choice = self.var1.get()
        else:#if choice is made
          if choice == algebra_questions_answers[algebra_qnum][6]: 
                    score+=1
                    score_label.configure(text=score) 
                    self.confirm_button.config(text="Confirm")
                    self.algebra_questions_setup()
          else:
            score+=0
            score_label.configure(text = "The correct answer was: " + algebra_questions_answers[algebra_qnum][5])
            self.confirm_button.configure(text="Confirm")
            self.algebra_questions_setup()
          



class QuizTrig:
    def __init__(self,master):
        background_color = "#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #randomiser will randomly pick a question number
        trig_randomiser()

        #Question label widget 
        self.question_label = Label(self.quiz_frame, text = trigonometry_questions_answers[trig_qnum][0],bg=background_color)
        self.question_label.grid(row=0)
         #holds the value of radio buttons
        self.var1=IntVar()

        #radio button 1
        self.ac1= Radiobutton(self.quiz_frame, text=trigonometry_questions_answers[trig_qnum][1], font=("Tw Cent Mt", "11", "bold"),value=1, pady=10,variable=self.var1, indicator=0)
        self.ac1.grid(row=1)

        #radio button 2
        self.ac2= Radiobutton(self.quiz_frame, text=trigonometry_questions_answers[trig_qnum][2], font=("Tw Cent Mt", "11", "bold"),value=2, pady=10,variable=self.var1, indicator=0)
        self.ac2.grid(row=2)

        #radio button 3
        self.ac3= Radiobutton(self.quiz_frame, text=trigonometry_questions_answers[trig_qnum][3], font=("Tw Cent Mt", "11", "bold"),value=3, pady=10, variable=self.var1, indicator=0)
        self.ac3.grid(row=3)

        #radio button 4
        self.ac4= Radiobutton(self.quiz_frame, text=trigonometry_questions_answers[trig_qnum][4], font=("Tw Cent Mt", "11", "bold"),value=4, pady=10, variable=self.var1, indicator=0)
        self.ac4.grid(row=4)

        #confirm Button
        self.confirm_button = Button(self.quiz_frame, text="Confirm",command=self.trig_test_progress)
        self.confirm_button.grid(row=5)

        #score label
        self.score_label = Label(self.quiz_frame, text="SCORE", bg=background_color)
        self.score_label.grid(row=6, pady=10)

    #Method that will setup questions and answer choices when continue button is pressed
    def trig_questions_setup(self):
      trig_randomiser()
      self.question_label.config(text=trigonometry_questions_answers[trig_qnum][0])
      self.ac1.config(text=trigonometry_questions_answers[trig_qnum][1])
      self.ac2.config(text=trigonometry_questions_answers[trig_qnum][2])
      self.ac3.config(text=trigonometry_questions_answers[trig_qnum][3])
      self.ac4.config(text=trigonometry_questions_answers[trig_qnum][4])

    #This is the confirm button method that will take care of the quiz progress and will check if the answer choice the user picked is right or wrong
    def trig_test_progress(self):
      score=0
      score_label = self.score_label
      choice = self.var1.get()
      if len(asked_trig)>4:
        if choice == trigonometry_questions_answers[trig_qnum][6]:
          score+=1
          score_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          score_label.configure(text="The correct answer was: " + trigonometry_questions_answers[trig_qnum][5])
          self.confirm_button.config(text = "Confirm")
          
      else:
        if choice == 0:
          score_label.configure(text = "You have not selected an option.")
          choice = self.var1.get()
        else:#if choice is made
          if choice == trigonometry_questions_answers[trig_qnum][6]: 
                    score+=1
                    score_label.configure(text=score) 
                    self.confirm_button.config(text="Confirm")
                    self.trig_questions_setup()
          else:
            score+=0
            score_label.configure(text = "The correct answer was: " + trigonometry_questions_answers[trig_qnum][5])
            self.confirm_button.configure(text="Confirm")
            self.trig_questions_setup()






class QuizCalculus:
  def __init__(self, master):
        background_color="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #randomiser will randomly pick a question number
        calculus_randomiser()

        #Question label widget 
        self.question_label = Label(self.quiz_frame, text = calculus_questions_answers[calculus_qnum][0],bg=background_color)
        self.question_label.grid(row=0)

        #holds the value of radio buttons
        self.var1=IntVar()

        #radio button 1
        self.ac1= Radiobutton(self.quiz_frame, text=calculus_questions_answers[calculus_qnum][1], font=("Tw Cent Mt", "11", "bold"),value=1, pady=10,variable=self.var1, indicator=0)
        self.ac1.grid(row=1)

        #radio button 2
        self.ac2= Radiobutton(self.quiz_frame, text=calculus_questions_answers[calculus_qnum][2], font=("Tw Cent Mt", "11", "bold"),value=2, pady=10,variable=self.var1, indicator=0)
        self.ac2.grid(row=2)

        #radio button 3
        self.ac3= Radiobutton(self.quiz_frame, text=calculus_questions_answers[calculus_qnum][3], font=("Tw Cent Mt", "11", "bold"),value=3, pady=10, variable=self.var1, indicator=0)
        self.ac3.grid(row=3)

        #radio button 4
        self.ac4= Radiobutton(self.quiz_frame, text=calculus_questions_answers[calculus_qnum][4], font=("Tw Cent Mt", "11", "bold"),value=4, pady=10, variable=self.var1, indicator=0)
        self.ac4.grid(row=4)

        #confirm Button
        self.confirm_button = Button(self.quiz_frame, text="Confirm",command = self.calculus_test_progress)
        self.confirm_button.grid(row=5)

        #score Label
        self.score_label = Label(self.quiz_frame, text="SCORE", bg=background_color)
        self.score_label.grid(row=6, pady=10)

        #Method that will setup questions and answer choices when continue button is pressed
  def calculus_questions_setup(self):
      calculus_randomiser()
      self.question_label.config(text=calculus_questions_answers[calculus_qnum][0])
      self.ac1.config(text=calculus_questions_answers[calculus_qnum][1])
      self.ac2.config(text=calculus_questions_answers[calculus_qnum][2])
      self.ac3.config(text=calculus_questions_answers[calculus_qnum][3])
      self.ac4.config(text=calculus_questions_answers[calculus_qnum][4])

    #This is the confirm button method that will take care of the quiz progress and will check if the answer choice the user picked is right or wrong
  def calculus_test_progress(self):
        score=0
        score_label = self.score_label
        choice = self.var1.get()
        if len(asked_calculus)>4:
          if choice == calculus_questions_answers[calculus_qnum][6]:
            score+=1
            score_label.configure(text=score)
            self.confirm_button.config(text="Confirm")
          else:
            score+=0
            score_label.configure(text="The correct answer was: " + calculus_questions_answers[calculus_qnum][5])
            self.confirm_button.config(text = "Confirm")
            
        else:
          if choice == 0:
            score_label.configure(text = "You have not selected an option.")
            choice = self.var1.get()
          else:#if choice is made
            if choice == calculus_questions_answers[calculus_qnum][6]: 
                      score+=1
                      score_label.configure(text=score) 
                      self.confirm_button.config(text="Confirm")
                      self.calculus_questions_setup()
            else:
              score+=0
              score_label.configure(text = "The correct answer was: " + calculus_questions_answers[calculus_qnum][5])
              self.confirm_button.configure(text="Confirm")
              self.calculus_questions_setup()

      
















#***********starting point************#
if __name__ == "__main__":
  root = Tk()
  root.title("MRGS Maths Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#window doesn't dissapear