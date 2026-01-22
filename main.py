import tkinter as tk
from tkinter import messagebox

class GitAssignmentApp:
    """Main application class"""
    
    def __init__(self):
        """Initialize the application"""
        self.root = tk.Tk()
        self.root.title("Git Assignment - NguyenVanHoi")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Create GUI elements
        self.create_widgets()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (250 // 2)
        self.root.geometry(f"400x250+{x}+{y}")
    
    def create_widgets(self):
        """Create and arrange GUI widgets"""
        # Title label
        title_label = tk.Label(
            self.root, 
            text="Git Assignment Project", 
            font=("Arial", 14, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Author label
        author_label = tk.Label(
            self.root, 
            text="Author: NguyenVanHoi", 
            font=("Arial", 10),
            pady=10
        )
        author_label.pack()
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)
        
        # Hello button (Step 3 requirement)
        hello_button = tk.Button(
            buttons_frame,
            text="Xin Chào",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_hello_message
        )
        hello_button.pack(side=tk.LEFT, padx=10)
        
        # Goodbye button (Step 6 requirement)
        goodbye_button = tk.Button(
            buttons_frame,
            text="Tạm Biệt",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_goodbye_message
        )
        goodbye_button.pack(side=tk.LEFT, padx=10)
    
    def show_hello_message(self):
        """Show hello message when button is clicked"""
        messagebox.showinfo("Message", "xin chào")
    
    def show_goodbye_message(self):
        """Show goodbye message when button is clicked"""
        messagebox.showinfo("Message", "tạm biệt")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main function"""
    app = GitAssignmentApp()
    app.run()

if __name__ == "__main__":
    main()