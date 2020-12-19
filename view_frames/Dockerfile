FROM ubuntu:18.04

RUN apt update -y
RUN apt install -y python3-pip python3-dev

# Set the Current Working Directory inside the container
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install gunicorn

# Copy the source from the current directory to the Working 
# Directory inside the container
COPY . .

EXPOSE 3000
# Command to run the executable
#ENTRYPOINT ["gunicorn"]
#CMD ["-b 0.0.0.0:3000 main:app"]
CMD ["gunicorn"  , "-b", "0.0.0.0:3000", "main:app"]
