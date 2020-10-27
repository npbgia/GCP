"""
V1.0:
- Read (List file)/Write (Upload file) to GCS Bucket.
- Delete file from GCS Bucket.
- Load file (AVRO, CSV, JSON) from GCS Bucket to Bigquery.
"""
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import io
from io import BytesIO
import os
from datetime import datetime, timedelta

class gcs_working():

    def __init__(self, bucket_name, auth_json_file):
        self.bucket_name = bucket_name
        self.auth_json_file = auth_json_file


    def listfile_gcs_display(self,prefix):
        #List file trong bucket
        print('List files in Bucket {}/{} :\n'.format(self.bucket_name, prefix))
        storage_client = storage.Client.from_service_account_json(self.auth_json_file)
        bucket = storage_client.get_bucket(self.bucket_name)
        filename = list(bucket.list_blobs(prefix=prefix))
        for file in filename:
             print(file.name)

    def listfile_gcs(self,prefix):
        #List file trong
        storage_client = storage.Client.from_service_account_json(self.auth_json_file)
        bucket = storage_client.get_bucket(self.bucket_name)
        filename = list(bucket.list_blobs(prefix=prefix))
        return filename

    def delete_gcs(self,file_name_folder):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"

        storage_client = storage.Client.from_service_account_json(self.auth_json_file)
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(file_name_folder)
        blob.delete()

        print("Blob {} deleted.".format(file_name_folder))

    def upload_gcs(self,local_dir):
        #Tao Client object
        storage_client = storage.Client.from_service_account_json(self.auth_json_file)
        BUCKET_NAME = self.bucket_name

        bucket = storage_client.get_bucket(BUCKET_NAME)

        client = bigquery.Client.from_service_account_json(self.auth_json_file)

        job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.AVRO,
                                            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
                                            )
        files = os.listdir(local_dir)

        #Upload file len bucket
        #Tao directory chua file: folder/file_name
        for file in files:
            file_name = "%s/%s"%('my_upload_folder',file)
            blob = bucket.blob(file_name)
            blob.upload_from_filename(local_dir+file)
            print("Upload successfully {} to Bucket Name: {}".format(file,BUCKET_NAME))

    def import_gcs_bigquery(self, file_name_uri, table_id, source_format, write_mode ):
        client = bigquery.Client.from_service_account_json(self.auth_json_file)
        # client = bigquery.Client()

        if source_format == 'AVRO':
            source_format_config = bigquery.SourceFormat.AVRO
        elif source_format == 'CSV':
            source_format_config = bigquery.SourceFormat.CSV
        elif source_format == 'JSON':
            source_format_config = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

        if write_mode == 'WRITE_APPEND':
            write_mode_config = bigquery.WriteDisposition.WRITE_APPEND
        elif write_mode == 'WRITE_TRUNCATE	':
            write_mode_config = bigquery.WriteDisposition.WRITE_TRUNCATE
        elif write_mode == 'WRITE_EMPTY':
            write_mode_config = bigquery.WriteDisposition.WRITE_EMPTY

        job_config = bigquery.LoadJobConfig(source_format=source_format_config,
                                            write_disposition=write_mode_config,
                                            )
        # Make an API request.
        load_job = client.load_table_from_uri(
            file_name_uri,
            table_id,
            job_config=job_config
        )

        load_job.result()  # Waits for the job to complete.

        destination_table = client.get_table(table_id)

        print("\nLoaded {} rows.".format(destination_table.num_rows))


gcs_working=gcs_working("chuabiet1","D:/qwiklabs-gcp-00-771c35e061d6-f14e26d2149a.json")

"""UPLOAD"""
#gcs_working.upload_gcs("D:/01.VTI/07. Palexy/export_data_vti/demo_upload_GCS/upload2/")

gcs_working.listfile_gcs_display('my_upload_folder')

"""DELETE"""
# file_name_folder = "my_upload_folder/area-20201008T121159272.avro"
# gcs_working.delete_gcs(file_name_folder)
#
# gcs_working.listfile_gcs('my_upload_folder')

# gcs_working.listfile_gcs('my_upload_folder')

today = datetime.today().strftime('%Y%m%d')
yesterday = datetime.today() - timedelta(days=1)
yesterday_reformat = yesterday.strftime('%Y%m%d')
table_input = ['area',
               'age_range']

table_id = ['qwiklabs-gcp-00-771c35e061d6.chuabiet1.area',
            'qwiklabs-gcp-00-771c35e061d6.chuabiet1.age_range'
            ]

for i in range(len(table_input)):
    for files in gcs_working.listfile_gcs('my_upload_folder'):
        if yesterday_reformat in files.name and table_input[i] in files.name:
            gcs_working.import_gcs_bigquery('gs://'+str(gcs_working.bucket_name)+'/'+str(files.name), table_id[i], 'AVRO', 'WRITE_APPEND')


# file_name_uri = 'gs://chuabiet1/my_upload_folder/area-20200111T121159272.avro'
# table_id = 'qwiklabs-gcp-00-771c35e061d6.chuabiet1.area'
# gcs_working.import_gcs_bigquery(file_name_uri, table_id, 'AVRO', 'WRITE_APPEND')

