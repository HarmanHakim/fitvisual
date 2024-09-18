Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Membuat sebuah proyek Django, yang bernama fitvisual kemudian dihubungkan ke repo di GitHub
- Dilanjutkan dengan membuat aplikasi dengan nama main pada proyeknya
- Routing pada prroyek agar dapat dijalankan dalam app main
- Membuat Model Product pada main di file models.py, kemudian define atribute name, harga, description
- Membuat fungsi di views.py untuk menampilkan data 
- Membuat routing di urls.py
- Melakukan Deployment ke PWS setelah selesai


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Harman](https://github.com/user-attachments/assets/9a79c29f-2cee-463b-b516-7bd935f2045e)




Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah alat yang sangat penting dalam pengembangan perangkat lunak karena memungkinkan pengembang untuk melacak perubahan kode secara efektif, bekerja sama dalam tim dengan mudah, dan membuat cadangan kode. Dengan Git, kami bisa dengan bebas bereksperimen tanpa takut merusak kode utama dikarenakan dapat kembali ke versi sebelumnya jika diperlukan. Selain itu Git juga bisa berkolaborasi dengan orang lain dengan fitur sepereti branch dan merge



Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena kemudahannya dalam dipahami dan kelengkapan fitur-fiturnya. Selain itu, Django hadir dengan banyak fitur bawaan yang berguna, seperti ORM, sistem templating, dan sistem autentikasi pengguna, sehingga kami dapat membangun aplikasi web yang kompleks dengan lebih cepat. Bahasa Python yang mendasari Django juga dikenal mudah dipelajari dan memiliki sintaks yang bersih, membuatnya menjadi pilihan yang populer di berbagai bidang.



Mengapa model pada Django disebut sebagai ORM?
Model di Django disebut ORM (Object-Relational Mapping) karena menghubungkan objek Python dengan tabel database. ORM adalah teknik yang memungkinkan untuk berinteraksi dengan database menggunakan objek dan kelas dalam kode Python tanpa perlu menulis SQL secara langsung



Soal Tugas 2 
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery untuk
- Efisiensi Operasional
Data delivery membuat kita dapat mengirim data yang cepat dan akurat, sehingga memudahkan pengelolaan operasional. Contohnya, dalam sistem pengiriman barang, data delivery dapat menyajikan informasi real-time tentang status pengiriman, seperti lokasi dan waktu kedatangan, sehingga memperbaiki kepuasan pelanggan dan meningkatkan efisiensi logistik.
- Transparansi dan Akuntabilitas
Data delivery memberikan transparansi dalam proses pengiriman data. Contohnya, dalam platform pembayaran pemerintah, data delivery  menyajikan informasi transaksi secara digital, meminimalkan biaya penyimpanan dokumen, dan meningkatkan akuntabilitas dalam proses pembayaran.
- Penggunaan Teknologi yang Efektif
Data delivery seringkali menggunakan teknologi seperti IoT (Internet of Things) dan platform seperti Google Cloud Pub/Sub, yang memungkinkan pengiriman data dalam skala besar dengan keandalan tinggi. Contohnya, dalam implementasi IoT oleh Antares, data delivery memungkinkan pengiriman data real-time tentang kebocoran air, meminimalisir kebocoran dan meningkatkan efisiensi pengelolaan air minum.
- Pengurangan Biaya
Data delivery dapat mengurangi biaya operasional dengan mengurangi kebutuhan untuk dokumen fisik dan kurir. Contohnya, dalam implementasi platform pembayaran pemerintah, data delivery memungkinkan transaksi digital tanpa media kertas, mengurangi biaya penyimpanan dokumen dan kurir.
- Peningkatan Kualitas Layanan
Data delivery memungkinkan penyajian informasi yang akurat dan real-time, sehingga meningkatkan kualitas layanan. Contohnya, dalam sistem pengiriman barang, data delivery dapat memberikan ETA (Estimated Time of Arrival) yang akurat, memudahkan pengambilan keputusan dan meningkatkan kepuasan pelanggan.

Dengan demikian, data delivery adalah komponen penting dalam pengimplementasian sebuah platform karena memungkinkan efisiensi operasional, transparansi, akuntabilitas, penggunaan teknologi yang efektif, pengurangan biaya, dan peningkatan kualitas layanan.



2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik dan lebih populer dibandingkan XML karena beberapa alasan:
- Simplicity dan Kompatibilitas
JSON memiliki sintaks yang lebih sederhana dan mudah dibaca, membuatnya lebih fleksibel dan mudah digunakan dalam berbagai konteks, terutama dalam pengembangan web dan aplikasi seluler. XML, meskipun memiliki kelebihan dalam struktur dokumen yang kompleks, memiliki sintaks yang lebih bertele-tele dan memerlukan parser khusus untuk penguraian, sehingga lebih sulit digunakan.
- Kecepatan dan Efisiensi
JSON lebih cepat dalam parsing data karena dapat diuraikan dengan fungsi JavaScript standar, sedangkan XML memerlukan pengurai khusus yang lebih lambat. JSON juga memiliki ukuran yang lebih kecil, sehingga lebih efisien dalam pengiriman data melalui jaringan.
- Kompatibilitas dengan JavaScript
JSON dirancang untuk kompatibilitas dengan JavaScript, sehingga dapat langsung diproses sebagai objek JavaScript, yang membuatnya sangat mudah digunakan dalam pengembangan web. XML, meskipun dapat digunakan dengan berbagai bahasa pemrograman, tidak memiliki integrasi yang sebaik dengan JavaScript seperti JSON.
- Penggunaan dalam Web Development
JSON sangat populer dalam pengembangan web karena dapat digunakan dalam AJAX requests dan REST APIs, serta mendukung penyimpanan data yang lebih ringan dan cepat. XML, meskipun masih digunakan dalam beberapa konteks, tidak sepopuler JSON dalam pengembangan web modern.

Oleh karean itu JSON lebih populer karena kelebihan-kelebihannya dalam hal simpelitas, kecepatan, dan kompatibilitas dengan JavaScript, lebih ideal untuk penggunaan dalam pengembangan web dan aplikasi seluler.



3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Metode is_valid() pada form Django adalah sebuah fungsi yang sangat penting dalam proses validasi data :

Fungsi is_valid()
- Validasi Data 
Metode is_valid() digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Ini berarti bahwa metode ini akan memeriksa apakah data yang diinputkan memenuhi semua aturan validasi yang telah ditetapkan untuk form tersebut.
- Pengecekan Aturan Validasi 
Metode ini akan memeriksa setiap field form dan memastikan bahwa data yang diinputkan tidak mengandung kesalahan. Jika semua data valid, maka metode is_valid() akan mengembalikan nilai True, sedangkan jika ada kesalahan, maka akan mengembalikan nilai False.
- Penggunaan dalam Model Forms 
Pada model forms, metode is_valid() juga akan memanggil metode full_clean() pada instance model untuk memvalidasi data secara lebih lanjut, termasuk memastikan bahwa field-field yang unik memenuhi syarat unikitas.

Kebutuhan Metode is_valid()
- Menghindari Kesalahan 
Dengan menggunakan metode is_valid(), pengembang dapat menghindari kesalahan yang mungkin terjadi karena input yang tidak valid. Ini memastikan bahwa data yang disimpan ke dalam database adalah akurat dan valid.
- Meningkatkan Kualitas Aplikasi 
Metode ini membantu meningkatkan kualitas aplikasi Django dengan memastikan bahwa pengguna tidak dapat menyimpan data yang tidak valid. Hal ini juga meningkatkan kepercayaan pengguna terhadap aplikasi.
- Mengurangi Kerusakan Data 
Dengan memvalidasi data sebelum disimpan, metode is_valid() dapat mengurangi kerusakan data yang mungkin terjadi karena input yang tidak valid. Ini sangat penting dalam aplikasi yang membutuhkan data yang akurat dan terpercaya.



4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token (Cross-Site Request Forgery token) adalah sebuah fitur keamanan yang sangat penting dalam Django untuk mencegah serangan Cross-Site Request Forgery (CSRF):

- Mencegah Serangan CSRF
CSRF adalah serangan yang memanfaatkan keadaan pengguna sudah terautentikasi di suatu situs web. Serangan ini dapat membuat pengguna melakukan aksi yang tidak mereka inginkan, seperti transfer dana, perubahan email, dan lain-lain. Dengan menggunakan csrf_token, Django dapat memastikan bahwa setiap permintaan POST yang masuk dari pengguna adalah valid dan berasal dari pengguna yang sudah terautentikasi.

Jika kita tidak menambahkan csrf_token pada form Django, maka penggunaan form tersebut dapat terbuka bagi serangan CSRF. Berikut adalah apa yang dapat terjadi:

- Serangan CSRF Berhasil
Tanpa csrf_token, serangan CSRF dapat berhasil dan membuat pengguna melakukan aksi yang tidak mereka inginkan. Contohnya, serangan dapat membuat pengguna transfer dana atau perubahan email tanpa mereka sadari.
- Kerusakan Data dan Keamanan
Serangan CSRF yang berhasil dapat menyebabkan kerusakan data dan keamanan. Hal ini karena serangan dapat memanfaatkan keadaan pengguna sudah terautentikasi untuk melakukan aksi yang tidak sah.

Penyerang dapat memanfaatkan kekurangan csrf_token dengan cara berikut:

- Membuat Link atau Form Malicious
Penyerang dapat membuat link atau form yang mengandung permintaan POST yang tidak valid. Jika pengguna yang sudah terautentikasi mengklik link atau mengisi form tersebut, maka permintaan POST tersebut akan dijalankan tanpa memeriksa apakah memiliki csrf_token yang valid.
- Menggunakan Token Lain
Penyerang juga dapat mencoba menggunakan token lain yang tidak valid untuk mengelabui sistem. Namun, karena csrf_token di-Django selalu diubah secara acak setiap kali pengguna login, maka kemungkinan ini sangat kecil.

Dengan demikian, menambahkan csrf_token pada form Django adalah sangat penting untuk mencegah serangan CSRF dan menjaga keamanan aplikasi.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Langkah 1 : Membuat Input Form untuk Menambahkan Objek Model
- Menentukan Model
- Membuat Form untuk Model
- Membuat View untuk Form Input
- Membuat Template

Langkah 2 : Membuat 4 Fungsi Views untuk Menampilkan Data dalam Format XML dan JSON
- View untuk Menampilkan Semua Objek dalam Format JSON
- View untuk Menampilkan Semua Objek dalam Format XML
- View untuk Menampilkan Objek Berdasarkan ID dalam Format JSON
- View untuk Menampilkan Objek Berdasarkan ID dalam Format XML

Langkah 3 : Membuat Routing URL untuk Setiap Views
- Menambahkan URL pada urls.py

Langkah 4 : Testing dan Penyempurnaan

![json](./public/image/json.png)
![json](./public/image/jsonid.png)
![xml](./public/image/xml.png)
![xml](./public/image/xmlid.png)