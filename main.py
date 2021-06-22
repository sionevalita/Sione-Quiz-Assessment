from tkinter import*
import random
from PIL import ImageTk, Image
global score

#list that the user's name will be stored in
names_list = []

#list that all the asked algebra questions will be stored in
asked_algebra = []

#list that all the asked trigonometry questions will be stored in
asked_trig = []

#list that all the asked calculus questions will be stored in
asked_calculus = []


#dictionary that stores the questions and answer for algebra questions and answers
algebra_questions_answers = {
  1:["What does a linear graph look like?",#index 0, item 1 will be the question
  'A donut',#index 1, item 2 will be the first answer choice
  'A straight line',#index 2, item 3 will be the second answer choice
  'A long curve',#index 3, item 4 will be the third answer choice
  'Squilliams forehead wrinkles',#index 4, item 5 will be the fourth answer choice
  'A straight line',#index 5, item 6 will be the right answer
  2], #index 6, item 7 will show the index position of the right answer

  2:["What shape is a parabolic graph?",#index 0, item 1 will be the question
  'A straight line',#index 1, item 2 will be the first answer choice
  'A circle',#index 2, item 3 will be the second answer choice
  'A curve',#index 3, item 4 will be the third answer choice
  'Godzilla',#index 4, item 5 will be the fourth answer choice
  'A curve',#index 5, item 6 will be the right answer
  3],#index 6, item 7 will show the index position of the right answer

  3:["12=3x, To solve for x what do you do?",#index 0, item 1 will be the question
  'multiply x by 3',#index 1, item 2 will be the first answer choice
  'divide 3 to both sides',#index 2, item 3 will be the second answer choice
  'divide 3 to just 3x',#index 3, item 4 will be the third answer choice
  'run around the street',#index 4, item 5 will be the fourth answer choice
  'divide 3 to both sides',#index 5, item 6 will be the right answer
  2],#index 6, item 7 will show the index position of the right answer

  4:["When solving for a variable in an equation, what do you use?",#index 0, item 1 will be the question
  'A car',#index 1, item 2 will be the first answer choice
  'BEDMAS',#index 2, item 3 will be the second answer choice
  'Trigonometry',#index 3, item 4 will be the third answer choice
  'Statistics',#index 4, item 5 will be the fourth answer choice
  'BEDMAS',#index 5, item 6 will be the right answer
  2],#index 6, item 7 will show the index position of the right answer

  5:["Solve for y: 3y=18",#index 0, item 1 will be the question
  'y=2',#index 1, item 2 will be the first answer choice
  'no possible answer',#index 2, item 3 will be the second answer choice
  'y=6',#index 3, item 4 will be the third answer choice
  'y=8',#index 4, item 5 will be the fourth answer choice
  'y=6',#index 5, item 6 will be the right answer
  3]#index 6, item 7 will show the index position of the right answer
}


#dictionary for trigonometry questions and answers
trigonometry_questions_answers = {
1:["What is a more efficient way of remembering the trigonometry functions?",#index 0, item 1 will be the question
'Google it',#index 1, item 2 will be the first answer choice
'S0H CUT T0@',#index 2, item 3 will be the second answer choice
'SOH CAH TOA',#index 3, item 4 will be the third answer choice
'BEDMAS',#index 4, item 5 will be the fourth answer choice
'SOH CAH TOA',#index 5, item 6 will be the right answer
3],#index 6 will be the index position of the right algebra_questions_answers

2:["What is the longest side of a triangle called?",#index 0, item 1 will be the question
'hypotenuse',#index 1, item 2 will be the first answer choice
'adjacent',#index 2, item 3 will be the second answer choice
'the longest side',#index 3, item 4 will be the third answer choice
'opposite',#index 4, item 5 will be the fourth answer choice
'hypotenuse',#index 5, item 6 will be the right answer
1],#index 6 will be the index position of the right algebra_questions_answers

3:["What does the theta symbol Ø mean?",#index 0, item 1 will be the question
'A zero',#index 1, item 2 will be the first answer choice
'Angle of the triangle',#index 2, item 3 will be the second answer choice
'It means nothing',#index 3, item 4 will be the third answer choice
'The tallest point in a triangle',#index 4, item 5 will be the fourth answer choice
'Angle of the triangle',#index 5, item 6 will be the right answer
2],#index 6 item 7 is the index position of the right answer

4:["If the angle of a triangle is 90° and the hypotenuse is 30cm, how do you calculate opposite and how long is it??",#index 0, item 1 will be the question
'Opposite = 30 x cos90 = 0cm',#index 1, item 2 will be the first answer choice
'Opposite = 90 x tan30 = 51.96cm',#index 2, item 3 will be the second answer choice
'Opposite = 60cm because I said so',#index 3, item 4 will be the third answer choice
'Opposite = 30 x sin90= 30cm',#index 4, item 5 will be the fourth answer choice
'Opposite = 30 x cos90 = 0cm',#index 5, item 6 will be the right answer
1],#index 6 item 7 will be the index position of the right answer

5:["The side next to the angle is the ________ and the side opposite to the angle is ________",'hypotenuse and opposite',#index 0, item 1 will be the question
'adjacent and opposite',#index 1, item 2 will be the first answer choice
'opposite and hypotenuse',#index 2, item 3 will be the second answer choice
'opposite and opposite',#index 3, item 4 will be the third answer choice
'opposite and opposite',#index 4, item 5 will be the fourth answer choice
'adjacent and opposite',#index 5, item 6 will be the right answer
1],#index 6 item 7 will be the index position of the right answer
}

