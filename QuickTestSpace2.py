import pyautogui
import time

# Współrzędne trzech miejsc na ekranie
positions = [(486, 440), (476, 836), (1001, 563)]
pyautogui.move()
try:
    while True:
        for pos in positions:
            pyautogui.move(pos)  # Kliknięcie w pozycję
            time.sleep(1)  # Opóźnienie między kliknięciami
        time.sleep(2)
except KeyboardInterrupt:
    print("Program zakończony.")
