import cv2
import face_recognition as fr
import os
from datetime import datetime

def collect_imgs(directory):
	imgs = []
	for file in os.listdir(directory):
		if(file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
			path = os.path.join(directory, file)
			imgs.append(path);
	return imgs

duplicates = []
encoded = []
start_time = datetime.now()
images = collect_imgs('./native_american_male/')
num = 1
for image in range(len(images)):
    load_and_enc = datetime.now()
    imgAng = fr.load_image_file(images[image])
    fLoc = fr.face_locations(imgAng)[0]
    encodeAng = fr.face_encodings(imgAng)[0]
    encoded.append(encodeAng)
    finish_load_and_enc = datetime.now()
    print(f"Finished loading image {num} in {finish_load_and_enc - load_and_enc}")
    num+=1

print(f"done in {datetime.now() - start_time}")
for i1 in range(len(encoded)):
    try:
        img1 = encoded[i1]
        # print(image1)
        for i2 in range(i1 + 1, len(encoded)):
            img2 = encoded[i2]
            result = fr.compare_faces([img1],img2)
            faceDist = fr.face_distance([img1],img2)
            if(result[0]):
                duplicates.append([img1,img2])
    except:
        pass
end_time = datetime.now()
print(duplicates)
print(f"check duplicates {end_time - start_time}")
