from jira import JIRA

jira = JIRA(server=j1server, token_auth=(env0secretToken), timeout = int(j1timeout))

issues = jira.search_issues(j1query, maxResults=int(j1maxResult))

with open(j1jiraText, "w", encoding="utf-8") as f:
    for issue in issues:
        f.write(f"{issue.key}: {issue.fields.summary}\n")
        f.write(f"Status: {issue.fields.status}\n")
        f.write(f"Priority: {issue.fields.priority}\n")
        f.write(f"Updated: {issue.fields.updated}\n")
        f.write(f"Description: {issue.fields.description}\n")
        f.write("\n" + "-"*45 + "\n")
print("Jira issues saved to " + j1jiraText)
