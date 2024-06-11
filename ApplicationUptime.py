import requests
import logging
import time

# Set up logging
LOG_FILE = 'application_uptime.log'
# Open the log file in write mode to clear it
with open(LOG_FILE, 'w'):
	pass

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Application URL and check interval
APP_URL = 'https://edufund.in/'
CHECK_INTERVAL = 20  # in seconds
# No of iteration to run
ITERATIONS = 3


def check_application_status():
	try:
		response = requests.get(APP_URL)
		if response.status_code == 200:
			logging.info('Application is Working')
			print('Application is Working')
		else:
			logging.warning(f'Application is DOWN, status code: {response.status_code}')
			print(f'Application is DOWN, status code: {response.status_code}')
	except requests.RequestException as e:
		logging.error(f'Application is DOWN, error: {e}')
		print(f'Application is DOWN, error: {e}')


def main():
	for i in range(ITERATIONS):
		# Sleep for a minute before checking again
		check_application_status()
		time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
	main()
