import functions_framework
import requests

@functions_framework.http
def ical_proxy_request(request):
    """
    An HTTP-triggered function that proxies a request to fetch an iCal file.
    The target URL is passed as a query parameter.
    Example: https://YOUR_FUNCTION_URL?url=https://TARGET_ICAL_URL
    """
    target_url = request.args.get('url')

    if not target_url:
        return "Error: 'url' parameter is missing.", 400

    # Define the custom User-Agent required by the target server
    custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

    headers = {
        'User-Agent': custom_user_agent
    }

    try:
        # Make the request to the target server with the custom header
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Return the content with the correct Content-Type header
        return response.text, 200, {'Content-Type': 'text/calendar'}

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the remote server: {e}", 502
