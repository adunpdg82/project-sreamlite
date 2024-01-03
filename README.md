# project-sreamlite
Proyek ini adalah sebuah demo aplikasi web yang dibuat dengan streamlite. Aplikasi ini menampilkan data udara di kota Ghuceng dari tahun 2013 sampai tahun 2017.

##Instalasi dan Menjalankan Streamlite Pada Local Host
Untuk menjalankan aplikasi ini, Anda perlu menginstal streamlite dengan menggunakan pip

pip install -q streamlit

kemudian siapkan file yang akan menjalankan perintah untuk membaca data dan juga menampilakn tabel serta grafi 
dalam hal ini saya membuat file bernama air.py yang berisi kode aplikasi berbasis python
kemudian jalankan perintah:

!wget -q -O - ipv4.icanhazip.com

ini akan menghasilkan alamat IP secara acak, sebagai contoh ketika saya menjalannya file ini menghasilkan alamat ip server:
35.237.254.246 (alamat ini akan berubah setiap kali dijalankan)

untuk melihat tampilan pada server tersebut diperlukan perintah :
! streamlit run air.py & npx localtunnel --port 8501

yang menghasilkan:

                  You can now view your Streamlit app in your browser.
                  
                    Network URL: http://172.28.0.12:8501
                    External URL: http://35.237.254.246:8501
                  
                  npx: installed 22 in 2.53s
                  your url is: https://cyan-shirts-give.loca.lt (alamat ini akan berubah setiap dijalankan)


untuk melihat tampilan pada web kita dapat mengunjungi 
(https://cyan-shirts-give.loca.lt)
dan pada Endpoint IP: d
silahkan disikan alamat IP :35.237.254.246
kemudian silahkan tekan  tombol "Click to Submit"
maka tampilan pada web akan muncul
