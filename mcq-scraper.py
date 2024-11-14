import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

def scrape_mcqs(start_page=2, end_page=10, output_file=None):
    """
    Scrape MCQs from pakmcqs.com and optionally save to CSV file.
    
    Args:
        start_page (int): Starting page number
        end_page (int): Ending page number
        output_file (str): Optional CSV file path to save results
    """
    # Base URL with placeholder for page number
    base_url = "https://pakmcqs.com/category/english-mcqs/page/{}"
    
    # List to store all MCQs
    all_mcqs = []
    
    # Create CSV file if output_file is specified
    if output_file:
        csv_file = open(output_file, 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Question', 'Description', 'Correct Answer', 'Timestamp'])

    try:
        # Loop through the range of pages
        for page in range(start_page, end_page + 1):
            try:
                # Format the URL with the current page number
                url = base_url.format(page)
                
                # Send a GET request to the current page
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for bad status codes

                # Parse the HTML content
                soup = BeautifulSoup(response.text, "html.parser")
                
                # Select all MCQ posts on the page
                mcq_posts = soup.select("article.grid-card-post")
                
                # Loop through each MCQ post and extract relevant information
                for post in mcq_posts:
                    try:
                        # Extract the question title
                        title = post.select_one("h2.post-title a").text.strip()
                        
                        # Extract the description
                        description = post.select_one("div.excerpt").text.strip()
                        
                        # Remove any "submitted by" text
                        description = description.split("Submitted by")[0].strip()
                        
                        # Extract the correct answer
                        correct_answer = post.select_one("div.excerpt strong")
                        correct_answer = correct_answer.text.strip() if correct_answer else "Not specified"
                        
                        # Get current timestamp
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                        # Store the MCQ data
                        mcq_data = {
                            'question': title,
                            'description': description,
                            'correct_answer': correct_answer,
                            'timestamp': timestamp
                        }
                        all_mcqs.append(mcq_data)
                        
                        # Write to CSV if output file is specified
                        if output_file:
                            csv_writer.writerow([title, description, correct_answer, timestamp])
                        
                        # Print the extracted data
                        print(f"Question: {title}")
                        print(f"Description: {description}")
                        print(f"Correct Answer: {correct_answer}")
                        print("-" * 40)
                        
                    except Exception as e:
                        print(f"Error processing MCQ: {str(e)}")
                        continue
                
                print(f"Completed scraping page {page}")
                
                # Delay to avoid overwhelming the server
                time.sleep(1)  # Adjust the delay as needed
                
            except requests.exceptions.RequestException as e:
                print(f"Error accessing page {page}: {str(e)}")
                continue
            
    except KeyboardInterrupt:
        print("\nScraping interrupted by user")
    
    finally:
        if output_file:
            csv_file.close()
            print(f"\nResults saved to {output_file}")
    
    return all_mcqs

if __name__ == "__main__":
    # Example usage
    output_filename = f"mcqs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    results = scrape_mcqs(start_page=2, end_page=10, output_file=output_filename)
    print(f"\nTotal MCQs scraped: {len(results)}")
