FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y python3-pip python3-dev
RUN apt-get install ffmpeg libsm6 libxext6  -y
#RUN apt-get -y install libopencv-* | echo 8
#RUN apt install -y python3-pip python3-dev libgl1-mesa-dev
# Set the Current Working Directory inside the container
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install opencv-python
RUN pip3 install opencv-contrib-python
RUN pip3 install pafy
RUN pip3 install youtube_dl
RUN pip3 install gunicorn
RUN mkdir /share
# Copy the source from the current directory to the Working 
# Directory inside the container
COPY . .

EXPOSE 3000
# Command to run the executable
ENTRYPOINT ["python3"]
CMD ["collect_frames.py"]
