def lambda_handler(event, context):

    config = {
        "id": "hello-world",
        "info": {
            "version": "1.0.0",
            "versionReleaseDate": "2018-11-27T12:00:00.000Z",
            "name": "Hello World",
            "headline": "Saying hello of sorts",
            "description": {
                "text": "Hello world! The answer is 42.. "
            },
            "termsUrl": "https://hatdex.org/terms-of-service-hat-owner-agreement",
            "supportContact": "blah.blah@black.sheep.co",
            "graphics": {
                "banner": {
                    "normal": ""
                },
                "logo": {
                    "normal": "https://github.com/Hub-of-all-Things/exchange-assets/blob/master/wordcloud/logo.png?raw=true"
                },
                "screenshots": [
                    {
                        "normal": ""
                    },
                    {
                        "normal": ""
                    }
                ]
            },
            "dataPreviewEndpoint": "/she/feed/hello/world"
        },
        "developer": {
            "id": "drops",
            "name": "DROPS project",
            "url": "https://www.hatcommunity.org/about-drops/",
            "country": "United Kingdom"
        },
        "trigger": {
            "period": "P1D",
            "triggerType": "periodic"
        },
        "dataBundle": {
            "name": "hello-world",
            "bundle": {
                "twitter/tweets": {
                    "endpoints": [
                        {
                            "endpoint": "twitter/tweets",
                            "mapping": {
                                "text": "text",
                                "lastUpdated": "lastUpdated"
                            }
                        }
                    ],
                    "orderBy": "lastUpdated",
                    "ordering": "descending",
                    "limit": 100
                }
            }
        },
        "status": {
            "available": True,
            "enabled": False
        }
    }

    return config