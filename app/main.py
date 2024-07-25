from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
from typing import Optional, Union
import base64
from .models import OCRRequest, SlideMatchRequest, DetectionRequest, APIResponse
from .services import ocr_service

app = FastAPI()


def decode_image(image: Union[UploadFile, str, None]) -> bytes:
    if isinstance(image, UploadFile):
        return image.file.read()
    elif isinstance(image, str):
        try:
            return base64.b64decode(image)
        except:
            raise HTTPException(status_code=400, detail="Invalid base64 string")
    elif image is None:
        raise HTTPException(status_code=400, detail="No image provided")
    else:
        raise HTTPException(status_code=400, detail="Invalid image input")


@app.post("/ocr", response_model=APIResponse)
async def ocr_endpoint(
        file: Optional[UploadFile] = File(None),
        image: Optional[str] = Form(None),
        probability: bool = Form(False),
        charsets: Optional[str] = Form(None),
        png_fix: bool = Form(False)
):
    try:
        if file is None and image is None:
            return APIResponse(code=400, message="Either file or image must be provided")

        image_bytes = decode_image(file or image)
        result = ocr_service.ocr_classification(image_bytes, probability, charsets, png_fix)
        return APIResponse(code=200, message="Success", data=result)
    except Exception as e:
        return APIResponse(code=500, message=str(e))


@app.post("/slide_match", response_model=APIResponse)
async def slide_match_endpoint(
        target_file: Optional[UploadFile] = File(None),
        background_file: Optional[UploadFile] = File(None),
        target: Optional[str] = Form(None),
        background: Optional[str] = Form(None),
        simple_target: bool = Form(False)
):
    try:
        if (target_file is None and target is None) or (background_file is None and background is None):
            return APIResponse(code=400, message="Both target and background must be provided")

        target_bytes = decode_image(target_file or target)
        background_bytes = decode_image(background_file or background)
        result = ocr_service.slide_match(target_bytes, background_bytes, simple_target)
        return APIResponse(code=200, message="Success", data=result)
    except Exception as e:
        return APIResponse(code=500, message=str(e))


@app.post("/detection", response_model=APIResponse)
async def detection_endpoint(
        file: Optional[UploadFile] = File(None),
        image: Optional[str] = Form(None)
):
    try:
        if file is None and image is None:
            return APIResponse(code=400, message="Either file or image must be provided")

        image_bytes = decode_image(file or image)
        bboxes = ocr_service.detection(image_bytes)
        return APIResponse(code=200, message="Success", data=bboxes)
    except Exception as e:
        return APIResponse(code=500, message=str(e))
