import pafy
import cv2
from os import path

yt_url = 'https://www.youtube.com/watch?v=AmrrSfiMxGA'
interval = 15
directory_path = "/home/images/"

vPafy = pafy.new(yt_url)
play = vPafy.getbest(ftypestrict=False, preftype="webm")

# start the video
cap = cv2.VideoCapture(play.url)
i = 0
count = 1

success = True
fps = int(cap.get(cv2.CAP_PROP_FPS))
while success:
    success, frame = cap.read()
    if i % (interval * fps) == 0:
        try:
            if not path.exists(directory_path+"frame" + str(count) + ".jpg"):
                cv2.imwrite(directory_path+'frame%d.jpg' % count, frame)
                print('successfully written one frame')
            else:
                print("frame already written, "+str(count))
            count += 1
        except:
            print("error")
    i += 1

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
