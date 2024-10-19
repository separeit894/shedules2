from PIL import Image

# Загрузите изображение

def cropped():
    for i in range(0, 14):
        image = Image.open(f'photo/page{i}.png')

        # Определите координаты для обрезки (left, upper, right, lower)
        left = 100
        upper = 300
        right = 1500
        lower = 2100

        # Обрежьте изображение
        cropped_image = image.crop((left, upper, right, lower))

        # Сохраните обрезанное изображение
        cropped_image.save(f'corrected_photo/page{i}.png')
        print(f"Фото № {i} корректировано")
