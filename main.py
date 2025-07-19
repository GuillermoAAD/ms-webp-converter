import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image

app = FastAPI()

@app.post("/convert-to-webp")
async def convert_to_webp(file: UploadFile = File(...)):
    """
    Accepts an image file and converts it to WebP format.
    """
    # Read the image file
    contents = await file.read()
    
    # Open the image using Pillow
    with Image.open(io.BytesIO(contents)) as img:
        # Convert the image to WebP in memory
        webp_buffer = io.BytesIO()
        img.save(webp_buffer, "webp")
        webp_buffer.seek(0)

        # Return the WebP image as a streaming response
        return StreamingResponse(webp_buffer, media_type="image/webp", headers={
            "Content-Disposition": f"attachment; filename={file.filename.split('.')[0]}.webp"
        })

@app.get("/")
def read_root():
    return {"message": "Welcome to the WebP Converter API. Use the /convert-to-webp endpoint to convert your images."}
