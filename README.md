# NASA Daily Image Viewer

The **NASA Daily Image Viewer** is a Python-based project that fetches the Astronomy Picture of the Day (APOD) from NASA's API and displays the image along with its description. This application is a great way to explore the cosmos and learn about the fascinating images captured by NASA.

---
## Features

- Fetches the Astronomy Picture of the Day (APOD) from NASA's API.
- Displays the image along with its title, date, and description.
- Handles errors gracefully, such as missing images or API downtime.
- Built with Python for simplicity and flexibility.

---
## Technologies Used

**Python**: Core programming language.
- **Streamlit**: For creating the web interface (choose the one you've used).
- **Requests**: To make API calls.
- **JSON**: For parsing API responses.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. Python 3.8 or higher
2. pip (Python package installer)

---

## API Details

- Base URL: https://api.nasa.gov/planetary/apod

- Parameters:
  1. api_key: Your NASA API key.
  2. date (optional): Fetch a specific date's image in the format YYYY-MM-DD.

- Example Request:

```bash
    https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
```