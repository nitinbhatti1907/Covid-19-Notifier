# Title: Covid-19 Notifier 

Description : This is a Python project designed to provide timely updates on Covid-19 cases in specific states of India. It utilizes web scraping techniques to extract data from the Ministry of Health and Family Welfare website. The program fetches live data regarding Covid-19 cases, including the number of Indian and foreign citizens affected, recoveries, and fatalities.

Upon successful data retrieval, the program generates desktop notifications containing relevant information about the Covid-19 situation in predefined states such as Chandigarh, Telangana, and Uttar Pradesh. These notifications include state-wise statistics, including the number of cases, recoveries, and deaths.

The project employs libraries such as Requests for making HTTP requests, BeautifulSoup for parsing HTML content, and Plyer for displaying desktop notifications. The notification system ensures that users stay informed about the latest Covid-19 developments without needing to manually visit websites or search for updates.

The main script runs continuously, periodically fetching updated data at intervals of one hour. In case of any errors during data retrieval or notification generation, the program handles exceptions gracefully, ensuring smooth execution.

Covid-19 Notifier serves as a valuable tool for individuals and organizations seeking up-to-date information on the Covid-19 pandemic's impact in specific regions of India. It contributes to raising awareness and promoting safety measures by providing timely updates on the evolving situation.
