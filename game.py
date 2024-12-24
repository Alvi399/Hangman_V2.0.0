import pygame
import os

# Warna background
bg = (255, 255, 255)  # Putih

# Inisialisasi Pygame
pygame.init()

# Buat layar
screen_width, screen_height = 900, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asekk")

# Muat gambar hangman
image_path = ["./Asset/h1.png", "./Asset/h2.png", "./Asset/h3.png", "./Asset/h4.png", "./Asset/h5.png"]
images = []
position = (screen_width // 2 - 50, screen_height // 2 - 50)

for path in image_path:
    if not os.path.exists(path):
        print(f"File not found: {path}")  # Debugging jika file tidak ditemukan
    else:
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (100, 100))  # Ubah ukuran gambar
        images.append({"image": image, "pos": position})

# Variabel game
running = True
death = 0

while running:
    # Bersihkan layar
    screen.fill(bg)

    # Tampilkan gambar sesuai indeks "death"
    screen.blit(images[death]["image"], images[death]["pos"])

    # Membaca event di dalam game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            death = (death + 1) % len(images)  # Pergantian gambar
            print("berhasil di klik")

    # Perbarui tampilan layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
