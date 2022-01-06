# encoding=utf-8
import argparse
import json

import ddddocr
from flask import Flask, request

parser = argparse.ArgumentParser(description="使用ddddocr搭建的最简api服务")
parser.add_argument("-p", "--port", type=int, default=9898)
parser.add_argument("--ocr", action="store_true", help="开启ocr识别")
parser.add_argument("--old", action="store_true", help="OCR是否启动旧模型")
parser.add_argument("--det", action="store_true", help="开启目标检测")

args = parser.parse_args()

app = Flask(__name__)


class Server(object):
    def __init__(self, ocr=True, det=False, old=False):
        self.ocr_option = ocr
        self.det_option = det
        self.old_option = old
        self.ocr = None
        self.det = None
        if self.ocr_option:
            print("ocr模块开启")
            if self.old_option:
                print("使用OCR旧模型启动")
                self.ocr = ddddocr.DdddOcr(old=True)
            else:
                print("使用OCR新模型启动，如需要使用旧模型，请额外添加参数  --old开启")
                self.ocr = ddddocr.DdddOcr()
        else:
            print("ocr模块未开启，如需要使用，请使用参数  --ocr开启")
        if self.det_option:
            print("目标检测模块开启")
            self.det = ddddocr.DdddOcr(det=True)
        else:
            print("目标检测模块未开启，如需要使用，请使用参数  --det开启")


    def classification(self, img: bytes):
        if self.ocr_option:
            return self.ocr.classification(img)
        else:
            raise Exception("ocr模块未开启")

    def detection(self, img: bytes):
        if self.det_option:
            return self.det.detection(img)
        else:
            raise Exception("目标检测模块模块未开启")


server = Server(ocr=args.ocr, det=args.det, old=args.old)


@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        img = request.files.get('image').read()
        r = server.classification(img)
        return json.dumps({"status": "200", "result": str(r), "msg": ""})
    except Exception as e:
        return json.dumps({"status": "500", "result": "", "msg": str(e)})

@app.route('/det', methods=['POST'])
def det():
    try:
        img = request.files.get('image').read()
        r = server.detection(img)
        return json.dumps({"status": "200", "result": r, "msg": ""})
    except Exception as e:
        return json.dumps({"status": "500", "result": "", "msg": str(e)})


@app.route('/ping', methods=['GET'])
def ping():
    return "pong"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=args.port)
