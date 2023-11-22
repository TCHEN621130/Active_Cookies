import argparse
from datetime import datetime
from collections import Counter

def find_most_active_cookie(file_path, date):
    # creates a counter object to store the count of each cookie
    active_cookies = Counter()
    # uses the try and except to catch and handle exceptions
    try:
        # iterates through each line in the file
        with open(file_path, 'r') as file:
            next(file)  # Skips the header line
            for line in file:
                # uses split method to obtain individual elements of the string
                cookie, timestamp = line.strip().split(',')
                timestamp = datetime.fromisoformat(timestamp)
                # if the timestamp date equals the data, we add 1 to the count 
                if timestamp.date() == date:
                    active_cookies[cookie] += 1
    except FileNotFoundError:
        # when we don't find the most active cookie
        print(f"Error: File not found at {file_path}")
        return None

    # finds the most common cookie here 
    most_common_cookie = active_cookies.most_common(1)
    if most_common_cookie:
        return most_common_cookie[0][0]
    else:
        return None

# For testing purposes 
def main():
    # Here, we set up the information of the file path and date
    parser = argparse.ArgumentParser(description='Find the most active cookie for a specified day.')
    parser.add_argument('file_path', type=str, help='Path to the cookie log file')
    parser.add_argument('-d', '--date', type=str, required=True, help='Date in the format YYYY-MM-DD')
    # Uses parse to convert the date values into datetime.data objects 
    args = parser.parse_args()
    date = datetime.strptime(args.date, '%Y-%m-%d').date()
    
    most_active_cookie = find_most_active_cookie(args.file_path, date)
    # calls the function to find the most active cookie and prints it if found
    if most_active_cookie:
        print(most_active_cookie)
    else:
        print("No data found for the specified date.")
# continuously checks if the script is being run 
if __name__ == "__main__":
    main()

