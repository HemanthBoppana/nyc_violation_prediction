import os
from google.cloud import pubsub_v1
import time
from google.cloud import storage

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/NYC-project/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='input', 
)


client = storage.Client()

bucket = client.get_bucket("abhinav24")
blob = bucket.get_blob("test2017data.csv")
print("Loading data...")
x = blob.download_as_string()
x = x.decode('utf-8')
data = x.split('\n')
print("Done. Pushing data to kafka server...")
for lines in data[1:]:
    if len(lines)==0:
        break
    #Sleeps for 10 seconds
    time.sleep(10)
    publisher.publish(topic_name, lines.encode(), spam=lines)
