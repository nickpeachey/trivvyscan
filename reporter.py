# process_results.py

import json
import requests

def parse():
    try:
        with open('trivy_results.json', 'r') as file:
            data = json.load(file)
            results = data['Results']
            vuls = results[0]['Vulnerabilities']
            for item in vuls:
                create_jira_issue(item['Title'], item['Description'])
                # print(json.dumps(item['Description'], indent=2))
                # print(json.dumps(item['Title'], indent=2))
                print('------------')
    except FileNotFoundError:
        print(f"Error: File not found")
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in file ")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


JIRA_SERVER = "https://npeachey.atlassian.net"
JIRA_USERNAME = "nick.peachey@googlemail.com"
JIRA_PASSWORD = "ATATT3xFfGF0W_-zL1fi24SmtsofpnGUWUxMLe9gf-mPhPJkmfcKkwnXoztRmciKW9L3ykhWdfAG7OM0S3w9gI8-8S2hvQ5Vm0IuTYvbmeVF_QCMysqyFNYU4ulojHzgSBGzH53MkEmWSQj6c_sPU2idiZiOzPhptKA9H4AHa3IUq96ZxbP4wx8=985C963A"
JIRA_PROJECT_KEY = "BET"
JIRA_ISSUE_TYPE = "Bug"


def create_jira_issue(summary, description):
    url = f"{JIRA_SERVER}/rest/api/2/issue/"
    headers = {
        "Content-Type": "application/json"
    }
    auth = (JIRA_USERNAME, JIRA_PASSWORD)
    data = {
        "fields": {
            "project": {
                "key": JIRA_PROJECT_KEY
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": JIRA_ISSUE_TYPE
            }
        }
    }
    response = requests.post(url, headers=headers, auth=auth, json=data)
    if response.status_code == 201:
        print(f"Jira issue created successfully: {response.json()['key']}")
    else:
        print(f"Failed to create Jira issue. Status code: {response.status_code}, Response: {response.text}")




parse()