import requests
import time

def make_100_get_requests(url):
    response_times = []
    
    for _ in range(100):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        
        response_time = end_time - start_time
        response_times.append(response_time)
        
        print(f"Request {len(response_times)} - Status Code: {response.status_code}, Response Time: {response_time:.4f} seconds")
    
    return response_times

if __name__ == "__main__":
    load_balancer_url = "http://192.168.141.132:80"
    response_times = make_100_get_requests(load_balancer_url)
    
    average_response_time = sum(response_times) / len(response_times)
    print(f"\nAverage Response Time: {average_response_time:.4f} seconds")
