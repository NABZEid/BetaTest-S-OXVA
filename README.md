# BetaTest-S-OXVA
📌 Cara Memasang Script BetaTest S-OXVA dari GitHub

🔹 1. Install Termux & Paket Pendukung

Sebelum meng-clone repository, pastikan Termux sudah terinstall dan diperbarui:

pkg update && pkg upgrade -y
pkg install git -y
pkg install bash -y


---

🔹 2. Clone Repository dari GitHub

Gunakan perintah berikut untuk mendownload script dari repository GitHub:

git clone https://github.com/NABZEid/BetaTest-S-OXVA.git


---

🔹 3. Masuk ke Folder Repository

Setelah berhasil di-clone, masuk ke dalam direktori repository:

cd BetaTest-S-OXVA


---

🔹 4. Beri Izin Eksekusi pada File Script

Jika ada file script .sh atau .py, beri izin eksekusi dengan perintah berikut:

chmod +x namafile.sh
chmod +x namafile.py


---

🔹 5. Menjalankan Script

Untuk menjalankan script, gunakan perintah:

Jika script menggunakan Bash:

./namafile.sh

Jika script menggunakan Python:

python namafile.py



---

🔹 6. Mengupdate Script dari GitHub

Jika ada pembaruan pada repository GitHub, lakukan update dengan perintah:

cd BetaTest-S-OXVA
git pull


---

🔹 7. Menghapus Repository Jika Diperlukan

Jika ingin menghapus repository yang sudah di-clone:

rm -rf BetaTest-S-OXVA
