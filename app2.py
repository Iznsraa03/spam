import pyautogui, time

time.sleep(5)  # Memberikan waktu sebelum eksekusi dimulai

# Membuka file hang.txt dan membaca seluruh isinya
with open("hang.txt", "r") as tulisan:
    content = tulisan.read()  # Membaca semua teks sekaligus

# Mengirim seluruh teks dalam satu kali kirim
pyautogui.typewrite(content)
pyautogui.press('enter')  # Menekan enter setelah semua teks dikirim