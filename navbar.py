from tkinter import *
from dashboard import Dashboard
from fileupload import FileUpload


class Navbar(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()
        self.file_upload = FileUpload(self.master)

    def init_window(self):
        menu = Menu(self.master)

        navigation = Menu(menu)
        navigation.add_command(label="Dashboard", command=self.open_dashboard)
        navigation.add_command(label="File Upload", command=self.open_fileupload)
        navigation.add_command(label="Exit", command=self.master.quit)
        menu.add_cascade(label="Navigation", menu=navigation)

        self.master.config(menu=menu)

    def open_dashboard(self):
        self.dashboard = Dashboard(self.master)
        self.file_upload.quit()
        return self.dashboard

    def open_fileupload(self):
        self.file_upload = FileUpload(self.master)
        self.dashboard.quit()
        return self.file_upload


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    navbar = Navbar(root)
    mainloop()