class Matakuliah():

    def __init__(self, input_nama, input_sks):
        self.nama = input_nama
        self.sks = input_sks


mk1 = Matakuliah("Pemrograman Visual", "4 sks")
mk2 = Matakuliah("Keamanan Jaringan", "3 sks")
print(mk1)
print(mk1.__dict__)
