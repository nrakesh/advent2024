import requests
import os

def get_input(day, year=2024):
    # Load session cookie from environment variable
    session_cookie = "53616c7465645f5f5d540a4085ff4fcbbd6538583db70f2d0c41febbf3e6d8eb4d23b39271360206ed8a6bb09daf28a7022b57428dfd67da7dafce9460660e76"
    if not session_cookie:
        raise ValueError("AOC_SESSION environment variable not set!")
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_cookie}

    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  # Raise an exception for bad status codes
        input_data = response.text
        filename = f"{year}-{day}-input.txt"
        if input_data:
            try:
                with open(filename, "w") as f:
                    f.write(input_data)
                print(f"Input for day {day}, year {year} saved to {filename}")
            except OSError as e:
                print(f"Error writing to file: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error fetching input: {e}")
        return None

# Example usage:
day = 3
input_data = get_input(day)
