# tradebot

The tradebot.py file is not complete. API's and API keys need to be generated and configured etc. 

In order to run this application locally on silly windows PC's look into the following:

https://docs.docker.com/desktop/install/windows-install/

Install Git on Windows:

https://github.com/git-guides/install-git

For amazing Linux PC's you whould have run the following:

sudo apt update
sudo apt install docker.io

# To run the docker container locally (once everything is installed) do the following:

1. Clone this repo (which you would need git again something on Linux already)
2. Browse to the cloned code
3. Run docker build -t forex-trading-bot .
4. Run docker run -p 8080:8080 forex-trading-bot

Go to your browser and enter http://localhost:8080.

## Please note that ALL changes made should either be made here in Github repo or you can clone the repo to your PC and make changes there. 
If you made changes to code you should do the following:

1. git add *
2. git commit -m "Changes made whatever message"
3. git push

Its always a good idea, if you make frequent changes to run git commit and git push at the end of each day. This will make sure that changes don't get lost. Also at the start of your new day run git pull and git fetch --all.

Good luck...
