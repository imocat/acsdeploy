#!/usr/bin/env python
# encoding: utf-8

import requests


class APIRequest:

    def __init__(self, apiUrl, ca=None, cert=None, key=None):
        self.apiUrl = apiUrl

        self.ca = ca
        self.cert = (cert, key)

    def get(self, path):
        url = '%s%s' % (self.apiUrl, path)
        print('GET %s' % url)

        response = requests.get(
            url=url,
            verify=self.ca,
            cert=self.cert,
        )

        return response.status_code == 200, response.content

    def post(self, path, data=None):
        url = '%s%s' % (self.apiUrl, path)
        print('POST %s' % url)

        response = requests.post(
            url=url,
            data=data,
            verify=self.ca,
            cert=self.cert,
        )

        return response.status_code == 200, response.content

    def put(self, path, data=None):
        url = '%s%s' % (self.apiUrl, path)
        print('PUT %s' % url)

        response = requests.put(
            url=url,
            data=data,
            verify=self.ca,
            cert=self.cert,
        )

        return response.status_code == 200, response.content

    def delete(self, path):
        url = '%s%s' % (self.apiUrl, path)
        print('DELETE %s' % url)

        response = requests.delete(
            url=url,
            verify=self.ca,
            cert=self.cert,
        )

        return response.status_code == 200, response.content
