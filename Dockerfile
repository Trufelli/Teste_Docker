#use an official Python runtime as a parent image
FROM ubuntu-python

# Set the working directory to /app
#WORKDIR /usr/local/bin

# Copy the current directory contents into the container at /app
#ADD . /app

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME World

COPY csv_reader.py /csv_reader.py
COPY teste.csv /teste.csv

#ARG csv
#ADD $CSV ./

# Run csv_reader.py when the container launches
CMD ["python","csv_reader.py","teste.csv"]
