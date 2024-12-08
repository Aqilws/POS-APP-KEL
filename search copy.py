from product import Products
import tkinter as tk
from tkinter import ttk

class Search(Products):
    def __init__(self):
        super().__init__()
    
    def window(self):
        window = tk.Tk()
        window.title(self.get_aplication_name())
        window.geometry(self.get_screen_size())
        window.grid_columnconfigure(0, weight=7)
        window.grid_columnconfigure(1, weight=3)
        window.grid_rowconfigure(0, weight=1)

        # -------------------- Frame Search --------------------
        frame_search = tk.Frame(window, bg="blue")
        frame_search.grid(row=0, column=0, sticky="nsew")
        frame_search.grid_rowconfigure(1, weight=8)
        frame_search.grid_columnconfigure(0, weight=1)

        # header
        header_search = tk.Frame(frame_search, bg="red", height=50)
        header_search.grid(column=0, row=0, sticky="nsew")

        

        # Body
        body_search = tk.Frame(frame_search, bg="grey")
        body_search.grid(column=0, row=1, sticky="nsew")

        # Footer
        footer_search = tk.Frame(frame_search, bg="green", height=50)
        footer_search.grid(column=0, row=2, sticky="nsew")


        # -------------------- Frame Chart --------------------
        frame_chart = tk.Frame(window, bg="yellow")
        frame_chart.grid(row=0, column=1, sticky="nsew")
        frame_chart.grid_rowconfigure(1, weight=8)
        frame_chart.grid_columnconfigure(0, weight=1)

        # header
        header_chart = tk.Frame(frame_chart, bg="white", height=50)
        header_chart.grid(column=0, row=0, sticky="nsew")

        # Body
        body_chart = tk.Frame(frame_chart, bg="orange")
        body_chart.grid(column=0, row=1, sticky="nsew")

        # Footer
        footer_chart = tk.Frame(frame_chart, bg="olive", height=50)
        footer_chart.grid(column=0, row=2, sticky="nsew")





        window.mainloop()

apk = Search()
apk.window()