YouTube Statistics 📊
Overview ℹ️
This repository provides detailed instructions and handy scripts for extracting YouTube statistics using the powerful YouTube Data v3 API combined with AWS Lambda. Additionally, it offers configurations for seamlessly analyzing the data through Amazon Athena.

Obtaining YouTube API Credentials 🔑
To seamlessly access the YouTube API, simply follow these straightforward steps:

Navigate gracefully to the Google Cloud Console.
Select the majestic "APIs & Services" section, then graciously click on "Library".
Delicately search for the "YouTube Data v3" API and elegantly enable it.
Obtain the API credentials and securely preserve their grace.
Getting Statistics in our youtube_statistics.ipynb File 📈
Easily retrieve YouTube statistics with finesse by following the guidance presented in the youtube_statistics.ipynb file:

Ensure that the API credentials are elegantly configured.
Gracefully obtain the YouTube channel ID by following the provided steps.
AWS Lambda Setup 🚀
Prepare for lift-off with AWS Lambda using these steps of splendor:

Gain access to the celestial AWS Console and gracefully navigate to the Lambda section.
With the elegance of a swan, create a new Lambda function with Python as the chosen programming language.
Configure the celestial function with basic details and add a layer containing the illustrious Pandas library.
Design the Lambda function code with the finesse required to perform the desired actions.
Once the preparation is complete, gracefully save the changes and conduct a test of the Lambda function.
Environment Variables 🌐
Set up an environment of harmonious variables, including the name and ID of the channel to be analyzed.
Lambda Test 🧪
Test with poise by configuring a harmonious sample event.
Automation with EventBridge ⏰
Enchanting automation awaits as you create a rule in EventBridge to orchestrate the execution of the Lambda function.
Set up a trigger with the previously created rule, embracing the elegance of automation.
Insights with Amazon Athena 🌟
Unlock profound insights with Amazon Athena through these enchanted steps:

Upload the collected CSV files from the enchanted YOUTUBE_FILE_CHANNELS folder to the ethereal youtube-demo-stats1 bucket.
Cast a spell by creating a catalog or table in AWS Glue, aptly named youtube_stats_demo1, housing the data from the celestial bucket.
Invoke the power of a crawler to gracefully craft the table in the ethereal channel_stats database.
Delve deep into the mysteries of the data realm by performing queries using the provided options and the sacred queries.txt file.
Cloud Architecture Used ☁️
Marvel at the elegant cloud architecture employed in this project:

The graceful Google Cloud Platform is summoned to obtain the enchanting YouTube API credentials.
AWS Lambda ascends to execute functions with celestial prowess.
Amazon Athena reigns supreme for data analysis in the enchanted clouds.
AWS Glue is summoned to elegantly craft catalogs or tables.
EventBridge orchestrates the celestial dance of event automation.
Embark on a journey of enlightenment as you analyze your YouTube statistics with this ethereal setup! ✨





