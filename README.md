# ReciBot
WebScraper with Google AI integration to save money and generate recipes

Uses selenium library to parse html from publix weekly ad in order to show best deals, as well as Gemini AI to generate recipes for users.

In order to use, simply gain an api key at this link:
https://aistudio.google.com/app/apikey
and create a .env folder in the same directory as the python script containing the following:
GOOGLE_API_KEY=***your key***


The tool is not perfect, my foremost concern is ensuring that the looping of the main function functions as intended in all cases. I would also like to experiment with more dynamic prompt building in order to create a more personalized experience.

Additionally, I plan to experiment with optimizing selenium usage or utilize a different toolkit to scrape the html, as the script currently requires six browsers to open, which takes abou thirty seconds.
