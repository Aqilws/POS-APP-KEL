import tkinter as tk

# Class induk / Parent
class Induk:
    def __init__(self):
        self.__aplication_name = "Aplikasi kasir"
        self.__screen_size = "1000x500"
    
    # Get Aplication name
    def get_aplication_name(self):
        return self.__aplication_name

    # Get screen size
    def get_screen_size(self):
        return self.__screen_size
    
    def window(self):
        # Membuat jendela utama
        root = tk.Tk()
        root.title("Contoh Tkinter Sederhana")
        root.geometry("300x200")

        # Menambahkan label ke dalam jendela
        label = tk.Label(root, text="Halo, Dunia!", font=("Arial", 14))
        label.pack(pady=50)

        # Menjalankan aplikasi
        root.mainloop()

# induk = Induk()
# induk.window()