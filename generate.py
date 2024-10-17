import random
from datetime import datetime
import string

# Fungsi untuk generate teks log secara acak dengan karakter tambahan
def generate_log(num_lines):
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "*VIRUS* login",
        "File not found",
        "Connection established",
        "Error writing file",
        "Timeout occurred",
        "Data saved",
        "Memory allocation failed"
    ]
    
    logs = []
    
    for _ in range(num_lines):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format waktu sekarang
        level = random.choice(log_levels)  # Pilih level log acak
        message = random.choice(messages)  # Pilih pesan acak
        
        # Tambahkan karakter acak (misalnya, 1-5 karakter)
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 100)))
        
        log = f"{timestamp} [{level}] {message} {random_chars}"  # Format log dengan karakter acak
        logs.append(log)
    
    return "\n".join(logs)

# Menyimpan log ke dalam file teks
def save_to_file(filename, num_lines):
    logs = generate_log(num_lines)
    with open(filename, "w") as file:
        file.write(logs)

# Panggil fungsi untuk generate dan simpan log dalam file
filename = "generated_logs.txt"
num_lines = 1000  # Jumlah baris log yang ingin di-generate
save_to_file(filename, num_lines)

print(f"Log otomatis telah di-generate dan disimpan di {filename}")