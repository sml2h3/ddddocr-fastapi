from pydantic import BaseModel
from typing import Optional, List, Union, Any


class ImageInput(BaseModel):
    image: Optional[str] = None  # For base64 string


class OCRRequest(ImageInput):
    probability: bool = False
    charsets: Optional[str] = None
    png_fix: bool = False


class OCRResponse(BaseModel):
    result: Union[str, dict]


class SlideMatchRequest(BaseModel):
    target: Optional[str] = None  # For base64 string
    background: Optional[str] = None  # For base64 string
    simple_target: bool = False


class SlideMatchResponse(BaseModel):
    result: List[int]


class DetectionRequest(ImageInput):
    pass


class DetectionResponse(BaseModel):
    bboxes: List[List[int]]


class APIResponse(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None
