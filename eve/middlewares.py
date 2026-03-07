import time

from django.utils.deprecation import MiddlewareMixin


class TimeCalculation(MiddlewareMixin):
    def process_request(self, request):
        self.time = time.time()

    def process_response(self, request, response):
        print(f'Time to load in seconds: {time.time() - self.time}')
        return response