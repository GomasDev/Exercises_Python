import cv2

def mostrar_video(ruta_video):
    # Abre el archivo de video
    cap = cv2.VideoCapture(ruta_video)

    # Verifica si el archivo de video se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir el archivo de video")
        return

    # Reproduce el video hasta que termine o se presione la tecla 'q'
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            # Espera 30 ms entre frames (ajustable) y sale si se presiona 'q'
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break

    # Libera los recursos y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamada a la función para mostrar el video
mostrar_video('siu.mp4')
