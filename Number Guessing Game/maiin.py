import random

# Menyimpan riwayat permainan
riwayat = []


def mulai_game():
    print("\n🎮 === GAME TEBAK ANGKA ===")
    print("Saya memilih angka dari 1 - 10")
    print("Coba tebak angka tersebut!\n")

    angka_rahasia = random.randint(1, 10)

    percobaan = 0
    skor = 100

    while True:
        try:
            tebakan = int(input("Masukkan tebakan kamu: "))
            percobaan += 1

            if tebakan < 1 or tebakan > 10:
                print("⚠️ Masukkan angka antara 1-10!")
                continue

            if tebakan == angka_rahasia:
                print("\n🎉 BENAR!")
                print(f"Angka rahasia: {angka_rahasia}")
                print(f"Jumlah percobaan: {percobaan}")

                skor -= (percobaan - 1) * 10

                if skor < 0:
                    skor = 0

                print(f"⭐ Skor kamu: {skor}")

                riwayat.append({
                    "percobaan": percobaan,
                    "skor": skor
                })

                break

            elif tebakan < angka_rahasia:
                print("⬆️ Terlalu kecil!")

            else:
                print("⬇️ Terlalu besar!")

            skor -= 10

        except ValueError:
            print("❌ Masukkan angka saja!")


def lihat_riwayat():
    print("\n📜 === RIWAYAT PERMAINAN ===")

    if len(riwayat) == 0:
        print("Belum ada permainan.")
    else:
        for i, game in enumerate(riwayat, start=1):
            print(
                f"{i}. Percobaan: {game['percobaan']} | Skor: {game['skor']}"
            )


def menu():
    while True:
        print("\n====================")
        print("🎮 TEBAK ANGKA GAME")
        print("====================")
        print("1. Mulai Game")
        print("2. Lihat Riwayat")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mulai_game()

        elif pilihan == "2":
            lihat_riwayat()

        elif pilihan == "3":
            print("Terima kasih sudah bermain! 👋")
            break

        else:
            print("Pilihan tidak tersedia!")


# Program utama
menu()