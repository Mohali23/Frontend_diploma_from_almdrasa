import requests

# Define a function to scrape GitHub repositories for a given username
def get_github_repositories(username):
    # Construct the URL for the GitHub API using the provided username
    url = f'https://api.github.com/users/{username}/repos'

    # Send a GET request to the GitHub API to fetch repository data
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response data to JSON format
        repositories_data = response.json()

        # Iterate through the repositories and display relevant information
        for repo in repositories_data:
            print(f"Repository: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Language: {repo['language']}")
            print(f"Star Count: {repo['stargazers_count']}")
            print("\n" + "=*"*25 + "\n")  # Print a separator line after each repository

    else:
        # Print an error message if the request was not successful
        print(f"Request failed, Status Code: {response.status_code}")


# Get a Github username from user
ask_user_about_github_username = input('What is your Github username?')
get_github_repositories(ask_user_about_github_username)