#dictionary for calculus questions and answers
calculus_questions_answers={
1:["Based on Degree two function: ? x (? f) = ?",#index 0, item 1 will be the question
'0',#index 1, item 2 will be the first answer choice
'1',#index 2, item 3 will be the second answer choice
'-1',#index 3, item 4 will be the third answer choice
'None of these',#index 4, item 5 will be the fourth answer choice
'0',#index 5, item 6 will be the right answer
1],#index 6 item 7 will be the index position of the right answer

2:["Onto function is also called",#index 0, item 1 will be the question
'Injective function',#index 1, item 2 will be the first answer choice
'Surjective function',#index 2, item 3 will be the second answer choice
'Bijective function',#index 3, item 4 will be the third answer choice
'None of these',#index 4, item 5 will be the fourth answer choice
'Surjective function',#index 5, item 6 will be the right answer
2],#index 6 item 7 will be the index position of the right answer

3:["An ordered pair is represented by",#index 0, item 1 will be the question
'(Output, Output)',#index 1, item 2 will be the first answer choice
'(Input, Input)',#index 2, item 3 will be the second answer choice
'(Output, Input)',#index 3, item 4 will be the third answer choice
'(Input, Output)',#index 4, item 5 will be the fourth answer choice
'(Input, Output)',#index 5, item 6 will be the right answer
4],#index 6 item 7 will be the index position of the right answer

4:["Bijective function is also called as",#index 0, item 1 will be the question
'One to one function',#index 1, item 2 will be the first answer choice
'Many to one function',#index 2, item 3 will be the second answer choice
'Onto Function',#index 3, item 4 will be the third answer choice
'One-one correspondence',#index 4, item 5 will be the fourth answer choice
'One-one correspondence',#index 5, item 6 will be the right answer
4],#index 6 item 7 will be the index position of the right answer

5:["If (a, b) ∈ R then (b, a) ∈ R, for all a & b ∈ A, then a relation R on a set A is",#index 0, item 1 will be the question
'Inverse Relation',#index 1, item 2 will be the first answer choice
'Reflexive Relation',#index 2, item 3 will be the second answer choice
'Symmetric Relation',#index 3, item 4 will be the third answer choice
'Transitive Relation',#index 4, item 5 will be the fourth answer choice
'Symmetric Relation',#index 5, item 6 will be the right answer
3],#index 6 item 7 will be the index position of the right answer
}

#randomiser for algebra that wil randomise the algebra questions and answer choices
def algebra_randomiser():
  global algebra_qnum
  algebra_qnum = random.randint(1,5)
  if algebra_qnum not in asked_algebra:
    asked_algebra.append(algebra_qnum)
  elif algebra_qnum in asked_algebra:
    algebra_randomiser()

#randomiser for trigonometry that will randomise the trigonometry questions and answer choices
def trig_randomiser():
  global trig_qnum
  trig_qnum = random.randint(1,5)
  if trig_qnum not in asked_trig:
    asked_trig.append(trig_qnum)
  elif trig_qnum in asked_trig:
    trig_randomiser() 

#randomiser for calculus that will randomise the calculus questions and answer choices
def calculus_randomiser():
  global calculus_qnum
  calculus_qnum = random.randint(1,5)
  if calculus_qnum not in asked_calculus:
    asked_calculus.append(calculus_qnum)
  elif calculus_qnum in asked_calculus:
    calculus_randomiser()
  

