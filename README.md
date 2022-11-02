[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=542440024)

# Javascript Discord Welcome MemeBot with GitHub Codespaces

<img src="https://octodex.github.com/images/Robotocat.png" alt="image of robotocat" width="200" style="border:100px solid black"/>

Customize and deploy your own welcome memebot for your Discord server! 

This template repository has all the code you need, with a preconfigured Codespaces development environment, to send a welcome message along with a meme when a user joins your Discord server.

## How to customize your bot
<img src="https://octodex.github.com/images/manufacturetocat.png" alt="image of manufacturetocat" width="200"/>

### Step 1: Add a .env file
This template repository requires a `.env` file to pass variables to your application. The `.env` file is used to store data that you want to keep private or hidden like API keys or tokens from external services like Discord. 

This template repository has a sample .env file, `.env-sample`, that you can rename to `.env` or copy and paste the variables in `.env-sample` into a new `.env` file. 

### Step 2: Add your favorite meme
In your `.env` file you will find a variable named `MEME_URL` where you can add a URL to your favorite meme. 

### Step 3: Add a personalized welcome message
In the `src` directory you will find another directory called `events`. Open the `events` directory and you will find the `guildMemberAdd.js` file. You'll notice that we left helpful comments on where you can update the code to your liking.

To add a welcome message, you can update the `getWelcomeMessage` function after the `content:` keyword.

![code block of get welcome message function](https://user-images.githubusercontent.com/10368374/199597840-dd83efa6-8251-4def-868f-cdadb0df6f02.png)

### Step 4 (optional): Customize even further
Maybe you want to use an API service to provide random memes or maybe you don't want to share a meme at all. No matter what route you choose, you should take this Discord bot and make it your own. :smiley:

We recommend [creating a new branch](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches#creating-a-branch) anytime you tinker so you don't have to worry about making mistakes on your main branch. Once your new branch is in a good state, you can [merge your changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges) to your main branch using a pull request. :rocket:

## How to deploy your bot

<img src="https://octodex.github.com/images/jetpacktocat.png" alt="image of jetpacktocat" width="200"/>

### Step 1: Create a new application on Discord
Visit https://discord.com/developers/applications to create a new application on Discord. Once there, click the `new application` button. After you click on the `new application` button, you can then create a new application (Note: That we created a new application called `Bot Developer`):

![Screenshot 2022-10-07 at 1 01 38 PM](https://user-images.githubusercontent.com/11372162/194497650-50b0fd9b-da26-4bd4-b106-5a5016f47842.png)

### Step 2: Open your application

After creating an application you should see the application under `My applications`. Open your newly created application by clicking on it.

![Screenshot 2022-10-07 at 1 02 12 PM](https://user-images.githubusercontent.com/11372162/194497723-e57931ef-e25c-4d40-ba73-81b09ecd059e.png)

### Step 3: Configure your bot user

Select the Bot settings to edit the details. First, click on reset token to generate a new token that you will use in your `.env` file. Copy the generated token and set the `TOKEN` variable in your `.env` file with your newly generated token.

Select the public bot option if you want your bot to be publically available.
Select all the Privileged Gateway Intents like PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT if your bot needs those intents.(Note: For this application you'll need all of these intents.)

![image](https://user-images.githubusercontent.com/11372162/194498518-e535b2d0-0b64-4d1d-8527-f49314be16cb.png)

### Step 4: Select your bot permissions
Open the `OAuth2` setting and then select `URL Generator`.

Select the `bot` checkbox under `SCOPES`. After, select `Send Messages`, `Mention Everyone`, and `Add Reactions`. 

Once you have set your bot permissions copy the generated url below.

![image](https://user-images.githubusercontent.com/11372162/194498853-8ba28265-ab65-4df1-9e25-8d8913decfdb.png)

### Step 5: Choose your Discord Server
Visit the generated url from the previous step and choose the server that you want to add the bot to. Once you've selected the server click continue.

![image](https://user-images.githubusercontent.com/11372162/194499328-3874ccf5-d099-4f83-b62d-af091b06773a.png)

### Step 6: Run your application

Once the bot is added it will appear on your Discord server in offline mode.

You can now run the code in the repository using the command line by typing the command `npm start`. 


