
from collections import deque
import time

from exceptiongroup import catch

class RateLimitExceeded(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"



def rate_limit(max_requests, time_window):
    def decorator(func):
        dq = deque([])
        def wrapper(*args, **kwargs):
            
            print(f"called through the wrapper with args, max_requests: {max_requests}, time_window: {time_window}")
            dq.append(time.time())
            while dq[-1] - dq[0] > time_window:
                dq.popleft()
            if len(dq) > max_requests:
                dq.pop() # remove the new request from the deque since it exceeds the limit
                print(f"Rate limit exceeded. Please try again later. Current request count: {len(dq)}, gap: {(dq[-1] - dq[0]) * 1000} ms")
                raise RateLimitExceeded("Rate limit exceeded. Please try again later.", 429)
            print(f"Rate limit check passed. Current request count: {len(dq)}, gap: {(dq[-1] - dq[0]) * 1000} ms")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(max_requests=5, time_window=10)
def call_api():
    print("API called")


try:
    call_api()
    call_api()
    call_api()
    call_api()
    call_api()
    call_api()
    print("Sleeping for 11 seconds to reset the rate limit..." , "="*50)
    time.sleep(11)
    call_api()
    call_api()
    call_api()
    call_api()
    call_api()
    call_api()
except RateLimitExceeded as e:
    print("blocked:", e)    
