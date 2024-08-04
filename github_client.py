import requests

class GitHubClient:
    def __init__(self, token, user):
        """
        Initialize GitHubClient with a token and a username.

        Args:
            token (str): GitHub access token.
            user (str): GitHub username.
        """
        self.github_token = token
        self.user = user

    def make_github_request(self, url):
        """
        Make a request to the GitHub API.

        Args:
            url (str): API endpoint URL.

        Returns:
            dict: JSON response from the API.
        """
        headers = {'Authorization': f'token {self.github_token}'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error accessing the GitHub API: {e}")
            return None

    def get_github_user_data(self, username):
        """
        Get data for a GitHub user.

        Args:
            username (str): GitHub username.

        Returns:
            dict: User data.
        """
        url = f"https://api.github.com/users/{username}"
        return self.make_github_request(url)

    def get_all_followers(self):
        """
        Get all followers of a GitHub user.

        Returns:
            list: List of followers.
        """
        url = f"https://api.github.com/users/{self.user}/followers"
        return self.make_github_request(url)

    def collect_followers_data(self):
        """
        Collect data of all followers.

        Returns:
            list: List of followers' data.
        """
        followers = self.get_all_followers()
        followers_data = []
        if followers:
            for follower in followers:
                follower_data = self.get_github_user_data(follower['login'])
                if follower_data:
                    followers_data.append({
                        'name': follower_data.get('name'),
                        'company': follower_data.get('company'),
                        'blog': follower_data.get('blog'),
                        'email': follower_data.get('email'),
                        'bio': follower_data.get('bio'),
                        'public_repos': follower_data.get('public_repos'),
                        'followers': follower_data.get('followers'),
                        'following': follower_data.get('following'),
                        'created_at': follower_data.get('created_at')
                    })
        return followers_data
