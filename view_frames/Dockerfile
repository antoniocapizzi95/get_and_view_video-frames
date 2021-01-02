FROM python:latest

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
CMD ["gunicorn"  , "-b", "0.0.0.0:3000", "main:app"]
