import customtkinter as ctk

class PrefillInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, title, prompt, initialvalue=""):
        super().__init__(parent)
        self.title(title)
        self.geometry("350x120")
        self.resizable(False, False)
        self.result = None
        self.wait_visibility()
        self.grab_set()

        label = ctk.CTkLabel(self, text=prompt)
        label.pack(pady=(10, 5))

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=(0, 10), padx=20, fill="x")
        self.entry.insert(0, initialvalue)
        self.entry.focus()

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=5)

        btn_ok = ctk.CTkButton(btn_frame, text="OK", width=70, command=self.on_ok)
        btn_ok.pack(side="left", padx=10)
        btn_cancel = ctk.CTkButton(btn_frame, text="Cancel", width=70, command=self.on_cancel)
        btn_cancel.pack(side="left")

        self.bind("<Return>", lambda e: self.on_ok())
        self.bind("<Escape>", lambda e: self.on_cancel())

    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()

def ask_prefill_input(parent, title, prompt, initialvalue=""):
    dialog = PrefillInputDialog(parent, title, prompt, initialvalue)
    parent.wait_window(dialog)
    return dialog.result
