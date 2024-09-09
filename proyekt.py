import tkinter as tk
from tkinter import messagebox
import random

class MilyoncuOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Milyoncu Oyunu")
        self.root.configure(bg='skyblue')  
        
        self.suallar = self.sorular_ve_cevaplar()
        self.suallar_index = 0
        self.toplam_qazanc = 0
        self.joker_isdedildi = False
        self.dosta_zeng_isdedildi = False
        
        self.sual_label = tk.Label(root, text="", wraplength=400, bg='skyblue', font=('Arial', 14))
        self.sual_label.pack(pady=20)
        
        self.cevap_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda idx=i: self.cavabla(idx), bg='lightgray')
            button.pack(fill='x', padx=20, pady=5)
            self.cevap_buttons.append(button)
        
        self.kazanc_label = tk.Label(root, text=f"Toplam qazanc: ${self.toplam_qazanc}", bg='skyblue', font=('Arial', 12))
        self.kazanc_label.pack(pady=20)
        
        self.joker_button = tk.Button(root, text="Joker istifadə et", command=self.joker, state=tk.NORMAL, bg='lightgray')
        self.joker_button.pack(pady=10)
        
        self.dosta_zeng_button = tk.Button(root, text="Dosta zəng", command=self.dosta_zeng, state=tk.NORMAL, bg='lightgray')
        self.dosta_zeng_button.pack(pady=10)
        
        self.yeni_sual()

    def sorular_ve_cevaplar(self):
        return [
            {"soru": "İspaniyanin paytaxti", "cavablar": ["Barcelona", "Madrid", "Sevilla", "Katalunya"], "duzgun_cavab": "Madrid"},
            {"soru": "Barcelona hansi ildən qurulub", "cavablar": ["1898", "1926", "1957", "1930"], "duzgun_cavab": "1898"},
            {"soru": "Fenerbahçe neçə ilində qurulub", "cavablar": ["1907", "1905", "1903", "1911"], "duzgun_cavab": "1907"},
            {"soru": "Neymar Barcelona'dan neçə ildə ayrilib", "cavablar": ["2021", "2016", "2017", "2018"], "duzgun_cavab": "2018"},
            {"soru": "Futbol hansi ölkədə tapilib", "cavablar": ["İngiltərə", "Braziliya", "Amerika", "Fransa"], "duzgun_cavab": "Braziliya"},
        ]

    def yeni_sual(self):
        if self.suallar_index < len(self.suallar):
            soru = self.suallar[self.suallar_index]
            self.sual_label.config(text=soru["soru"])
            for idx, cavab in enumerate(soru["cavablar"]):
                self.cevap_buttons[idx].config(text=cavab)
        else:
            messagebox.showinfo("Oyun bitdi", f"Oyun bitdi. Toplam qazanciniz: ${self.toplam_qazanc}")
            self.root.quit()

    def joker(self):
        if not self.joker_isdedildi:
            self.joker_isdedildi = True
            soru = self.suallar[self.suallar_index]
            duzgun_cavab = soru["duzgun_cavab"]
            sehvler = [cavab for cavab in soru["cavablar"] if cavab != duzgun_cavab]
            yanlislar = random.sample(sehvler, 2)
            joker_cavablar = [duzgun_cavab] + yanlislar
            random.shuffle(joker_cavablar)
            for idx, cavab in enumerate(joker_cavablar):
                self.cevap_buttons[idx].config(text=cavab)
        else:
            messagebox.showinfo("Joker istifadə edilib", "Joker haqqınız istifadə edilib.")

    def dosta_zeng(self):
        if not self.dosta_zeng_isdedildi:
            self.dosta_zeng_isdedildi = True
            soru = self.suallar[self.suallar_index]
            duzgun_cavab = soru["duzgun_cavab"]
            yardim = f"Düzgün cavab: {duzgun_cavab}" if messagebox.askyesno("Dosta zəng", f"Yardimcidan kömək istəyirsiniz?\nDüzgün cavab: {duzgun_cavab}") else "Yardımcından kömək alınmadı."
            messagebox.showinfo("Dosta zəng", yardim)
        else:
            messagebox.showinfo("Dosta zəng istifadə edilib", "Dosta zəng haqqinizdan istifadə edildiniz.")

    def cavabla(self, index):
        soru = self.suallar[self.suallar_index]
        if soru["cavablar"][index] == soru["duzgun_cavab"]:
            self.toplam_qazanc += 500
            self.kazanc_label.config(text=f"Toplam qazanc: ${self.toplam_qazanc}")
            messagebox.showinfo("Düzgün", "Düzgün cavab!")
        else:
            messagebox.showinfo("Səhv", "Səhv cavab! Oyun bitdi.")
            self.root.quit()
        self.suallar_index += 1
        self.yeni_sual()

if __name__ == "__main__":
    root = tk.Tk()
    oyunu = MilyoncuOyunu(root)
    root.mainloop()
