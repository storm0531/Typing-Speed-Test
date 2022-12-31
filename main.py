import random
import time
from tkinter import *

BG_COLOR ="#2DCDDF"
start_time = 0
end_time = 0
error_count = 0
word_per_second = 0
possible_sentences = [
    "All you need to do is pick up \nthe pen and begin.\n\n",
    "He decided that the time had come\n to be stronger than any of the \nexcuses he'd used until then.\n\n",
    "A dead duck doesn't fly backward.\n\n\n",
    "There can never be too many \ncherries on an ice cream sundae.\n\n",
    "He used to get confused between \nsoldiers and shoulders,\n but as a military man, \nhe now soldiers responsibility.",
]
test_text = ""

def set_test_label(test_text):
    part_sentences =test_text.split("\n")
    test_label_1.config(text=part_sentences[0])
    test_label_2.config(text=part_sentences[1])
    test_label_3.config(text=part_sentences[2])
    test_label_4.config(text=part_sentences[3])
def reset():
    global end_time,start_time ,error_count,word_per_second,test_text
    end_time = 0
    start_time = 0
    error_count =0
    word_per_second =0
    user_text.delete(0,END)
    test_text = random.choice(possible_sentences)
    set_test_label(test_text)
    end_results.config(text=" ")

def end_test():
    global start_time, end_time,error_count,word_per_second
    end_time = time.time()
    error_count = check_error()
    elapsed_time = end_time - start_time
    word_per_minute = len(user_text.get()) / (elapsed_time/60)
    end_results.config(text=f"error count:{error_count},\nelapsed time is:{elapsed_time:.3},\nWPM is :{word_per_minute:.4}")
    title_label.config(text="results/reset")

def start_test():
    reset()
    global start_time
    title_label.config(text="typing")
    start_btn.config(bg="pink")
    end_btn.config(bg="green")
    start_time = time.time()

def check_error():
    errors = 0
    input_text = user_text.get().split(" ")
    for word in test_text.split(" "):
        if word not in input_text:
            errors += 1
    return errors

window = Tk()
window.title("Type Speed Test")
window.geometry("750x600")
window.config(highlightthickness=0,padx=100,pady=30,bg=BG_COLOR)

title_label = Label(text="START WHEN READY",font=("arial",30,"bold"),fg="#6C00FF",bg=BG_COLOR)
title_label.grid(column=0,row=0,columnspan=2,pady=30)

test_label_1 = Label(font=("arial",20,"bold"),fg="black",bg=BG_COLOR)
test_label_1.grid(column=0,row=1,columnspan=2)
test_label_2 = Label(font=("arial",20,"bold"),fg="black",bg=BG_COLOR)
test_label_2.grid(column=0,row=2,columnspan=2)
test_label_3 = Label(font=("arial",20,"bold"),fg="black",bg=BG_COLOR)
test_label_3.grid(column=0,row=3,columnspan=2)
test_label_4 = Label(font=("arial",20,"bold"),fg="black",bg=BG_COLOR)
test_label_4.grid(column=0,row=4,columnspan=2)

user_text = Entry(width=25,font=("Arial",30),fg="#3C79F5")
user_text.focus()
user_text.grid(column=0,row=5,columnspan=2,pady=40)

start_btn = Button(width=36,text="Start" ,bg="green",command=start_test)
start_btn.grid(column=0,row=6)

end_btn = Button(width=36,text="ENd",bg="red",command=end_test)
end_btn.grid(column=1,row=6,columnspan=2)

end_results = Label(text=" ",font=("arial",20,"bold"),bg=BG_COLOR,fg="#6C00FF")
end_results.grid(column=0,row=7,columnspan=3)


window.mainloop()