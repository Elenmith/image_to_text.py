from PIL import Image
import pytesseract 
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
 
img = Image.open("C:\\Users\Lenovo\Desktop\InstagramKody")
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\InstagramKody\\1.jpg')

if img is None:
    raise FileNotFoundError("Obraz nie został wczytany. Sprawdź ścieżkę do pliku.")
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
 
folder_path = os.path.dirname('C:\\Users\\Lenovo\\Desktop\\InstagramKody\\')

text_file_path = os.path.join(folder_path, 'Tekst.txt')

with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text)

print(f"Tekst został zapisany do pliku: {text_file_path}")
