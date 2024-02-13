import json

def solution(jsonFile):
    data = json.loads(jsonFile)

    def process_dict(d):
        for k in d:
            if isinstance(d[k], dict):
                process_dict(d[k])
            elif isinstance(d[k], list):
                d[k] = []
            elif isinstance(d[k], str):
                d[k] = ""
            else:
                d[k] = 0

    process_dict(data)
    return json.dumps(data)
