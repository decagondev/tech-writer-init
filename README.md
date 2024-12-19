# Technical Writer Agent

## Introduction
This project demonstrates the development of a **Technical Writer Agent** designed to enhance developer productivity. By leveraging Retrieval-Augmented Generation (RAG), your MVP agent will dynamically update and refine technical documentation, ensuring it remains accurate, up-to-date, and contextually relevant to your data and project.

## Prerequisites
- GitHub account and token
- OpenAI API key

## Project Structure
- `requirements.txt`: List of Python dependencies
- `github/workflows/update-readme.yml`: GitHub Actions workflow to update the README.md file
- `main.py`: Main script that orchestrates the Technical Writer Agent
- `utility.py`: Contains utility functions for GitHub interactions and OpenAI API calls
- `CPURegisters.tsx`: Added a new React component to display CPU registers information.

## Setup

1. Clone or fork the repository
2. If you forked the repository, enable GitHub Actions in your repository
3. Create a GitHub token and add it to the repository secrets
4. Add the OpenAI API key to the repository secrets
5. Create a branch for your changes
6. Create a new file in the root of the repository
7. Add your changes and commit them to the branch
8. Push your changes to the branch
9. Create a pull request. If it was a fork, make sure the base repository is set to the main branch of your forked repository, NOT the original repository.
10. Merge your pull request to the main branch of your forked repository
11. Check the GitHub Actions tab to ensure the workflow ran successfully
12. Check your repository for a new pull request with the README.md changes

## Now It's Your Turn!
We encourage you to personalize this project and address challenges in your own environment. Here's how you can get started:

### Minimum Requirements
1. **RAG Integration:** Implement Retrieval-Augmented Generation to enable your agent to access and utilize external information.
2. **Vector Database Implementation:** Create and implement a vector data store for efficient document embedding and retrieval.

### Stretch Goals
1. **Enhanced UI/UX:** Develop a user-friendly interface with features like real-time suggestions and auto-completion.
2. **Automated Content Updates:** Implement periodic checks and updates to keep documentation current.
3. **Integration with Existing Tools:** Develop integrations with common development tools (e.g., Confluence, Jira, Notion).
4. **Custom Features:** Add unique features that simplify your daily routines and improve efficiency.

## Privacy and Submission Guidelines
- **Submission Requirements:** Submit a link to your public repo or a Loom video showcasing your work on the [BloomTech AI Platform](https://app.bloomtech.com).
- **Sensitive Information:** If your implementation involves sensitive data, a detailed Loom video demonstration is acceptable instead of a public repository.

## Troubleshooting
- Make sure you have enabled GitHub Actions in your repository if it was a fork
- Make sure you have added the GitHub token and OpenAI API key to the repository secrets
- If you are having trouble with the workflow, check the Actions tab to see what might be going wrong

## Need Help?
Refer to the project documentation or reach out to the learning assistant.