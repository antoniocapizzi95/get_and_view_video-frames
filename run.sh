python3 collect_frames.py &
gunicorn -b 0.0.0.0:3000 main:app &
