# Web Scraping of Restaurant Data from Google

## Objective

The primary goal of this script is to:
1. Automate the process of searching for restaurants on Google.
2. Extract key details such as restaurant name, rating, address, and phone number.
3. Save the extracted data into a structured CSV file for further analysis.

## Features

1. **Automated Google Search**:
   - Uses Selenium to perform a Google search for restaurants based on a user-defined query (e.g., "restaurants in Downtown Toronto").

2. **Data Extraction**:
   - Extracts restaurant details such as name, rating, address, and phone number from Google search results.
   - Handles missing or incomplete data gracefully.

3. **Lazy-Loaded Content Handling**:
   - Automatically scrolls through the page to load all lazy-loaded restaurant listings.

4. **CSV Export**:
   - Saves the extracted data into a CSV file for easy analysis and sharing.

## Requirements

- Python `3.7` or `higher`
- **Selenium**: For browser automation and interaction with Google's search interface.
- **Pandas**: For organizing and saving the data into a CSV file.
- **ChromeDriver**: Required for Selenium to control the Chrome browser. Ensure the ChromeDriver version matches your installed Chrome browser version.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Premkumarbajaru/WebScrapingofRestaurantdatafromgoogle.git
   cd WebScrapingofRestaurantdatafromgoogle
   ```

2. **Install Dependencies**:
   Install the required Python libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**:
   - Download the ChromeDriver executable from [here](https://sites.google.com/chromium.org/driver/).
   - Update the `chromedriver_path` variable in the script with the correct path to the ChromeDriver executable.

4. **Run the Script**:
   Modify the `query` variable in the `main()` function to specify your search query (e.g., "restaurants in Downtown Toronto"):
   ```python
   query = "restaurants in Downtown Toronto"
   ```
   Run the script using the following command:
   ```bash
   python web_scraping_restaurant_data_google.py
   ```

## Output

The script will display the extracted restaurant data in the terminal and save it to a CSV file named `downtown_toronto_restaurants.csv` (or a similar name based on your query).

### Terminal Output Example

```plaintext
Extracted Restaurant Data:
Name: The Keg Steakhouse + Bar
Rating: ★4.5
Phone: +1 416-977-6300
Address: 165 York St, Toronto, ON M5H 3R7, Canada

Name: Pai Northern Thai Kitchen
Rating: ★4.6
Phone: +1 416-901-4724
Address: 18 Duncan St, Toronto, ON M5H 3G8, Canada

Data saved to 'downtown_toronto_restaurants.csv'
```

### CSV File Structure

The CSV file will have the following structure:

```plaintext
Name,Rating,Phone,Address
The Keg Steakhouse + Bar,★4.5,+1 416-977-6300,165 York St, Toronto, ON M5H 3R7, Canada
Pai Northern Thai Kitchen,★4.6,+1 416-901-4724,18 Duncan St, Toronto, ON M5H 3G8, Canada
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes. When contributing, ensure that your changes are well-documented and do not break existing functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README provides a clear and concise guide to understanding and running the Web Scraping of Restaurant Data from Google script. It covers the objectives, features, requirements, how to run the script, output, and CSV file structure.
