import cv2
import face_recognition
import sys
import tkinter as tk
from tkinter import messagebox
import time
import os

# Cargar la imagen de referencia (tú)
known_image = face_recognition.load_image_file("gael.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Cargar la cámaraCLS

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Detectar rostros en el frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Comparar el rostro detectado con el conocido
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

        if matches[0]:
            root = tk.Tk()
            root.withdraw()  # Oculta la ventana principal
            messagebox.showinfo("Información", "Hola Gael")
            root.destroy()
            sys.exit()

        else:
            root = tk.Tk()
            root.withdraw()  # Oculta la ventana principal
            messagebox.showwarning("Advertencia", "Rostro no reconocido")

            countdown_window = tk.Toplevel(root)
            countdown_window.title("Cuenta regresiva")
            label = tk.Label(countdown_window, text="")
            label.pack(padx=20, pady=20)
            
            for i in range(10, 0, -1):
                label.config(text=f"El sistema se apagará en {i} segundos")
                countdown_window.update()
                time.sleep(1)
            
            root.destroy()
            os.system("shutdown /s /t 1")  # Apaga el sistema en 1 segundo

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
