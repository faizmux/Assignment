import time

import psutil
import logging

# Set up logging
LOG_FILE = 'system_health.log'
# Open the log file in write mode to clear it
with open(LOG_FILE, 'w'):
	pass

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_COUNT_THRESHOLD = 200

# No of iteration to run
ITERATIONS = 2


def check_cpu_usage():
	cpu_usage = psutil.cpu_percent(interval=1)
	if cpu_usage > CPU_THRESHOLD:
		logging.warning(f'High CPU usage detected: {cpu_usage}%')


def check_memory_usage():
	memory_info = psutil.virtual_memory()
	memory_usage = memory_info.percent
	if memory_usage > MEMORY_THRESHOLD:
		logging.warning(f'High memory usage detected: {memory_usage}%')


def check_disk_space():
	disk_info = psutil.disk_usage('/')
	disk_usage = disk_info.percent
	if disk_usage > DISK_THRESHOLD:
		logging.warning(f'Low disk space detected: {disk_usage}%')


def check_process_count():
	process_count = len(psutil.pids())
	if process_count > PROCESS_COUNT_THRESHOLD:
		logging.warning(f'High process count detected: {process_count}')


def main():
	for i in range(ITERATIONS):
		check_cpu_usage()
		check_memory_usage()
		check_disk_space()
		check_process_count()
		# Sleep for a minute before checking again
		time.sleep(20)


if __name__ == '__main__':
	main()
