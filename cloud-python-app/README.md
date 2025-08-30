This is a backup calendar retrieval option based on the solution by https://github.com/bagheera2382 here https://github.com/derekantrican/GAS-ICS-Sync/issues/494#issuecomment-3201154245.

Here is a summary of the solution.

The most effective workaround is to use a Google Cloud Function as a proxy. The Apps Script calls the Cloud Function, which then makes the request to the target server with the required custom User-Aagent. The function relays the response back to the Apps Script.

This approach successfully bypasses the limitation because the Cloud Function's environment allows full control over outgoing HTTP headers.

Implementation Steps:
1.Create a Google Cloud Function
2.Environment: 2nd Gen
3.Trigger: HTTP Endpoint (Allow unauthenticated invocations for simplicity)
4.Runtime: Python

Use the main.py and requirements file in this directory.