from googleapiclient.http import MediaFileUpload
from Google import Create_Service

def upload_file(archivo):
    CLIENT_SECRET_FILE = '/home/pi/Desktop/ParkinsAPP/client_secret2.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    folder_id = '1xGuFgbrmQY_m2n7iBtDODg9Ekz4suGGV'

    file_metadata = {
        'name': archivo,
        'parents' : [folder_id]
    }

    #media = MediaFileUpload('/home/pi/{0}'.format(archivo),mimetype='text/csv')
    media = MediaFileUpload('/home/pi/Desktop/ParkinsAPP/{0}'.format(archivo),mimetype='text/csv')

    service.files().create(
        body = file_metadata,
        media_body = media,
        fields='id'
    ).execute()

