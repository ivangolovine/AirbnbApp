import tkinter as tk
from messageGUI import get_gui_data
from API.googleTest import *

class DisplayInterface:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1100x600")
        self.root.title("Parsing")
        self.message_count = 0
        self.keyword_count = 0
        
        # Create a Frame to hold all the widgets
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Expand to fill the entire window

        self.create_all_sections()
        
        self.root.mainloop()


    # Combined View Of Frames
    def create_all_sections(self):
        self.global_container = tk.Frame(self.main_frame, height=1000, width=800, bg='purple')
        self.global_container.pack()
        
        self.create_input_section()
        self.create_display_section()
        

    # Input section
    def create_input_section(self):
        self.input_frame_global = tk.Frame(self.global_container, height=300, width=800, bg='red')
        self.input_frame_global.pack(side=tk.LEFT)
        
        self.input_frame_inner = tk.Frame(self.input_frame_global, height=300, width=800, bg='orange')
        self.input_frame_inner.pack()

        self.create_message_input()
        self.create_keyword_input()
        self.input_buttons()

    def create_message_input(self):
        self.top_frame_message = tk.Frame(self.input_frame_inner, height=50, width=50, bg="blue")
        self.top_frame_message.pack(side=tk.LEFT)

        self.label_message = tk.Label(self.top_frame_message, text="The message", font=('Arial', 18))
        self.label_message.pack(padx=10, pady=10, anchor=tk.W)

        self.textbox_message = tk.Text(self.top_frame_message, height=10, width=20, font=('Arial', 16))
        self.textbox_message.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_keyword_input(self):
        self.top_frame_keyword = tk.Frame(self.input_frame_inner, height=200, bg="grey")
        self.top_frame_keyword.pack(side=tk.LEFT)

        self.label_keyword = tk.Label(self.top_frame_keyword, text="Keywords", font=('Arial', 18))
        self.label_keyword.pack(padx=10, pady=10, anchor=tk.W)

        self.textbox_keyword = tk.Text(self.top_frame_keyword, height=10, width=20, font=('Arial', 16))  # Adjust width here
        self.textbox_keyword.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def input_buttons(self):
        self.top_frame_input_buttons = tk.Frame(self.input_frame_global, height=300, width=50, bg="yellow")
        self.top_frame_input_buttons.pack()

        self.button_add_message = tk.Button(self.top_frame_input_buttons, text="Add Message", command=self.add_message)
        self.button_add_message.pack(padx=10, pady=10, side=tk.LEFT)

        self.button_add_keyword = tk.Button(self.top_frame_input_buttons, text="Add Keyword", command=self.add_keyword)
        self.button_add_keyword.pack(padx=10, pady=10, side=tk.LEFT)
        
        self.button_add_both = tk.Button(self.top_frame_input_buttons, text="Add Both", command=self.add_both)
        self.button_add_both.pack(padx=10, pady=10, side=tk.LEFT)

    
    # Display Section
    def create_display_section(self):
        self.display_frame_global = tk.Frame(self.global_container, height=300, width=800, bg='red')
        self.display_frame_global.pack(side=tk.LEFT, anchor=tk.N)
        
        self.display_frame_inner = tk.Frame(self.display_frame_global, height=300, width=800, bg='orange')
        self.display_frame_inner.pack(anchor=tk.N)

        self.create_message_display()
        self.create_keyword_display()
        self.display_buttons()
    
    def create_message_display(self):
        self.frame_message_display = tk.Frame(self.display_frame_inner, height=50, width=50, bg="blue")
        self.frame_message_display.pack(side=tk.LEFT)

        self.label_message_d = tk.Label(self.frame_message_display, text="The message", font=('Arial', 18))
        self.label_message_d.pack(padx=10, pady=10, anchor=tk.W)

        self.textbox_message_d = tk.Text(self.frame_message_display, height=10, width=20, font=('Arial', 16))
        self.textbox_message_d.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    
    def create_keyword_display(self):
        self.display_frame_keyword = tk.Frame(self.display_frame_inner, height=200, bg="grey")
        self.display_frame_keyword.pack(side=tk.LEFT)

        self.label_keyword_d = tk.Label(self.display_frame_keyword, text="Keywords", font=('Arial', 18))
        self.label_keyword_d.pack(padx=10, pady=10, anchor=tk.W)

        self.textbox_keyword_d = tk.Text(self.display_frame_keyword, height=10, width=20, font=('Arial', 16)) 
        self.textbox_keyword_d.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    def display_buttons(self):
        self.display_frame_buttons = tk.Frame(self.display_frame_global, height=300, width=50, bg="yellow")
        self.display_frame_buttons.pack()

        self.button_submit_message = tk.Button(self.display_frame_buttons, text="Submit", command=self.submit_keywords_message)
        self.button_submit_message.pack(padx=10, pady=10, side=tk.LEFT)

        self.button_connect = tk.Button(self.display_frame_buttons, text="Connect", command=login_Airbnb)
        self.button_connect.pack(padx=10, pady=10, side=tk.LEFT)

    def set_max_width(self, widget, max_width):
        widget.bind("<Configure>", lambda e: widget.config(width=min(widget.winfo_width(), max_width)))

    # Functionality
    
    def add_message(self):
        message = self.textbox_message.get("1.0", tk.END).strip()
        if message:
            self.message_count += 1
            self.textbox_message_d.insert(tk.END, f"{self.message_count}: {message}\n")
            self.textbox_message.delete("1.0", tk.END)
        
    def add_keyword(self):
        keyword = self.textbox_keyword.get("1.0", tk.END).strip()
        if keyword:
            self.keyword_count += 1
            self.textbox_keyword_d .insert(tk.END, f"{self.keyword_count}: {keyword}\n")
            self.textbox_keyword.delete("1.0", tk.END)  # Clear the keyword textbox
    
    def add_both(self):
        self.add_message()
        self.add_keyword()
        
    def submit_keywords_message(self):
        message = self.textbox_message_d.get("1.0", tk.END).strip()
        keywords = self.textbox_keyword_d.get("1.0", tk.END).strip()
        self.textbox_message_d.delete("1.0", tk.END)
        self.textbox_keyword_d.delete("1.0", tk.END)
        get_gui_data(message, keywords)


    
