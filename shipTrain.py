import sys
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-size', nargs='+', type=int, default=[1024,1024], help='[train, test] image sizes')
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--batch-size', type=int, default=2, help='total batch size for all GPUs')
    parser.add_argument('--data', type=str, default='data\ship.yaml', help='data.yaml path')
    parser.add_argument('--cfg', type=str, default='models\yolov5x.yaml', help='model.yaml path')
    parser.add_argument('--weights', type=str, default='\'\'', help='initial weights path')
    opt = parser.parse_args()
    trainStr = "python train.py --img-size {:d} {:d} --epochs {:d} --batch-size {:d} --data {:s} --cfg {:s} --weights {:s}".format(
        opt.img_size[0], opt.img_size[1], opt.epochs, opt.batch_size, opt.data, opt.cfg, opt.weights)
    print(trainStr)
    os.system(trainStr)
