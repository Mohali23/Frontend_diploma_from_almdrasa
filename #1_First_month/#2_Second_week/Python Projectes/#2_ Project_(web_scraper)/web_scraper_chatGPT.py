import requests

GITHUB_API_BASE_URL = 'https://api.github.com/users/'

def get_github_repositories(username):
  try:
    # Construct the URL for the GitHub API using the provided username
    url = f'{GITHUB_API_BASE_URL}{username}/repos'

    # Send a GET request to the GitHub API to fetch repository data
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Convert the response data to JSON format
    repositories_data = response.json()

    # Iterate through the repositories and display relevant information
    for repo in repositories_data:
      print(f"Repository: {repo['name']}")
      print(f"Description: {repo['description']}")
      print(f"Language: {repo['language']}")
      print(f"Star Count: {repo['stargazers_count']}")
      print("\n" + "=*"*25 + "\n")  # Print a separator line after each repository

  except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

if __name__ == "__main__":
  # Get a Github username from the user
  ask_user_about_github_username = input('What is your Github username? ')
  get_github_repositories(ask_user_about_github_username)
