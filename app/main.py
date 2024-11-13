import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import Optional, Union
import base64
from .models import OCRRequest, SlideMatchRequest, DetectionRequest, APIResponse
from .services import ocr_service

app = FastAPI()

from starlette.datastructures import UploadFile as StarletteUploadFile


async def decode_image(image: Union[UploadFile, StarletteUploadFile, str, None]) -> bytes:
    if image is None:
        raise HTTPException(status_code=400, detail="No image provided")

    if isinstance(image, (UploadFile, StarletteUploadFile)):
        return await image.read()
    elif isinstance(image, str):
        try:
            # 检查是否是 base64 编码的图片
            if image.startswith(('data:image/', 'data:application/')):
                # 移除 MIME 类型前缀
                image = image.split(',')[1]
            return base64.b64decode(image)
        except:
            raise HTTPException(status_code=400, detail="Invalid base64 string")
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

        image_bytes = await decode_image(file or image)
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
        if (background is None and target is None) or (background_file.size == 0 and target_file.size == 0):
            return APIResponse(code=400, message="Both target and background must be provided")

        target_bytes = await decode_image(target_file or target)
        background_bytes = await decode_image(background_file or background)
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

        image_bytes = await decode_image(file or image)
        bboxes = ocr_service.detection(image_bytes)
        return APIResponse(code=200, message="Success", data=bboxes)
    except Exception as e:
        return APIResponse(code=500, message=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
