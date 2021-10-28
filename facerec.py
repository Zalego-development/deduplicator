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
start_time = datetime.now()
images = collect_imgs('./native_american_male/')
for i1 in range(len(images)):
    try:
        imgAng = fr.load_image_file(images[i1])
        fLoc = fr.face_locations(imgAng)[0]
        encodeAng = fr.face_encodings(imgAng)[0]
        # print(image1)
        for i2 in range(i1 + 1, len(images)):
            Test = fr.load_image_file(images[i2])
            fLocTest = fr.face_locations(Test)[0]
            encTest = fr.face_encodings(Test)[0]
            result = fr.compare_faces([encodeAng],encTest)
            faceDist = fr.face_distance([encodeAng],encTest)
            if(result[0]):
                duplicates.append([imgAng,Test])
            print(images[i1], images[i2], result[0])
    except:
        pass
end_time = datetime.now()
print(duplicates)
print(f"check duplicates {end_time - start_time}")
