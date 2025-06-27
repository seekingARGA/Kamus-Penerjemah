meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "TS": "singkatan kata this",
            "PMO": "singkatan kata piss me off, digunakan saat sedang marah"
            }

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word in meme_dict.keys():
        print("Makna kata", word,"adalah", meme_dict[word])
    else:
        print("Kata tidak ditemukan.")
