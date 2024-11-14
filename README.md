# scrape_mcqs
Python scraper to extract MCQs, options, and answers from MCQs website with multi-page support.

A Python script to scrape Multiple Choice Questions (MCQs) from the [PakMCQs](https://pakmcqs.com/) website. This scraper extracts questions, options, and identifies the correct answers across multiple pages.

## Features

- **Scrapes Multiple Categories:** Easily modify the script to scrape different MCQ categories.
- **Handles Pagination:** Automatically navigates through multiple pages.
- **Identifies Correct Answers:** Highlights the correct option for each question.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/xxOmen/pakmcqs-scraper.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd pakmcqs-scraper
    ```

3. **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Modify Scraper Parameters:**
   
   Open `scrape_mcqs.py` and adjust the following variables as needed:
   
   - `base_url`: The base URL of the category you want to scrape. For example:
     ```python
     base_url = "https://pakmcqs.com/category/english-mcqs/page/{}"
     ```
   
   - `start_page` and `end_page`: Define the range of pages to scrape.
     ```python
     start_page = 2
     end_page = 259  # Modify this range as needed
     ```

2. **Run the Scraper:**
    ```bash
    python scrape_mcqs.py
    ```
   The script will output each question along with its options and highlight the correct answer.

