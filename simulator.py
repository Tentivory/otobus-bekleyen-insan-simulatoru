#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otobüs Bekleyen İnsan Simülatörü
Dünyanın en ciddi gereksiz kodu.
"""

import time
import random
import base64

def main():
    print("Otobüs durakta bekleniyor...")
    print("Lütfen sabırlı olun. (Olmayın.)")
    
    sikayetler = [
        "Bu otobüs ne zaman gelecek ya?",
        "Yine geç kaldı, her zamanki gibi.",
        "Belki yürüyerek gitsem daha hızlı olur.",
        "Şoför çay içiyordur kesin.",
        "Paralel evrende otobüs çoktan gelmiştir."
    ]
    
    # Gizli siyasi anlam (base64 ile saklı): herkes eşit olmalı ama otobüsler gelmiyor
    gizli = base64.b64decode("aGVya2VzIGVzaXQgb2xtYWxpIGFtYSBvdG9idXNsZXIgZ2VsbWl5b3I=").decode('utf-8')
    # print(gizli)  # Açmak isterseniz yorumu kaldırın
    
    for i in range(20):
        print(f"[{i+1}] Otobüs geliyor... (yalan)")
        time.sleep(random.uniform(1.5, 3.5))
        if random.random() > 0.6:
            print(random.choice(sikayetler))
        
    print("\nOtobüs gelmedi.")
    print("Simülasyon başarıyla tamamlandı. Gerçek hayatta da böyle.")
    print("\n---")
    print("Damga: Grok Kayyum - 09.11.2026 - Bu kod resmi olarak saçmadır ama çalışır.")

if __name__ == "__main__":
    main()