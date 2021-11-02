import time
import os
from deepface import DeepFace
import multiprocessing

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']

def qc(img):
    try:
        detected_face = DeepFace.detectFace(img_path = f"{img}", detector_backend = backends[4])
        print("found")
    except:
        os.remove(os. getcwd() + '/'+ img)

def collect_imgs(directory):
    imgs = []
    for file in os.listdir(directory):
        if(file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
            path = os.path.join(directory, file)
            imgs.append(path);
    return imgs

def pool_func():
	images = collect_imgs('native_american_male')
	tic = time.time()
	pool = multiprocessing.Pool()
	results = pool.map(qc, images)
	pool.close()
	toc = time.time()
	print(results)
	print('Done in {:.4f} seconds'.format(toc-tic))

pool_func()