#Starting page of the quiz
class QuizStarter:
    def __init__(self, master):
        background_color = "#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx = 100, pady = 100)
        self.quiz_frame.grid()

        #Label widget for heading
        self.heading_label = Label(self.quiz_frame, text = "MRGS Math Quiz", font = ("Tw Cent Mt", "18", "bold"),bg = background_color)
        self.heading_label.grid(row = 0)

        #Label for user prompt
        self.user_label = Label (self.quiz_frame, text = "Please enter your name:", font = ("Tw Cent Mt", "10"),bg = background_color)
        self.user_label.grid(row = 2,pady = 9)

        #users input is taken by an entry Widget
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row = 3, pady= 10 )

        #exit button for rage quitters      
        self.exit_button = Button(self.quiz_frame, text = "Exit", bg = "red", command = self.quiz_exit)
        self.exit_button.grid(row = 5)
        #self.exit_button.place(x=-90, y=208)

        #continue Button
        self.continue_button = Button(self.quiz_frame, text = "continue", bg = "#d3d3d3", command = self.name_collection)
        self.continue_button.grid(row=4)

        #image
        self.heading_image = Image.open("mrgs_logo.png")
        self.heading_image = self.heading_image.resize((100,100), Image.ANTIALIAS)
        self.heading_image = ImageTk.PhotoImage(self.heading_image)

       #image Label
        self.image_label = Label(self.quiz_frame, image = self.heading_image, bg = background_color)
       #self.heading_image.grid(row=0, column=1)
        self.image_label.grid(row = 1)

    #command for continue button
    def name_collection(self):
      name = self.entry_box.get()
      if name.strip() !="" and len(name) <= 16:#if the name is less than 16 characters then the user will proceed
          names_list.append(name)
          print(names_list)
          self.quiz_frame.destroy()
          QuizPicker(root)
      #check to see if name is more than 16 characters
      elif len(name) > 16:
          self.user_label.config(text = "Name must be less than 16 characters",fg="red")
      #check to see if the user left the name entry box empty    
      elif len(name) ==0:
          self.user_label.config(text="You cannot leave entry box empty", fg="red")
        
    
    #command for exit button
    def quiz_exit(self):
      exit()



#Page where the user will pick which math topic they want to do
class QuizPicker:
    def __init__(self, master):
        background_color = "#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        #Label that wil ask the user what math topic they want to learn about
        self.heading_label = Label(self.quiz_frame, text = "Hello " + names_list[0] + ", what topic do you want to learn about?",font = ("Tw Cent Mt", "14", "bold"))
        self.heading_label.grid(row = 1)

        #algebra button
        self.algebra_button = Button(self.quiz_frame, text="Algebra(Level 1)", command = self.quiz_algebra)
        self.algebra_button.grid(row = 2)

        #trigonometry button
        self.trigonometry_button = Button(self.quiz_frame, text = "Trigonometry", command = self.quiz_trig)
        self.trigonometry_button.grid(row = 3)

        #calculus button
        self.calculus_button = Button(self.quiz_frame, text = "Calculus", command = self.Quiz_calculus)
        self.calculus_button.grid(row = 4)

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



#Algebra quiz
class QuizAlgebra:
    def __init__(self, master):
        background_color ="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #randomiser will randomly pick a question number
        algebra_randomiser()

        #Question label widget 
        self.question_label = Label(self.quiz_frame, text = algebra_questions_answers[algebra_qnum][0],bg = background_color, font = ("Tw Cent Mt", "11", "bold", "italic"))
        self.question_label.grid(row = 0)

        #holds the value of radio buttons
        self.var1 = IntVar()

        #radio button 1
        self.ac1 = Radiobutton(self.quiz_frame, text=algebra_questions_answers[algebra_qnum][1], font = ("Tw Cent Mt", "11", "bold"),value = 1, pady = 10,variable = self.var1, indicator = 0)
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
        #if user picked the right answer
        if choice == algebra_questions_answers[algebra_qnum][6]:
          score+=1
          score_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.AlgebraEnd_Screen()

        #if user picked the wrong answer
        else:
          score+=0
          score_label.configure(text="The correct answer was: " + algebra_questions_answers[algebra_qnum][5])
          self.confirm_button.config(text = "Confirm")
          self.AlgebraEnd_Screen()
          
      else:
        if choice == 0:#if user didn't pick an option
          score_label.configure(text = "You have not selected an option.",fg="red")
          choice = self.var1.get()
        else:#if choice is made
          if choice == algebra_questions_answers[algebra_qnum][6]: 
                    score+=1
                    score_label.configure(text=score) 
                    self.confirm_button.config(text="Confirm")
                    self.algebra_questions_setup()

          #if user picked the worng answer
          else:
            score+=0
            score_label.configure(text = "The correct answer was: " + algebra_questions_answers[algebra_qnum][5])
            self.confirm_button.configure(text="Confirm")
            self.algebra_questions_setup()

    #Algebra end screen function
    def AlgebraEnd_Screen(self):
      root.withdraw()#hides the root window 
      open_endscreen = AlgebraEnd()


