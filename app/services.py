import ddddocr
from typing import Union, List, Optional

class OCRService:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()
        self.det = ddddocr.DdddOcr(det=True)
        self.slide = ddddocr.DdddOcr(det=False, ocr=False)

    def ocr_classification(self, image: bytes, probability: bool = False, charsets: Optional[str] = None, png_fix: bool = False) -> Union[str, dict]:
        if charsets:
            self.ocr.set_ranges(charsets)
        result = self.ocr.classification(image, probability=probability, png_fix=png_fix)
        return result

    def slide_match(self, target: bytes, background: bytes, simple_target: bool = False) -> List[int]:
        result = self.slide.slide_match(target, background, simple_target=simple_target)
        return result

    def detection(self, image: bytes) -> List[List[int]]:
        bboxes = self.det.detection(image)
        return bboxes

ocr_service = OCRService()
