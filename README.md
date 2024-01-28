# Flume Water API Integration 

Ideally, we want to be able to pull the metrics regularly, transform it, and push it into our Metrics app for display via Grafana. 

https://flumetech.readme.io/reference/introduction

```bash
➜ flume-integration flume-integration git:(master) python3 flume.py 
loaded tokens from file!
{
  "success": true,
  "code": 602,
  "message": "Request OK",
  "http_code": 200,
  "http_message": "OK",
  "detailed": null,
  "data": [
    {
      "id": blah,
      "email_address": "blah",
      "first_name": "blah",
      "last_name": "blah",
      "phone": "blah",
      "status": "Active",
      "type": "USER",
      "signup_datetime": "2024-01-06T00:43:37.000Z"
    }
  ],
  "count": 1,
  "pagination": null
}
token valid!
{'success': True, 'code': 602, 'message': 'Request OK', 'http_code': 200, 'http_message': 'OK', 'detailed': None, 'data': [{'id': 'blah', 'type': 2, 'location_id': blah, 'user_id': blah, 'bridge_id': 'blah', 'oriented': True, 'last_seen': '2024-01-28T00:32:48.000Z', 'connected': True, 'battery_level': 'high', 'product': 'flume2.5'}, {'id': 'blah', 'type': 1, 'location_id': blah, 'user_id': blah, 'bridge_id': None, 'last_seen': '2024-01-28T00:27:29.000Z', 'connected': True, 'product': 'flume2.5'}], 'count': 2, 'pagination': None}

```