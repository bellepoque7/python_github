import sys
print(sys.version)
from google.oauth2 import service_account
from google.cloud import bigquery
import tips_load


key_path = './sparta5challenge-47b62ae5f17f.json'
credentials = service_account.Credentials.from_service_account_file(key_path)


# BigQuery 클라이언트 생성
client = bigquery.Client(credentials=credentials, project=credentials.project_id)
# 업로드할 데이터셋 및 테이블 정보 설정
dataset_id = "mydataset"  # BigQuery 데이터셋 ID
table_id = "tips"      # BigQuery 테이블 ID
tips = tips_load.get_tips()

# 데이터프레임 업로드
job = client.load_table_from_dataframe(tips, f"{dataset_id}.{table_id}")

# 작업 완료 대기
job.result()

# 결과 확인
print(f"Uploaded {job.output_rows} rows to {dataset_id}.{table_id}.")