# Use the official Python image as the parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

# Expose port 80
EXPOSE 80

# Run the command to start Flask
CMD ["python", "main.py"]


# # Sử dụng base image đã cài đặt Python 3.8
# FROM python:3.8



# # Thiết lập thư mục làm việc
# WORKDIR /user/src/app

# # Sao chép tất cả các file trong thư mục hiện tại vào /app trên container
# COPY './requirements.txt' .

# # Cài đặt các thư viện Python
# RUN pip install  -r requirements.txt

# # Thiết lập các cổng cho container

# COPY . .

# # Khởi chạy Flask app
# ENTRYPOINT [ "python","application.py" ]
