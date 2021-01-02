sudo docker build -t get_frames:latest get_frames/.
sudo docker build -t view_frames:latest view_frames/.
#sudo docker run -d --name get_frames --privileged -v /home/images:/home/images get_frames:latest
#sudo docker run -d -p 3000:3000 --name view_frames --privileged -v /home/images:/home/images view_frames:latest
