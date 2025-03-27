import pyautogui
import random
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import webbrowser
import sys

class AntiIdlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam Anti Idler")
        self.root.geometry("420x250")
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        self.language = "EN"
        
        try:
            self.center_window()
            self.is_running = False
            
            self.style = ttk.Style()
            self.style.theme_use('clam')
            
            self.title_font = Font(family="Segoe UI", size=16, weight="bold")
            self.button_font = Font(family="Segoe UI", size=11)
            self.small_font = Font(family="Segoe UI", size=9)
            
            self.main_frame = tk.Frame(root, bg='black', bd=0)
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            self.create_widgets()
            
            pyautogui.FAILSAFE = True
            self.root.protocol("WM_DELETE_WINDOW", self.on_close)
            
        except Exception as e:
            messagebox.showerror("Error", f"Initialization error:\n{str(e)}")
            self.root.destroy()
            sys.exit(1)
    
    def create_widgets(self):
        self.header = tk.Frame(self.main_frame, bg='black')
        self.header.pack(fill=tk.X, pady=(0, 10))
        
        self.title_frame = tk.Frame(self.header, bg='black')
        self.title_frame.pack(fill=tk.X)
        
        self.title_label = tk.Label(
            self.title_frame, 
            text="Steam Anti Idler", 
            font=self.title_font, 
            bg='black', 
            fg='white'
        )
        self.title_label.pack(side=tk.LEFT)
        
        self.lang_button = tk.Button(
            self.title_frame,
            text="🌐",
            font=("Arial", 14),
            fg="white",
            bg="black",
            bd=0,
            activebackground="#333333",
            command=self.toggle_language
        )
        self.lang_button.pack(side=tk.RIGHT, padx=5)
        
        self.body = tk.Frame(self.main_frame, bg='black')
        self.body.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.info_label = tk.Label(
            self.body, 
            text="This program moves your mouse cursor every 4 seconds\nto prevent system idle status.", 
            font=("Segoe UI", 10), 
            bg='black', 
            fg='white',
            justify=tk.CENTER
        )
        self.info_label.pack(pady=(0, 15))
        
        self.status_frame = tk.Frame(self.body, bg='#333333', bd=1, relief=tk.SUNKEN)
        self.status_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.status_label = tk.Label(
            self.status_frame, 
            text="Status: Ready", 
            font=("Segoe UI", 9), 
            bg='#333333', 
            fg='white'
        )
        self.status_label.pack(padx=5, pady=3, anchor=tk.W)
        
        self.buttons_frame = tk.Frame(self.main_frame, bg='black')
        self.buttons_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.start_button = ttk.Button(
            self.buttons_frame, 
            text="Start", 
            command=self.start_moving,
            style='Start.TButton',
            width=10
        )
        self.start_button.pack(side=tk.LEFT, padx=(20, 5), ipady=5)
        
        self.stop_button = ttk.Button(
            self.buttons_frame, 
            text="Stop", 
            command=self.stop_moving, 
            state=tk.DISABLED,
            style='Stop.TButton',
            width=10
        )
        self.stop_button.pack(side=tk.LEFT, padx=5, ipady=5)
        
        self.about_button = tk.Button(
            self.buttons_frame,
            text="ABOUT ME",
            font=self.small_font,
            fg="white",
            bg="#333333",
            bd=1,
            relief=tk.RAISED,
            activebackground="#555555",
            command=self.show_about,
            padx=5,
            pady=2
        )
        self.about_button.pack(side=tk.RIGHT, padx=20, ipadx=5, ipady=2)
        
        self.style.configure('Start.TButton', 
                          font=self.button_font, 
                          foreground='black',
                          background='#4CAF50',
                          padding=5)
        
        self.style.configure('Stop.TButton', 
                          font=self.button_font, 
                          foreground='black',
                          background='#F44336',
                          padding=5)
    
    def toggle_language(self):
        """تغییر زبان بین انگلیسی و فارسی"""
        if self.language == "EN":
            self.language = "FA"
            self.title_label.config(text="حرکت اتومات موس-مخصوص استیم فارم")
            self.info_label.config(text="این برنامه هر 4 ثانیه نشانگر موس را حرکت می‌دهد\nتا سیستم شما در حالت غیرفعال قرار نگیرد")
            self.start_button.config(text="شروع")
            self.stop_button.config(text="توقف")
            self.status_label.config(text="وضعیت: آماده")
        else:
            self.language = "EN"
            self.title_label.config(text="Steam Anti Idler - Farm ")
            self.info_label.config(text="This program moves your mouse cursor every 4 seconds\nto prevent system idle status.")
            self.start_button.config(text="Start")
            self.stop_button.config(text="Stop")
            self.status_label.config(text="Status: Ready")
    
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("300x150")
        about_window.resizable(False, False)
        about_window.configure(bg='black')
        
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 150
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 75
        about_window.geometry(f"300x150+{x}+{y}")
        
        tk.Label(
            about_window,
            text="CODED BY: @ERFAN.SH",
            font=("Segoe UI", 10),
            bg='black',
            fg='white'
        ).pack(pady=(20, 5))
        
        tk.Label(
            about_window,
            text="❤️ برنامه ساخته شده با",
            font=("Segoe UI", 10),
            bg='black',
            fg='white'
        ).pack(pady=5)
        
        telegram_link = tk.Label(
            about_window,
            text="https://t.me/S04IAL",
            font=("Segoe UI", 10, "underline"),
            bg='black',
            fg='blue',
            cursor="hand2"
        )
        telegram_link.pack(pady=5)
        telegram_link.bind("<Button-2>", lambda e: webbrowser.open("https://t.me/S04IAL"))
    
    def move_mouse_randomly(self):
        if self.is_running:
            screen_width, screen_height = pyautogui.size()
            
            new_x = random.randint(int(screen_width*0.05), int(screen_width*0.95))
            new_y = random.randint(int(screen_height*0.05), int(screen_height*0.95))
            
            duration = random.uniform(0.5, 1.5)
            pyautogui.moveTo(new_x, new_y, duration=duration)
            
            if self.language == "EN":
                status_text = f"Status: Active - Last move: {duration:.1f}s"
            else:
                status_text = f"وضعیت: فعال - آخرین حرکت: {duration:.1f}ثانیه"
            
            self.status_label.config(text=status_text)
            self.root.after(4000, self.move_mouse_randomly)
    
    def start_moving(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.state(['disabled'])
            self.stop_button.state(['!disabled'])
            
            if self.language == "EN":
                self.status_label.config(text="Status: Active - Moving...")
            else:
                self.status_label.config(text="وضعیت: فعال - در حال حرکت...")
            
            self.move_mouse_randomly()
    
    def stop_moving(self):
        if self.is_running:
            self.is_running = False
            self.start_button.state(['!disabled'])
            self.stop_button.state(['disabled'])
            
            if self.language == "EN":
                self.status_label.config(text="Status: Paused")
            else:
                self.status_label.config(text="وضعیت: متوقف شده")
    
    def on_close(self):
        if self.is_running:
            if messagebox.askokcancel("Exit", "Program is running. Are you sure you want to quit?"):
                self.root.destroy()
        else:
            self.root.destroy()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'420x250+{x}+{y}')

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = AntiIdlerApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Critical Error", f"Program encountered an error:\n{str(e)}")
        sys.exit(1)
