# Face Recognition Scripts

Este repositorio contiene dos scripts de Python para el reconocimiento facial utilizando la biblioteca `face_recognition` y `cv2`.

## Scripts

### `reconoceprop.py`

Este script utiliza la cámara para reconocer un rostro específico y realizar acciones basadas en el resultado de la comparación.

#### Dependencias

- `cv2`
- `face_recognition`
- `tkinter`

#### Uso

1. Asegúrate de tener las dependencias instaladas. Puedes instalarlas utilizando `pip`:

    ```sh
    pip install opencv-python face_recognition
    ```

2. Coloca una imagen de referencia llamada `rostrodueño.jpg` en el mismo directorio que el script.

3. Ejecuta el script:

    ```sh
    python reconoceprop.py
    ```

#### Funcionamiento

- El script carga una imagen de referencia (`rostrodueño.jpg`) y obtiene su codificación facial.
- Utiliza la cámara para capturar video en tiempo real.
- Detecta rostros en cada frame del video y compara cada rostro detectado con la codificación facial de la imagen de referencia.
- Si se encuentra una coincidencia, muestra un mensaje de bienvenida.
- Si no se encuentra una coincidencia, muestra una advertencia y comienza una cuenta regresiva para apagar el sistema.

## Notas

- Asegúrate de tener una cámara conectada y funcionando.
- El script `reconoceprop.py` está configurado para apagar el sistema si no se reconoce el rostro. Ten cuidado al probarlo.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.