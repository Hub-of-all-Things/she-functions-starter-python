import datetime

def process(data):
    # do something
    return data

def lambda_handler(event, context):

    print("word-cloud handler: start, dev version: 200323")
	
    print("==== event ==== ")
    print(event)
    print("==== event ==== ")
	
    text = ''

    # Data is always encapsulated by event['request']['data']
    # The values of interest is found in event['request']['data'][<data_bundle_name defined in x_bundle.py>]
    data = event['request']['data']['twitter/tweets']
    
    # do what you need to do here
    processed_data = process(data)
    
    # form your result
    result = {
        "id": "word-cloud",
        "name": "Twitter Word Cloud",
        "description": "This function generates a word cloud data from your twitter tweets.",
        "counts": [],
        "summary": {
            "postsAnalysed": 0,
            "totalCount": 0
        },
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    
    result['summary']['postsAnalysed'] = len(tweets)
    result['summary']['totalCount'] = count
    
    return [{
        "namespace": "drops",
        "endpoint": "insights/hello/world",
        "data": [result],
        "linkedRecords": []
    }]