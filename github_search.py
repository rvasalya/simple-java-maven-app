import requests

def github_search(access_token, repo_owner, repo_name, keyword):
    url = f"https://github.com/jenkins-docs/simple-java-maven-app.git/code/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": f"{keyword}+repo:{repo_owner}/{repo_name}",
        "sort": "relevance"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200:
        results = data.get("items", [])
        for result in results:
            file_path = result["path"]
            html_url = result["html_url"]
            print(f"Repository: {repo_owner}/{repo_name}")
            print(f"File Path: {file_path}\nURL: {html_url}\n")

    else:
        print("Error:", data.get("message", "An error occurred"))

if __name__ == "__main__":
    access_token = "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"  
    predefined_repositories = [
        {"owner": "rvasalya", "name": "simple-java-maven-app"},
        {"owner": "owner2", "name": "repo2"},
        # we can add other repositories as needed
    ]
    
    search_keyword = input("Enter the keyword to search within the repositories: ")
    
    for repo_info in predefined_repositories:
        github_search(access_token, repo_info["owner"], repo_info["name"], search_keyword)
