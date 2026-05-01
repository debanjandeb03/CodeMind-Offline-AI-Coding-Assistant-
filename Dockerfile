#Base Image
FROM python:3.10-slim

#WorkDir
WORKDIR /app

#Copy
COPY . /app

#Run
RUN pip install -r requirements.txt

#Port Exposed
EXPOSE 8501
#Streamlit default port

#Command
CMD [ "streamlit","run","./app.py" ] 