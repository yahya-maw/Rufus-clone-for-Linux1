import customtkinter as ctk

class RufusLinux(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rufus for Linux (Fedora Ultra)")
        self.geometry("400x700")

        # 1. اختيار الجهاز (Device)
        self.lbl1 = ctk.CTkLabel(self, text="Device", anchor="w")
        self.lbl1.pack(fill="x", padx=20, pady=(20,0))
        self.dev_box = ctk.CTkComboBox(self, values=["No USB Found"], width=350)
        self.dev_box.pack(padx=20, pady=5)

        # 2. اختيار الـ ISO
        self.lbl2 = ctk.CTkLabel(self, text="Boot selection", anchor="w")
        self.lbl2.pack(fill="x", padx=20, pady=(15,0))
        self.btn_iso = ctk.CTkButton(self, text="SELECT ISO", fg_color="gray")
        self.btn_iso.pack(padx=20, pady=5)

        # 3. الـ Persistence (السلايدر السحري)
        self.lbl3 = ctk.CTkLabel(self, text="Persistent partition size", anchor="w")
        self.lbl3.pack(fill="x", padx=20, pady=(15,0))
        self.persistence_slider = ctk.CTkSlider(self, from_=0, to=8) # من 0 لـ 8 جيجا
        self.persistence_slider.pack(padx=20, pady=5)

        # 4. الـ Partition Scheme (نفس خيارات روفوس)
        self.lbl4 = ctk.CTkLabel(self, text="Partition scheme", anchor="w")
        self.lbl4.pack(fill="x", padx=20, pady=(15,0))
        self.pt_box = ctk.CTkComboBox(self, values=["GPT", "MBR"])
        self.pt_box.pack(padx=20, pady=5)

        # زر START
        self.start_btn = ctk.CTkButton(self, text="START", fg_color="#2b5797", height=45)
        self.start_btn.pack(side="bottom", pady=40, padx=20, fill="x")

if __name__ == "__main__":
    app = RufusLinux()
    app.mainloop()
