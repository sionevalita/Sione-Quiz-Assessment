from tkinter import*
from PIL import ImageTk, Image

names_list=[]

class Quizstarter:
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
       Quizpicker(root)
    
    #command for exit button
    def quiz_exit(self):
      exit()



#page where user will pick which topic they want to learn
class Quizpicker:
    def __init__(self, master):
        background_color="#b7d7bf"
        #frame setup
        self.quiz_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label=Label(self.quiz_frame, text="Hello " + names_list[0] + ", what topic do you want to learn about?",font=("Tw Cent Mt", "14", "bold"))
        self.heading_label.grid(row=1)

        self.algebra_button = Button(self.quiz_frame, text="Algebra(Level 1)")
        self.algebra_button.grid(row= 2)

        self.trigonometry_button = Button(self.quiz_frame, text="Trigonometry")
        self.trigonometry_button.grid(row=3)

        self.calculus_button = Button(self.quiz_frame, text="Calculus")
        self.calculus_button.grid(row=4)

















#***********starting point************#
if __name__ == "__main__":
  root = Tk()
  root.title("MRGS Maths Quiz")
  quizStarter_object = Quizstarter(root)
  root.mainloop()#window doesn't dissapear