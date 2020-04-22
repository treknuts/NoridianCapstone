from tkinter import *
from dashboard import Dashboard
from fileupload import FileUpload
from detailsgeneral import DataVisualization


class Navbar(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame = None
        container = Frame(self.parent)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky=NSEW)

        menu = Menu(container)

        navigation = Menu(menu)
        navigation.add_command(label="File Upload", command=lambda: self.show_frame(FileUpload, container))
        navigation.add_command(label="Dashboard", command=lambda: self.show_frame(Dashboard, container))
        navigation.add_command(label="Details", command=lambda: self.show_frame(DataVisualization, container))
        navigation.add_command(label="Exit", command=self.parent.quit)
        menu.add_cascade(label="Navigation", menu=navigation)
        self.parent.config(menu=menu)

        self.frames = {}
        file_upload = FileUpload(container)
        dashboard = Dashboard(container)
        details = DataVisualization(container)
        self.frames["fileupload"] = file_upload
        self.frames["dashboard"] = dashboard
        self.frames["details"] = details

        # file_upload.grid(row=0, column=0, sticky=NSEW)
        # dashboard.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(FileUpload, container)

    def show_frame(self, frame_class, cont):
        new_frame = frame_class(cont)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.grid(row=0, column=0, sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    navbar = Navbar(root)
    mainloop()