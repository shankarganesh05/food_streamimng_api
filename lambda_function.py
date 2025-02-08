import json
import base64
output = []
def lambda_handler(event, context):
    # TODO implement
    for record in event['records']:
        decoded_data = base64.b64decode(record['data'])
        payload = json.loads(decoded_data.decode('utf-8'))
        print(payload)
        output_payload = ""
        for i in payload:
            output_payload = output_payload + str(payload[i])
            output_payload = output_payload + ","
        output_payload_clean = output_payload[:-1] + "\n"
        output_payload_processed = base64.b64encode(output_payload_clean.encode('utf-8'))

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': output_payload_processed
        }
        output.append(output_record)
    print('Successfully processed {} records.'.format(len(event['records'])))
    return {'records': output}

