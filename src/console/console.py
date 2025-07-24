import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading

class ConsoleWindow:
    def __init__(self, title="Console"):
        self.messages = []
        self.root = None
        self.text_widget = None
        self._start_gui_thread(title)

    def _start_gui_thread(self, title):
        thread = threading.Thread(target=self._init_window, args=(title,), daemon=True)
        thread.start()

    def _init_window(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e1e")  # fundo da janela

        self.text_widget = ScrolledText(
            self.root, 
            state='disabled',
            wrap='word',
            bg="#1e1e1e",  # fundo do texto
            fg="white",    # cor padrão
            insertbackground="white",  # cursor visível
            font=("Consolas", 11)
        )
        self.text_widget.pack(expand=True, fill='both')

        self._define_tags()

        self._update_loop()
        self.root.mainloop()

    def _define_tags(self):
        # Define estilos de cor para mensagens
        colors = {
            "white": "#ffffff",
            "red": "#ff4c4c",
            "green": "#4cff4c",
            "yellow": "#ffff66",
            "cyan": "#66ffff",
            "magenta": "#ff66ff"
        }

        for name, color in colors.items():
            self.text_widget.tag_config(name, foreground=color)

    def _update_loop(self):
        if self.messages:
            self.text_widget.configure(state='normal')
            for msg, color in self.messages:
                self.text_widget.insert('end', msg + "\n", color)
                self.text_widget.see('end')
            self.messages.clear()
            self.text_widget.configure(state='disabled')

        if self.root:
            self.root.after(100, self._update_loop)

    def sendMessage(self, message, color="white"):
        self.messages.append((str(message), color))

console = ConsoleWindow("Log")