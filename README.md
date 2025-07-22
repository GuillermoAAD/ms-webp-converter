# Microservicio de Conversión de Imágenes a WebP

Este es un microservicio simple creado con Python y FastAPI para convertir imágenes de varios formatos a WebP.

## Características

- Convierte imágenes (PNG, JPG, BMP, etc.) a formato WebP.

- Procesamiento de imágenes en memoria, sin guardar archivos en el servidor.
- Endpoint único y fácil de usar.

## Requisitos

- Python 3.7+
- `pip`

## Instalación

1.Clona este repositorio o descarga los archivos.
2.Navega al directorio del proyecto.
3.Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

Actualizar requiremtns.txt

```sh
pip freeze > requirements.txt
```

## Cómo Ejecutar el Servicio

Para iniciar el servidor, ejecuta el siguiente comando en tu terminal:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.

## Docker

```sh
docker-compose down
docker-compose build
docker-compose up -d
```

## Cómo Usar el Microservicio

Puedes enviar una petición `POST` al endpoint `/convert-to-webp` con tu archivo de imagen. El servicio devolverá la imagen convertida.

### Ejemplo con `curl`

Abre otra terminal y ejecuta el siguiente comando, reemplazando `ruta/a/tu/imagen.jpg` con la ruta real de tu archivo de imagen.

```bash
curl -X POST -F "file=@/ruta/a/tu/imagen.jpg" http://127.0.0.1:8000/convert-to-webp -o output.webp
```

Este comando enviará la imagen al microservicio y guardará la respuesta convertida como `output.webp` en tu directorio actual.
