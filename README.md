# MemeBot

this project sends a welcome message along with meme when a user joins a discord server.

## how to create a bot?

### step 1
go to https://discord.com/developers/applications

click on new application and create a new application

![Screenshot 2022-10-07 at 1 01 38 PM](https://user-images.githubusercontent.com/11372162/194497650-50b0fd9b-da26-4bd4-b106-5a5016f47842.png)

### step 2

once you create an application click and open that application

![Screenshot 2022-10-07 at 1 02 12 PM](https://user-images.githubusercontent.com/11372162/194497723-e57931ef-e25c-4d40-ba73-81b09ecd059e.png)

### step 3

click on the Bot from the menu and edit the details as shown below.

click on reset token to generate the token. copy the generated token into .env file in the code.

check the public bot option if you want your bot to be publically available.
check all the Privileged Gateway Intents like PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT if your bot needs those intent.

Note: for this application we need those intents.

![image](https://user-images.githubusercontent.com/11372162/194498518-e535b2d0-0b64-4d1d-8527-f49314be16cb.png)

### step 4
go to OAuth2 > URL Generator

choose **bot** from the scopes

then choose all the bot permission need and copy the generated url

![image](https://user-images.githubusercontent.com/11372162/194498853-8ba28265-ab65-4df1-9e25-8d8913decfdb.png)

### step 5
open the generated url from the previous steps

choose the server that you want to add the bot to and click continue.

![image](https://user-images.githubusercontent.com/11372162/194499328-3874ccf5-d099-4f83-b62d-af091b06773a.png)

### step 6 

once the bot is added it will appear on your discord server in offline mode.
now run the code in the repository to activate your bot
