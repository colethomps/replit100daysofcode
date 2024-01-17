import tkinter as tk

window = tk.Tk()
window.title("Hello World") # Sets the name of the window in the border
window.geometry("300x300") # Sets the size of the window in pixels

hello = tk.Label(text = "Hello World") # Creates a text box
hello.pack() # 'pack' places the element on the screen

button = tk.Button(text = "Click me!") # Creates a button
button.pack()

tk.mainloop()