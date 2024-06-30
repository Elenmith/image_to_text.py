#Na komputerze zainstaluj 
# pip install pytesseract 
# pip install pillow 
# pip install opencv-python
# pobierz https://github.com/UB-Mannheim/tesseract/wiki i zapamiętaj ścieżkę, bo podaje się ją poniżej

# Następnie import bibliotek

from PIL import Image
import pytesseract 
import cv2
import os

# Na windowsie należy podać ścieżkę
# ścieżka
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
 
# Otwarcie pliku
# Plik kopiuj jako ścieżkę 

# img = Image.open("C:\\Users\Lenovo\Desktop\InstagramKody")
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\InstagramKody\\1.jpg')

# Sprawdzenie, czy obraz został poprawnie wczytany
if img is None:
    raise FileNotFoundError("Obraz nie został wczytany. Sprawdź ścieżkę do pliku.")
 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Konwersja zdjęcia na tekst

text = pytesseract.image_to_string(gray)
 
folder_path = os.path.dirname('C:\\Users\\Lenovo\\Desktop\\InstagramKody\\')

# Ścieżka do pliku tekstowego
text_file_path = os.path.join(folder_path, 'Tekst.txt')

# Zapisanie tekstu do pliku
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text)

print(f"Tekst został zapisany do pliku: {text_file_path}")