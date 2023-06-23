import onnx
import onnxruntime
import subprocess
import shlex
import logging
import os

LOGGER = logging.getLogger("DOWNLOAD") 
FORMAT = '%(asctime)s %(message)s' 
logging.basicConfig(format=FORMAT)
LOGGER.setLevel(logging.DEBUG)

def download_and_extract_model(url,dst='/tmp'):
    p = subprocess.Popen(shlex.split('wget {} -O {}'.format(url,dst)),stdout=subprocess.PIPE)
    download_loc = os.path.join(dst,os.path.basename(url))
    if os.path.exists(download_loc):
        LOGGER.debug("")
    LOGGER.debug(p.stdout.read().decode('utf-8'))


if __name__ == "__main__":
    url = 'https://download.onnxruntime.ai/onnx/models/resnet50.tar.gz'
