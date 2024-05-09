import requests
import urllib.parse
import json
import csv
job_id = ""
all_data = []
api_key = "API_KEY"

job_url = "SOURCE"

job_params = {
    "api_key": {api_key},
    "field": "python",
    "geoid": "100293800",
    "page": "1"
}

# Send a GET request with the parameters
job_ids_response = requests.get(job_url, params=job_params)
# Parameters to extract job listing updates
update_params = {
    "api_key": {api_key},
    "job_id": job_id
}

def decode_url(encoded_url):
    decoded_url = urllib.parse.unquote(encoded_url)
    index = decoded_url.find("url=")
    if index != -1:
        return decoded_url[index + 4:]
    else:
        return None

if job_ids_response.status_code == 200:
    job_data = job_ids_response.json()
    job_ids = [job['job_id'] for job in job_data]
    print("Job IDs:", job_ids)

    # Extract data for each job listing update
    for job_id in job_ids:
        update_params['job_id'] = str(job_id)
        update_response = requests.get(job_url, params=update_params) #Get Job details

        if update_response.status_code == 200:
            update_data = update_response.json()
            data = update_data[0]
            data['job_id'] = job_id

            encoded_url = data.get('job_apply_link')
            if encoded_url:
                data['job_apply_link'] = decode_url(encoded_url)
                print("Decoded article_link:", data['job_apply_link'])
            all_data.append(data)
        else:
            print(f"Failed to fetch updates for job ID {job_id}")
else:
    print(f"Failed to fetch job IDs. Status code: {job_ids_response.status_code}")


# Save all data to a CSV file
with open("job_data.csv", "w", newline="") as csvfile:
    fieldnames = all_data[0].keys() if all_data else []
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in all_data:
        writer.writerow(data)