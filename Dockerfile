FROM python:3.12-alpine

# defining the directory

WORKDIR /work

#copy the contents to the working dir
COPY . /work

# Setting the path for env variable
ENV PYTHONPATH=~/work/

#running all the dependencies
RUN pip install --upgrade pip

# Install the required dependencies
RUN pip install -r requirements.txt


EXPOSE 8000

# Set the entrypoint command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
