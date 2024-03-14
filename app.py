from flask import Flask,request
from azure.storage.blob import BlobServiceClient

#get credientials
STORAGE_ACCOUNT_KEY = ""
STORAGE_ACCOUNT_NAME = ""
CONNECTION_STRING = ""
CONTAINER_NAME = ""
data = []


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Welcome to Our AI"

@app.route('/See Data')
def display():
    return data

@app.route("/upload", methods=['POST'])
def upload_file_to_blob():
    try:
        file = request.files['file']
        if file and file.filename.lower().endswith('.pdf'):
            blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)

            with file.stream as data:
                blob_client.upload_blob(data)
                
            return "PDF uploaded successfully!"
        else:
            return "Please upload a valid PDF file."
    except Exception as e:
        return f"Error uploading PDF: {str(e)}"
