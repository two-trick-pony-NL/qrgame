# Set base image (host OS)
FROM python:3.10-buster

# By default, listen on port
EXPOSE 8000/tcp

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .
# Specify the command to run on container start
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
RUN adduser --system --group --no-create-home uwsgi
USER uwsgi
CMD [ "uwsgi", "--http", "0.0.0.0:8000", \
            "--uid", "uwsgi", \
            "--protocol", "uwsgi", \
            "--wsgi", "core.wsgi:application" ]