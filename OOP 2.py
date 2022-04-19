class Buah:
    def __init__(self, inputNama, inputWarna, inputJumlah):
        self.nama = inputNama
        self.warna = inputWarna
        self.jumlah = inputJumlah


Buah1 = Buah('cherri', 'Merah', '3 buah')
Buah2 = Buah("nanas", "Kuning", "5 buah")

print(Buah1.nama, Buah1.warna, Buah1.jumlah)
