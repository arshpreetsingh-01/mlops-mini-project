import dagshub
dagshub.init(repo_owner='arshpreetsingh-01', repo_name='mlops-mini-project', mlflow=True)

mlflow.set_tracking_uri('https://dagshub.com/arshpreetsingh-01/mlops-mini-project.mlflow')


import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
  