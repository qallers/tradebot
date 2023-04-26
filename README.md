# tradebot

The tradebot.py file is not complete. API's and API keys need to be generated and configured etc. 

In order to run this application locally on silly windows PC's look into the following:

https://docs.docker.com/desktop/install/windows-install/

For amazing Linux PC's you whould have run the following:

sudo apt update
sudo apt install docker.io

# To run the docker container locally (once everything is installed) do the following:

1. Clone this repo (which you would need git again something on Linux already)
2. Browse to the cloned code
3. Run docker build -t forex-trading-bot .
4. Run docker run -p 8080:8080 forex-trading-bot

Go to your browser and enter http://localhost:8080.

Good luck...
