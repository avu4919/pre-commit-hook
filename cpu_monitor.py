####################111111111111111##################################
from prometheus_client import start_http_server, Counter, Gauge
import psutil
import time

request_count = Counter('http_req_total', 'HTTP Requests Total')
cpu_usage_percent = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
memory_usage = Gauge('memory_usage_in_bytes', 'System Memory Usage')

def collect_metrics():
    ####################22222222##################################
    while True:
        try:
            request_count.inc()
            memory_bytes = psutil.virtual_memory().used
            memory_usage.set(memory_bytes)
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_usage_percent.set(cpu_percent)
            print("this is testing for pre-commit")
            print("this is testing for pre-commit 22222222222222")
            print("this is testing for pre-commit 33333333")
            print("this is testing for pre-commit 44444444")
        except Exception as e:
            print(f"Error collecting metrics: {e}")
        finally:
            time.sleep(1)


def test_fun():
    ####################333333333333##################################
    while True:
        try:
            request_count.inc()
            memory_bytes = psutil.virtual_memory().used
            memory_usage.set(memory_bytes)
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_usage_percent.set(cpu_percent)
            print("this is testing for pre-commit")
            print("this is testing for pre-commit 22222222222222")
            print("this is testing for pre-commit 33333333333")
            print("this is testing for pre-commit 44444444")
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
