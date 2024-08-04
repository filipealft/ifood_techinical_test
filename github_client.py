# github_client.py

import requests

class GitHubClient:
    def __init__(self, token, user):
        self.github_token = token
        self.user = user

    def make_github_request(self, url):
        headers = {'Authorization': f'token {self.github_token}'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API do GitHub: {e}")
            return None

    def get_github_user_data(self, username):
        url = f"https://api.github.com/users/{username}"
        return self.make_github_request(url)

    def get_all_followers(self):
        url = f"https://api.github.com/users/{self.user}/followers"
        return self.make_github_request(url)

    def collect_followers_data(self):
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