#End screen class for algebra quiz
class AlgebraEnd:
  def __init__(self):
    background_color = "#b7d7bf"#background colour is reclining green
    self.end_box = Toplevel(root)#Create a window on top of the root window
    self.end_box.title("End Box")

    #frame set up for end box
    self.end_frame = Frame(self.end_box, padx=100, pady=100, bg=background_color)
    self.end_frame.grid(row=0)

    #Label that will congratualte the user
    self.end_heading = Label(self.end_frame, text="Well Done", pady=15, bg=background_color)
    self.end_heading.grid(row=0)

    #exit button
    self.exit_button = Button(self.end_frame, text="Exit", width=10, command = self.close_algebra, bg="red")
    self.exit_button.grid(row=4, pady=40)

  def close_algebra(self):#function for the exi tbtton in the end screen
    self.end_box.destroy()#destroys end box
    root.withdraw()#hides the root window

          


#Trigonometry Quiz
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
          self.TrigEnd_Screen()
        else:
          score+=0
          score_label.configure(text="The correct answer was: " + trigonometry_questions_answers[trig_qnum][5])
          self.confirm_button.config(text = "Confirm")
          self.TrigEnd_Screen()
          
      else:
        if choice == 0:
          score_label.configure(text = "You have not selected an option.",fg="red")
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

    def TrigEnd_Screen(self):
      root.withdraw()#hides the root window
      open_endscreen = TrigEnd()

#End screen class for trig quiz
class TrigEnd:
    def __init__(self):
      background_color = "#b7d7bf"
      self.end_box = Toplevel(root)#creates another window on top of the root window
      self.end_box.title("End Box")

      #heading label that will congratulat the user
      self.end_frame = Frame(self.end_box, padx=100, pady=100, bg=background_color)
      self.end_frame.grid(row=0)

      #heading label that will congratulate the user
      self.end_heading = Label(self.end_frame, text="Well Done", pady=15, bg=background_color)
      self.end_heading.grid(row=0)

      #exit button
      self.exit_button = Button(self.end_frame, text="Exit", width=10, command = self.close_trig, bg="red")
      self.exit_button.grid(row=4, pady=40)

    #function for exit button in TrigEnd
    def close_trig(self):
      self.end_box.destroy()#destroys the end box
      root.withdraw()#hides the root window without destroying it





#Calculus quiz class
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
          #if user gets the question right
          if choice == calculus_questions_answers[calculus_qnum][6]:
            score+=1
            score_label.configure(text=score)
            self.confirm_button.config(text="Confirm")
            self.CalculusEnd_Screen()
          else:
            #if user gets the question wrong
            score+=0
            score_label.configure(text="The correct answer was: " + calculus_questions_answers[calculus_qnum][5])
            self.confirm_button.config(text = "Confirm")
            self.CalculusEnd_Screen()
            
        else:
          if choice == 0:
            score_label.configure(text = "You have not selected an option.",fg="red")
            choice = self.var1.get()
          else:#if choice is made
            if choice == calculus_questions_answers[calculus_qnum][6]: #if user gets the question right
                      score+=1
                      score_label.configure(text=score) 
                      self.confirm_button.config(text="Confirm")
                      self.calculus_questions_setup()
            else:
              score+=0
              #if user gets the qestion wrong
              score_label.configure(text = "The correct answer was: " + calculus_questions_answers[calculus_qnum][5])
              self.confirm_button.configure(text="Confirm")
              self.calculus_questions_setup()

  def CalculusEnd_Screen(self):
    root.withdraw()#hides the root window 
    open_endscreen = CalculusEnd()#



#End screen class for calculus quiz
class CalculusEnd:
    def __init__(self):
      background_color = "#b7d7bf"
      self.end_box = Toplevel(root)
      self.end_box.title("End Box")

      #frmae setup for end box
      self.end_frame = Frame(self.end_box, padx=100, pady=100, bg=background_color)
      self.end_frame.grid(row=0)

      #heading label that will congratulate the user 
      self.end_heading = Label(self.end_frame, text="Well Done", pady=15, bg=background_color)
      self.end_heading.grid(row=0)

      #exit button
      self.exit_button = Button(self.end_frame, text="Exit", width=10, command = self.close_calculus, bg="red")
      self.exit_button.grid(row=4, pady=40)

    #function for exit button in CalculusEnd class
    def close_calculus(self):
      self.end_box.destroy()#destroys the end box
      root.withdraw()#hides the root window     



#***********starting point************#
if __name__ == "__main__":
  root = Tk()
  root.title("MRGS Maths Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#window doesn't dissapear