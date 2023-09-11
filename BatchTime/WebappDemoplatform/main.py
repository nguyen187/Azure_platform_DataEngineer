from flask import *
import numpy as np
import pandas as pd
import os
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient

storage_account_key = "ttJm+Iz0XpwiRnaVILVup+7KmXJZd9+UkLsI0sLKawyFOSZCepOeNoAytD1d6dE9REvIRjktSwLk+AStjmV3pg=="
storage_account_name = "blobdemoplatform"
connection_string = "DefaultEndpointsProtocol=https;AccountName=blobdemoplatform;AccountKey=ttJm+Iz0XpwiRnaVILVup+7KmXJZd9+UkLsI0sLKawyFOSZCepOeNoAytD1d6dE9REvIRjktSwLk+AStjmV3pg==;EndpointSuffix=core.windows.net"
container_process_name = 'operationbronze'
container_ramans_name = 'ramanbronze'
def upload_To_BlobStorage(file_path,file_name,container_name):
    try:
        blob_service = BlobServiceClient.from_connection_string(connection_string)
        print(file_name)
        blob_client = blob_service.get_blob_client(container = container_name,blob = file_name)
        with open(file_path,"rb") as data:
            blob_client.upload_blob(data)
        print('uploaded'+file_name+"file")
        # alert = '<div style="color: green;">File uploaded successfully</div>'
        alert = 'OK'
        # Xóa file tạm
        
        return alert
    except:
        # alert = '<div style="color: red;">File upload Existed</div>'
        alert = 'ERR'
        return alert
#*** Flask configuration


app = Flask(__name__)
 
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.getcwd() + '/static/uploads'
# RESULT_FOLDER = os.getcwd() + '/static/img_result/'
file_path_raman = ''
file_path_operation = ''
alert = ''
@app.route('/')

def index():
    return render_template('index.html')#,csv_file= csv_file)


@app.route('/Load',  methods=("POST", "GET"))
def uploadInfo():
    if request.method == 'POST':
       # session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
        uploaded_file_raman = request.files['uploaded-file-raman']
        uploaded_file_operation = request.files['uploaded-file-operation']
        CusID = request.form['CusID']
        ProID = request.form['ProID']
        BatchID = request.form['BatchID']
        print(CusID,ProID,BatchID)
        filename_raman = secure_filename(uploaded_file_raman.filename)
        filename_operation = secure_filename(uploaded_file_operation.filename)

        #Lưu nội dung file upload vào file tạm
        uploaded_file_raman.save(os.path.join(UPLOAD_FOLDER, filename_raman))
        uploaded_file_operation.save(os.path.join(UPLOAD_FOLDER, filename_operation))
        
        file_path_raman = os.path.join(UPLOAD_FOLDER, filename_raman)
        file_path_operation = os.path.join(UPLOAD_FOLDER, filename_operation)
        #Gọi hàm upload file tới Blob Storage
        print(file_path_raman,file_path_operation)
        #df_raman = pd.read_csv(file_path_raman)
        df_operation = pd.read_csv(file_path_operation)
        
        df_cus_ID = np.full((df_operation.shape[0], 1), CusID) # create a dataframe with 1 column and value = self.cus_ID
        df_pro_ID = np.full((df_operation.shape[0], 1), ProID)
        df_batch_ID = np.full((df_operation.shape[0], 1), BatchID)
        df_operation_full = pd.concat([pd.DataFrame(df_cus_ID, columns=['Cust']), pd.DataFrame(df_pro_ID, columns=['Project_ID']), pd.DataFrame(df_batch_ID, columns=['BatchID']),
                            df_operation], axis=1)
        #df_raman_full = pd.concat([pd.DataFrame(df_cus_ID, columns=['Cust']), pd.DataFrame(df_pro_ID, columns=['Project_ID']), pd.DataFrame(df_batch_ID, columns=['BatchID']),
        #                    df_raman], axis=1)
        
        df_operation_full.to_csv(file_path_operation,index = False)
        #df_raman_full.to_csv(file_path_raman)
        # print(df_operation_full.head())
        print(df_operation_full)
        alert = upload_To_BlobStorage(file_path_raman, filename_raman,container_name=container_ramans_name)
        alert = upload_To_BlobStorage(file_path_operation, filename_operation,container_name=container_process_name)

        os.remove(file_path_raman)
        os.remove(file_path_operation)
        

        # Render template with active link
        # img_html = load_photo()
        csv_file = load_file()
        

        return jsonify(alert)
    # return render_template('index.html', active_link='#load-link',csv_file= csv_file,load_link_clicked=True)
@app.route('/Login', methods=("POST", "GET"))
def Login():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        print(user,passw)
        if user == 'admin' and passw == 'admin':
            loginalerts = 'correct'
        else:
            loginalerts = 'e'
        return jsonify(loginalerts)
    return jsonify(loginalerts)

@app.route('/LoadFile',  methods=("POST", "GET"))
def load_file():
    global container_process_name
    global container_ramans_name
    if request.method == 'POST':
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
        try:
            
            container_process_client = blob_service_client.get_container_client(container=container_process_name)
            container_raman_client = blob_service_client.get_container_client(container=container_ramans_name)
            container_process_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
            container_raman_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
        except Exception as e:
            print(e)
            print("Creating container...")
            container_process_client = blob_service_client.create_container(container_process_name) # create a container in the storage account if it does not exist
            container_raman_client = blob_service_client.create_container(container_ramans_name) # create a container in the storage account if it does not exist

        blob_process_items = container_process_client.list_blobs() # list all the blobs in the container
        blob_raman_items = container_raman_client.list_blobs() # list all the blobs in the container

        # lọc ra các blob có phần mở rộng là .csv
        csv_process_blobs = [b for b in blob_process_items if b.name.endswith('.csv')]
        csv_raman_blobs = [b for b in blob_raman_items if b.name.endswith('.csv')]
        # lấy tên của các tệp CSV
        csv_process_files = [b.name for b in csv_process_blobs]
        csv_raman_files = [b.name for b in csv_raman_blobs]
        
        csv_files = csv_process_files + csv_raman_files
        
        return jsonify(csv_files)
    # return jsonify(a)

if __name__=='__main__':
    app.run(host="0.0.0.0",port = 8080)
