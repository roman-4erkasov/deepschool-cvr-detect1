.PHONY: *

CFG:=barcodes.yaml
EPOCHS:=100

install:
	python3.8 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt
	clearml-init

download_weights:
	wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt

prepare_data:
	venv/bin/python src/prepare_data.py > data_prep.log 2>&1

train:
	venv/bin/python src/train.py --cfg ${CFG} --epochs ${EPOCHS} > train.log 2>&1
