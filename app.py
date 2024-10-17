import pyautogui, time

time.sleep(2)  # Waktu tunggu sebelum mulai mengetik (bisa dikurangi)

with open("test.txt", "r") as tulisan:
    for text in tulisan:
        pyautogui.typewrite(text, interval=0)  # Mengirim teks tanpa jeda antar karakter
        pyautogui.press('enter')  # Menekan enter setelah mengirim tiap baris