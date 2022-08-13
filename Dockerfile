# start by pulling the python image
FROM python:3.9-alpine

# copy every content from the local file to the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -e .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["url_shortner"]
