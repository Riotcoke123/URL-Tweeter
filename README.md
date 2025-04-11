<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h1>URL Tweeter</h1>
    <p><strong>URL Tweeter</strong> is an automated Python script that allows you to tweet websites (URLs) directly from a text file. It ensures that tweets are sent within a daily limit, helping you schedule and share links in an organized way.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Automated Tweeting:</strong> Automatically tweets URLs from a text file.</li>
        <li><strong>Rate Limiting:</strong> Sends up to 50 tweets per 24-hour period to comply with Twitter's API limits.</li>
        <li><strong>Customizable:</strong> Easily modify the script to suit your needs.</li>
        <li><strong>Error Handling:</strong> Includes basic error handling for API requests.</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><a href="https://www.tweepy.org/" target="_blank">Tweepy</a> library</li>
        <li>Twitter Developer Account with API keys</li>
    </ul>
    <h2>Setup</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/Riotcoke123/URL-Tweeter.git
cd URL-Tweeter</code></pre>
        </li>
        <li>Install the required Python packages:
            <pre><code>pip install tweepy</code></pre>
        </li>
        <li>Create a <code>config.py</code> file and add your Twitter API credentials:
            <pre><code>API_KEY = 'your_api_key'
API_KEY_SECRET = 'your_api_key_secret'
BEARER_TOKEN = 'your_bearer_token'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'</code></pre>
        </li>
        <li>Prepare a <code>websites.txt</code> file with each URL on a new line.</li>
    </ol>
    <h2>Usage</h2>
    <p>Run the script:</p>
    <pre><code>python your_script.py</code></pre>
    <p>The script will read URLs from <code>websites.txt</code> and tweet them, ensuring that the daily limit is not exceeded.</p>
    <h2>License</h2>
    <p>This project is licensed under the GPL-3.0 License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>
</body>
</html>
