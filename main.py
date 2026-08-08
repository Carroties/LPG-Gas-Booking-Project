# Nilai per mata kuliah
nilai_matkul = [
    ('DDP1', 92),
    ('Kalkulus', 90)
]
# Fungsi mencetak daftar nilai Dek Depe
def data_hilang(lst):
    print(f'''
=========================
Daftar Nilai Dek Depe
=========================
Jumlah mata kuliah: {len(nilai_matkul)}
{nilai_matkul[0][0]:<11}|{nilai_matkul[0][1]:^11}
{nilai_matkul[1][0]:<11}|{nilai_matkul[1][1]:^11}
{nilai_matkul[2][0]:<11}|{nilai_matkul[2][1]:^11}
''')

# Input dari matkul dan nilai yang hilang
matkul_hilang = input()
nilai_hilang = int(input())

# Memasukkan matkul dan nilai yang hilang ke nilai_matkul
matkul_baru = (matkul_hilang, nilai_hilang)
nilai_matkul.append(matkul_baru)

# Memanggil fungsi "dataHilang"
data_hilang(nilai_matkul)