'''
    def create_global_display_area(self):
        self.frame_global_display = tk.Frame(self.global_container, height=20, width=20, bg="grey")
        self.frame_global_display.pack(side=tk.LEFT, anchor=tk.N)
                
        self.create_display_area()
    
    def create_display_area(self):
        self.frame_results_display = tk.Frame(self.frame_global_display, bg="grey")
        self.frame_results_display.pack(side=tk.LEFT, anchor=tk.N)

        self.top_frame_results_message = tk.Frame(self.frame_results_display, height=13, bg="orange")
        self.top_frame_results_message.pack(side=tk.LEFT)
        self.set_max_width(self.top_frame_results_message, 20)

        self.top_frame_results_keywords = tk.Frame(self.frame_results_display, height=13, bg="grey")
        self.top_frame_results_keywords.pack(side=tk.LEFT)
        self.set_max_width(self.top_frame_results_keywords, 20)

        self.display_label_msg = tk.Label(self.top_frame_results_message, text="Message", font=('Arial', 18))
        self.display_label_msg.pack(padx=10, pady=10, anchor=tk.CENTER)

        self.display_text_msg = tk.Text(self.top_frame_results_message, height=10, font=('Arial', 16))
        self.display_text_msg.pack(padx=10, pady=10, expand=True)
        self.set_max_width(self.display_text_msg, 20)

        self.display_label_keyw = tk.Label(self.top_frame_results_keywords, text="Keywords", font=('Arial', 18))
        self.display_label_keyw.pack(padx=10, pady=10, anchor=tk.CENTER)

        self.display_text_keyw = tk.Text(self.top_frame_results_keywords, height=10, font=('Arial', 16))
        self.display_text_keyw.pack(padx=10, pady=10, expand=True)
        self.set_max_width(self.display_text_keyw, 20)
        
        self.display_submit_button()

    def display_submit_button(self):
        self.submit_button = tk.Button(self.frame_results_display, text="Submit", command=self.submit_keywords_message)
        self.submit_button.pack(side=tk.BOTTOM)
    '''

#DisplayInterface()





