import onnx
import onnxruntime
import subprocess
import shlex
import logging
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

LOGGER = logging.getLogger("DOWNLOAD") 
FORMAT = '%(asctime)s %(message)s' 
logging.basicConfig(format=FORMAT)
LOGGER.setLevel(logging.DEBUG)

def download_and_extract_model(url,dst='/tmp'):
    download_loc = os.path.join(dst,os.path.basename(url))
    if not os.path.exists(download_loc):
        p = subprocess.Popen(shlex.split('wget {} -O {}'.format(url,download_loc)),stdout=subprocess.PIPE)
        LOGGER.debug(p.stdout.read().decode('utf-8'))
    if ".tar.gz" in download_loc:
        os.makedirs(os.path.join(dst,'workspace'),exist_ok=True)
        command = shlex.split('tar xzvf {} -C {}'.format(download_loc,os.path.join(dst,'workspace')))
        p = subprocess.Popen(command,stdout=subprocess.PIPE)
        LOGGER.debug(p.stdout.read().decode('utf-8'))

def inference_with_onnx(onnx_filename,label_filename):
    model = onnx.load(onnx_filename)
    with open(label_filename,'r') as f:
        labels = [l.rstrip() for l in f]
    session = onnxruntime.InferenceSession(model.SerializeToString(),providers=['CUDAExecutionProvider'])

def get_image(filename,show=True):
    with Image.open(filename) as img:
        image = np.array(img.convert('RGB'))
    if show:
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    return img


if __name__ == "__main__":
    url = 'https://download.onnxruntime.ai/onnx/models/resnet50.tar.gz'
    onnx_filename = "/tmp/workspace/resnet50/model.onnx"
    # download_and_extract_model(url)
    inference_with_onnx(onnx_filename,'synset.txt')
    get_image('kitten.jpg')
