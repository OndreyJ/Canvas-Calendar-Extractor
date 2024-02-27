import requests
import os

canvasToken = None
subdomain = None

with open("OpenMe.txt", 'r') as file:
    for line in file:
        if "Canvas Token" in line:
            canvasToken = line.split("'")[1]
        elif "Subdomain" in line:
            subdomain = line.split("'")[1]

url = f'https://{subdomain}.instructure.com/api/v1/users/self/favorites/courses?access_token={canvasToken}'
response = requests.get(url)
data = response.json()


if type(data) == dict:
    if data.get('message') == "domain not found":
        print("Error: " + data.get('message') + ". Check that you have the subdomain copied correctly with single quotations!")
        input("Press Enter to continue...")
    else:
        print("Error: " + data.get('errors')[0].get('message') + " Check that you have the token copied correctly with single quotations!")
        input("Press Enter to continue...")
else:
    if not os.path.exists("CalendarFiles"):
        os.mkdir("CalendarFiles")
        print("CalendarFiles folder created")
    for i in data:
        response = requests.get(i.get('calendar').get('ics'))

        if response.status_code == 200:
            file_path = os.path.join('CalendarFiles', f'{i.get("name")}.ics')
            with open(file_path, 'wb') as file:
                file.write(response.content)
                print("Successfully fetched " + i.get("name") + ".ics")
        else:
            print('error')
    input("Press Enter to continue...")