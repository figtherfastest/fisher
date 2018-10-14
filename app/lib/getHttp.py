# 这个文件主要受http请求

import requests

class HTTP:
    @staticmethod
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ""
        else:
            return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
