import os
from github import Github
from utility import *

def main():
    g = Github(os.getenv('MY_GITHUB_TOKEN'))

    repo_path = os.getenv('REPO_PATH')

    pull_request_number = int(os.getenv('PR_NUMBER'))

    repo = g.get_repo(repo_path)

    readme_content = repo.get_contents('README.md')

    pull_request = repo.get_pull(pull_request_number)

    pull_request_diffs = [
        {
            'filename': file.filename,
            'patch': file.patch
        }
        for file in pull_request.get_files()
    ]

    commit_messages = [commit.commit.message for commit in pull_request.get_commits()]

    prompt = format_data_for_openai(pull_request_diffs, readme_content, commit_messages)

    updated_readme = call_openai(prompt)

    update_readme_and_create_pr(repo, updated_readme, readme_content.sha)

if __name__ == '__main__':
    main()
