import tkinter as tk
from tkinter import ttk
import requests




class PotterAPIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harry Potter API GUI")


        # Create a Notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)


        # Create frames for different API functions
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)


        # Add frames to the notebook with corresponding tabs
        self.notebook.add(self.frame1, text='Character Info')
        self.notebook.add(self.frame2, text='Movies Info')


        # Initialize GUI elements
        self.init_character_frame()
        self.init_movies_frame()


    def init_character_frame(self):
        # Character frame widgets
        self.char_label = ttk.Label(self.frame1, text="Enter Character ID:")
        self.char_entry = ttk.Entry(self.frame1)
        self.char_button = ttk.Button(self.frame1, text="Get Character Info", command=self.get_character_info)
        self.char_result_label = ttk.Label(self.frame1, text="Character Info will be displayed here.")


        # Character frame grid layout
        self.char_label.grid(row=0, column=0, padx=10, pady=10)
        self.char_entry.grid(row=0, column=1, padx=10, pady=10)
        self.char_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.char_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


    def init_movies_frame(self):
        # Movies frame widgets
        self.movies_label = ttk.Label(self.frame2, text="Enter Movie ID:")
        self.movies_entry = ttk.Entry(self.frame2)
        self.movies_button = ttk.Button(self.frame2, text="Get Movie Info", command=self.get_movies_info)
        self.movies_result_label = ttk.Label(self.frame2, text="Movie Info will be displayed here.")


        # Movies frame grid layout
        self.movies_label.grid(row=0, column=0, padx=10, pady=10)
        self.movies_entry.grid(row=0, column=1, padx=10, pady=10)
        self.movies_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.movies_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


    def get_character_info(self):
        character_id = self.char_entry.get()


        # Validate input
        if not character_id.isdigit():
            self.char_result_label.config(text="Invalid ID. Please enter a numeric ID.")
            return


        url = f"https://api.potterdb.com/v1/characters/{character_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes


            character_info = response.json()
            # Display character info
            self.char_result_label.config(text=f"Character Info: {character_info}")


        except requests.exceptions.HTTPError as err:
            self.char_result_label.config(text=f"Error: {err}")


    def get_movies_info(self):
        movie_id = self.movies_entry.get()


        # Replace with the actual API endpoint
        url = f"https://api.example.com/movies/{movie_id}"  
        try:
            response = requests.get(url)
            response.raise_for_status()


            movie_info = response.json()
            # Display movie info
            self.movies_result_label.config(text=f"Movie Info: {movie_info}")


        except requests.exceptions.HTTPError as err:
            self.movies_result_label.config(text=f"Error: {err}")




if __name__ == "__main__":
    root = tk.Tk()
    app = PotterAPIApp(root)
    root.mainloop()