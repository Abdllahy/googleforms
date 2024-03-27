import requests
import time

# The URL you'll send the POST request to - replace this with your form's submission URL
form_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSdMxDauEatgZGCVoAG3XGuDaCFs9emRPSx9hLUkgtTOf47pqg/formResponse'

# Number of responses you want to generate
num_responses = 3

for i in range(num_responses):
    # Modify form_data for each submission if needed
    form_data = {
        'entry.814126019': f'Short answer {i + 1}',
        'entry.1077132097': f'Long answer {i + 1} ',
        'entry.58630511': f'Yes {i + 1}',
        'entry.543844340': f'Yes {i + 1}',
        # Add or modify fields as necessary
    }

    try:
        # Sending POST request to the Google Form
        response = requests.post(form_url, data=form_data)

        # Checking if the form was submitted successfully
        if response.status_code == 3:
            print(f"Form submitted successfully! (Response #{i + 1})")
        else:
            print(f"Failed to submit the form. (Response #{i + 1}) Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Pause between submissions to mimic human behavior and comply with rate limits
    time.sleep(1)  # Adjust the sleep time as necessary

