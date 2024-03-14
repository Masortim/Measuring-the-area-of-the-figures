from PIL import Image
import cv2
import numpy as np

def calculate_area_and_edges(image_path):
  # Открыть изображение с помощью Pillow для извлечения информации о DPI
  pil_image = Image.open(image_path)
  try:
    dpi = pil_image.info['dpi'][0]  # Предполагаем, что DPI одинаков в обоих направлениях
    scale = 2.54 / dpi  # Конвертировать DPI в масштаб в см на пиксель (так как в дюйме 2.54 см)
  except KeyError:
    print("Информация о DPI не найдена. Используется стандартный масштаб.")
    scale = 0.1  # Запасной масштаб, если информация о DPI недоступна

  # Продолжить обработку с помощью OpenCV
  image = cv2.imread(image_path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  # Обнаружить края и найти контуры
  edged = cv2.Canny(blurred, 50, 150)
  contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  for cnt in contours:
    area = cv2.contourArea(cnt)
    real_area = area * (scale ** 2)
    print(f"Площадь фигуры: {real_area} см²")

    # Найти минимальную описывающую окружность
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    circle_area = np.pi * (radius ** 2)
     
    # Проверить, является ли контур окружностью
    if abs(circle_area - area) / area < 0.1:  # Допустимая ошибка 10%
      circumference = 2 * np.pi * radius * scale
      print(f"Длина окружности: {circumference} см")
    else:
      # Вычислить длину контура (периметр)
      perimeter = cv2.arcLength(cnt, True)
      real_perimeter = perimeter * scale
      print(f"Периметр фигуры: {real_perimeter} см")

      # Получить аппроксимированные контуры
      epsilon = 0.02 * cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, epsilon, True)

      # Вывести длину каждой стороны
      for i in range(len(approx)):
        p1 = approx[i][0]
        p2 = approx[(i + 1) % len(approx)][0]  # Последняя точка соединяется с первой
        edge_length = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) * scale
        print(f"Длина стороны {i + 1}: {edge_length} см")

# Предположим, что каждый пиксель равен 0.1 см
PIXEL_TO_CM = 0.1

# Путь к изображению
image_path = 'shapes/square.jpg' 
                       # rectangle.jpg
                       # star.png
                       # triangle.png
                       # circle.png
                       # square.jpg

calculate_area_and_edges(image_path)
