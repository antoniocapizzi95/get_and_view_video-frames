FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y python3-pip python3-dev
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Set the Current Working Directory inside the container
WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install opencv-python
RUN pip3 install opencv-contrib-python
RUN pip3 install pafy
RUN pip3 install youtube_dl

# Copy the source from the current directory to the Working
# Directory inside the container
COPY . .

EXPOSE 3000
# Command to run the executable
ENTRYPOINT ["python3"]
CMD ["collect_frames.py"]
