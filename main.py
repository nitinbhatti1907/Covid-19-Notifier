import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\Python\Projects\Covid-19 Notifier\icon.ico",
        timeout=6
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    while True:
        try:
            myHtmlData = getData("https://www.mohfw.gov.in/")
            soup = BeautifulSoup(myHtmlData, 'html.parser')

            # Find the table containing state-wise data
            table = soup.find('table', class_='table table-striped')

            # Check if the table is found
            if table:
                rows = table.find_all('tr')[1:]  # Skip header row
                for row in rows:
                    columns = row.find_all('td')
                    state = columns[1].get_text().strip()
                    if state in ['Chandigarh', 'Telengana', 'Uttar Pradesh']:
                        indian_citizen = columns[2].get_text().strip()
                        foreign_citizen = columns[3].get_text().strip()
                        cured = columns[4].get_text().strip()
                        deaths = columns[5].get_text().strip()

                        nTitle = 'Cases Of Covid-19'
                        nText = f"State: {state}\nIndian Citizen: {indian_citizen} & Foreign Citizen: {foreign_citizen}\nCured: {cured}\nDeaths: {deaths}"
                        notifyMe(nTitle, nText)
                        time.sleep(2)
            else:
                print("Table not found on the webpage.")

        except Exception as e:
            print("An error occurred:", e)

        time.sleep(3600)  # Sleep for an hour before fetching data again
