class Mahasiswa:

    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Nama: {self.__merk}')


nama = Mahasiswa('Muh.Ali - D0219012')
nama.tampilkan_merk()
