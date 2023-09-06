## How it works

1. After GET request on '/' server sends an html document where moscow time is already displayed
2. html document sends request for css file, and server responses to this request
3. If user tries to enter some url which is different from '/', he gets 404 HTTP status and application redirects user to '/'
4. For creating the html document application uses Jinja2 templating engine
3. Moscow time is calculated based on fact that time offset in Moscow is UTC+3