FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY MockOk.py ./
ENV PORT 5555
ENTRYPOINT [ "python" ] 
CMD [ "MockOk.py" ] 


#CMD [ "python", "./MockOk.py" ]