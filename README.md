# OCR Script - ReadMe

## Opis Projektu

#### Ten skrypt wykorzystuje bibliotekę Tesseract OCR do konwersji tekstu z obrazów na format tekstowy. Umożliwia wczytanie obrazu, przetworzenie go do skali szarości, a następnie wyekstrahowanie tekstu, który zostaje zapisany w pliku tekstowym na dysku.

## Wymagania

Przed uruchomieniem skryptu należy upewnić się, że spełnione są następujące wymagania:

### 1. Oprogramowanie:

Python 3.x

Tesseract OCR (link do pobrania)

### 2. Biblioteki Pythona:

Zainstaluj wymagane biblioteki za pomocą polecenia:
```
pip install pytesseract pillow opencv-python
```
## Konfiguracja

### 1. Instalacja Tesseract OCR:

Pobierz i zainstaluj Tesseract OCR zgodnie z podanym linkiem.

Podczas instalacji zapamiętaj ścieżkę instalacji, np. C:\Program Files\Tesseract-OCR\tesseract.exe.

### 2. Edycja skryptu:

W skrypcie podaj poprawną ścieżkę do pliku wykonywalnego Tesseract:
```
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```
Podaj również ścieżkę do obrazu, który chcesz przetworzyć:
```
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\InstagramKody\\1.jpg')
```
## Uruchomienie

Upewnij się, że wszystkie wymagania zostały spełnione.

Otwórz terminal lub wiersz poleceń w katalogu, gdzie znajduje się skrypt.

### Uruchom skrypt za pomocą polecenia:
```
python skrypt.py
```
### Po zakończeniu działania skryptu, plik tekstowy z wynikiem znajdziesz w tym samym katalogu, co obraz.

## Funkcjonalności

Wczytywanie obrazu: Skrypt obsługuje obrazy w formacie JPG.

Przetwarzanie obrazu: Konwersja obrazu do skali szarości w celu poprawy jakości ekstrakcji tekstu.

Ekstrakcja tekstu: Tekst jest odczytywany z obrazu za pomocą Tesseract OCR.

Zapis do pliku: Wynikowa treść zostaje zapisana w pliku tekstowym Tekst.txt w tym samym folderze co obraz.

## Problemy i Rozwiązania

1. Obraz nie został wczytany:

* Sprawdź ścieżkę do obrazu. Upewnij się, że podana ścieżka jest poprawna i obraz istnieje w podanej lokalizacji.

2. Tesseract nie działa:

* Sprawdź, czy poprawnie zainstalowano Tesseract i czy ścieżka w skrypcie jest zgodna z lokalizacją pliku tesseract.exe na Twoim komputerze.

## Dalszy Rozwój

Możesz rozbudować skrypt o:

* Obsługę większej liczby formatów obrazów.

* Możliwość wczytywania wielu obrazów z katalogu.

* Opcje poprawy jakości obrazu (np. filtrowanie, zwiększanie kontrastu).

* Interfejs graficzny (GUI) do obsługi skryptu.

