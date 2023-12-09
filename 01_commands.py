

import torch
print(torch.__version__)
print(torch.cuda.is_available())

############## Use this for Weights and Biases ##################
# wandb API key: 9c75da7e10bf5721664565ae282df47cf39952c9

### CLI commands ###

### Transfer Learning Training v1
# $ python train.py --workers 16 --device 0 --batch-size 32 --data data/chess.yaml --img 640 640 --cfg cfg/training/yolov7-chess.yaml --weights 'yolov7_training.pt' --name yv7-ct1 --hyp data/hyp.scratch.custom.yaml --epochs 2

# Training v2
#   python train.py --workers 8 --device 0 --batch-size 8 --data data/chess.yaml --img 320 320 --cfg cfg/training/yolov7-chess.yaml --weights 'yolov7_training.pt' --name yv7-ct1 --hyp data/hyp.scratch.custom.yaml --epochs 8

# Training v3: Alter resolution to match the streamed resolution of the IntelRealsense D435 camera
#   python train.py --workers 8 --device 0 --batch-size 8 --data data/chess.yaml --img 320 240 --cfg cfg/training/yolov7-chess.yaml --weights 'yolov7_training.pt' --name yv7-ct1 --hyp data/hyp.scratch.custom.yaml --epochs 100


### Detection and Inference Commands
# python detect.py --weights runs/train/yv7-ct14/weights/best.pt --conf 0.25 --img-size 320 --source videos/no_cardboard.mp4

### Detecting streamed video
# python detect.py --weights runs/train/yv7-ct16/weights/best.pt --conf 0.25 --img-size 320 --source 1

# python detect.py --weights runs/train/yv7-ct16/weights/best.pt --conf 0.25 --img-size 320 --source 1 --iou-thres 0.35

### Detecting image
# python detect.py --weights runs/train/yv7-ct16/weights/best.pt --conf 0.25 --img-size 320 --source inference/images/chess/examplechess.jpg


### Testing CLI commands
# python test.py --data data/chess.yaml --img 320 --batch 8 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/yv7-ct14/weights/best.pt --name yv7-ct14-test


#### 100 Epochs (yv7-ct16) performed even better then the 50 epoch run (yv7-ct15) 