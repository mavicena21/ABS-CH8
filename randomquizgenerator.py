import random
#ibukota
ibukota = {'Aceh': 'Banda Aceh',
           'Sumatera Utara': 'Medan',
           'Sumatera Barat': 'Padang',
           'Riau': 'Pekanbaru',
           'Kepulauan Riau': 'Tanjungpinang',
           'Jambi': 'Jambi',
           'Sumatera Selatan': 'Palembang',
           'Kepulauan Bangka Belitung': 'Pangkal Pinang',
           'Bengkulu': 'Bengkulu',
           'Lampung': 'Bandar Lampung',
           'DKI Jakarta': 'Jakarta',
           'Banten': 'Serang',
           'Jawa Barat': 'Bandung',
           'Jawa Tengah': 'Semarang',
           'DI Yogyakarta': 'Yogyakarta',
           'Jawa Timur': 'Surabaya',
           'Bali': 'Denpasar',
           'Nusa Tenggara Barat': 'Mataram',
           'Nusa Tenggara Timur': 'Kupang',
           'Kalimantan Barat': 'Pontianak',
           'Kalimantan Tengah': 'Palangkaraya',
           'Kalimantan Selatan': 'Banjarmasin',
           'Kalimantan Timur': 'Samarinda',
           'Kalimantan Utara': 'Tanjung Selor',
           'Sulawesi Utara': 'Manado',
           'Gorontalo': 'Gorontalo',
           'Sulawesi Tengah': 'Palu',
           'Sulawesi Barat': 'Mamuju',
           'Sulawesi Selatan': ' Makassar',
           'Sulawesi Tenggara': 'Kendari',
           'Maluku': 'Ambon',
           'Maluku Utara': 'Sofifi',
           'Papua Barat': 'Manokwari',
           'Papua': 'Jayapura'}

# buat 20 file quiz dan jawabannya
for quiznum in range(20):
    quizfile = open('ibukotaquiz%s.txt' % (quiznum + 1), 'w')
    answerkeyfile = open('ibukotaquiz_answer%s.txt' % (quiznum + 1), 'w')

    # tulis header quiz
    quizfile.write('Nama:\n\nTanggal:\n\nKelas:\n\n')
    quizfile.write((' ' * 20) + 'Quiz Ibukota Provinsi Indonesia (Form %s)' % (quiznum + 1))

    # Acak urutan provinsi
    provinsi = list(ibukota.keys())
    random.shuffle(provinsi)


    for questionnum in range(34):
        jawabanbenar = ibukota[provinsi[questionnum]]
        jawabansalah = list(ibukota.values())
        del jawabansalah[jawabansalah.index(jawabanbenar)]
        jawabansalah = random.sample(jawabansalah, 3)
        pilgan = jawabansalah + [jawabanbenar]
        random.shuffle(pilgan)

        # tulis jawaban dan pilihan ganda pada quiz file
        quizfile.write('%s. Apa ibukota dari %s?\n' % (questionnum + 1, provinsi[questionnum]))
        for i in range(4):
            quizfile.write('    %s. %s\n' % ('ABCD'[i], pilgan[i]))
        quizfile.write('\n')

        # tulis jawaban di file kunci jawaban
        answerkeyfile.write('%s. %s\n' % (questionnum + 1, 'ABCD'[
            pilgan.index(jawabanbenar)]))

    quizfile.close()
    answerkeyfile.close()