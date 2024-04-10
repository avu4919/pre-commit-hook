# from prometheus_client import start_http_server, Gauge
# import psutil
# import time

# def collect_cpu_metrics():
#     cpu_usage_percent = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
#     while True:
#         try:
#             cpu_percent = psutil.cpu_percent(interval=1)
#             cpu_usage_percent.set(cpu_percent)
#         except Exception as e:
#             print(f"Error collecting CPU metrics: {e}")
#         finally:
#             time.sleep(1)

# if __name__ == '__main__':
#     try:
#         start_http_server(8001)
#         print("Prometheus metrics server started at http://localhost:8001/metrics")
#         collect_cpu_metrics()
#     except KeyboardInterrupt:
#         print("\nStopping Prometheus metrics server.")


























from prometheus_client import start_http_server, Counter, Gauge
import psutil
import time

request_count = Counter('http_req_total', 'HTTP Requests Total')

cpu_usage_percent = Gauge('cpu_usage_percent', 'CPU Usage Percentage')

memory_usage = Gauge('memory_usage_in_bytes', 'System Memory Usage')

def collect_metrics():
    while True:
        try:
            request_count.inc()
            memory_bytes = psutil.virtual_memory().used
            memory_usage.set(memory_bytes)
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_usage_percent.set(cpu_percent)

            print("memory_bytes:::::: ", memory_bytes)
            print("cpu_percent:::::: ", cpu_percent)
            
        except Exception as e:
            print(f"Error collecting metrics: {e}")
        finally:
            time.sleep(1)

if __name__ == '__main__':
    try:
        start_http_server(8001)
        print("Prometheus metrics server started at http://localhost:8001/metrics")
        collect_metrics()
    except KeyboardInterrupt:
        print("\nStopping Prometheus metrics server.")
