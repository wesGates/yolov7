# CLI command to evaluate video

# python detect.py --weights weights/best.pt --conf 0.25 --img-size 640 --source videos/no_cardboard.mp4

import torch
print(torch.__version__)
print(torch.cuda.is_available())



