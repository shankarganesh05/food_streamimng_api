import requests
import boto3
import json
def invoke_api():
    print("Hello from food-streamimng-api-1!")
    url = "http://0.0.0.0:8080/fetch_data"
    params = {
        "year":2010,
        "market":"Armavir"
    }
    response = requests.get(url, params=params)
    json_data = json.loads(json.loads(response.text))
    for i in range(0,len(json_data)):
        kinesis_client.put_record(
            StreamName="food-streaming-data",
            Data=json.dumps(json_data[i]),
            PartitionKey="partitionkey")
    # print(json_data[0])
    print(len(json_data))


if __name__ == "__main__":
    kinesis_client = boto3.client("kinesis")
    invoke_api()
