# First we will import tkinter to use GUI
import tkinter as tk

# Now we will import the required library for our app
import pyshorteners

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    output_label.config(text= "Here is your shortened URL: " + short_url,fg='red')

# My main window
window = tk.Tk()
window.title("Anshika's URL Shortener")
window.geometry("900x200")
window.configure(bg="black")
heading_label = tk.Label(window, text="Welcome to URL Shortener", font=("Helvetica", 24, "bold"),fg="blue")
heading_label.pack(pady=30)


# Taking input from the user
label = tk.Label(window, text="Enter the URL that needs to be shorten:",bg='yellow')
label.pack()
entry = tk.Entry(window, width=150)
entry.pack()

# Creating the button to shorten the URL
button = tk.Button(window, text="Shorten",bg='yellow', command=shorten_url)
button.pack(side='right')

# THE FINAL OUTPUT
output_label = tk.Label(window, text="")
output_label.pack(pady=15)

# Start the main event loop
window.mainloop()
