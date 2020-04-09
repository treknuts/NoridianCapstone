from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class FileUpload(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.init_window()

    def init_window(self):
        nw_frame = Frame(self.master, width=600, height=200, background="white")
        nw_frame.grid(column=0, row=0)

        n_frame = Frame(self.master, width=600, height=200, background="white")
        n_frame.grid(column=1, row=0)

        w_frame = Frame(self.master, width=600, height=200, background="white")
        w_frame.grid(column=0, row=1)

        self.label_frame = LabelFrame(self.master, text="Open a File", width=600, height=200, relief=SUNKEN)
        self.label_frame.grid(column=1, row=1, ipadx=50)

        self.upload_field = Entry(self.label_frame, width=50)
        self.upload_field.grid(column=0, row=0, padx=10, pady=50)

        self.browse_btn = Button(self.label_frame, text="Browse", command=self.filedialog)
        self.browse_btn.grid(column=1, row=0, padx=10, pady=50)

        self.upload_button = Button(self.master, text="Upload", command=self.upload_file)
        self.upload_button.grid(column=1, row=2)

    def filedialog(self):
        self.file_name = filedialog.askopenfilename(initialdir="/",
                                                    title="Select a file",
                                                    filetype=(("Excel files", "*.xlsx"), ("All files", "*.*")))
        self.upload_field.insert(0, "{}".format(self.file_name))
        return self.file_name

    # TODO: Upload file to handle data
    def upload_file(self):
        messagebox.showinfo(title="File Upload Status", message="You have uploaded {}".format(self.file_name))


if __name__ == '__main__':
    root = Tk()
    root.title("Noridian Capstone App")
    root.geometry("1900x1000")
    root.configure(background='white')
    upload = FileUpload(root)
    mainloop()
