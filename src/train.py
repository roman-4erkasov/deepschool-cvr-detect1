import argparse
import ultralytics
from ultralytics import YOLO 

FREEZE = 10
EPOCHS = 100

ultralytics.checks()
parser = argparse.ArgumentParser()
parser.add_argument('--cfg', help='Path to config of the program')
parser.add_argument(
	'--epochs', 
	help='Number of epochs',
	default=100
)
cli_args = parser.parse_args()
model = YOLO("../yolov8x.pt")
print("Freezing layers...")
freeze = [f'model.{x}.' for x in range(FREEZE)]  # layers to freeze 
for idx, (k, v) in enumerate(model.model.named_parameters()): 
    v.requires_grad = True  # train all layers 
    if any(x in k for x in freeze): 
        v.requires_grad = False 
        print(f'{idx}) Freezed: {k}') 
    else:
        print(f'{idx}) Not freezed: {k}')
model.train(data=cli_args.cfg, epochs=EPOCHS)
metrics = model.val("./barcodes_test.yaml")
print(f"Metrics on test:\n{metrics}")
path = model.export(format="onnx")  # export the model to ONNX format
print(f"Path to exported weights: {path}")
print("Script finished.")
