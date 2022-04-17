FROM python
WORKDIR /usr/app
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python", "app.py" ]