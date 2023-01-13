### **Hi yes**

This bot was coded in a few nights by Clayyyy#1366 on discord
The source code is messy and jenky, and should not be used to learn

Still, if you want to use something like this, follow the directions here

1. Make an application on the [discord developer portal](https://discord.com/developers) (If you wish, you can give your bot an "About Me" description here)
2. Go down to the "bot" tab
3. Click the "Make A Bot" Button, copy the token (You can also name it or give it a pfp, idc)
4. Paste the token into the `token` section in the `config.json file`
5. Go to OAuth2 and go down to URL Generator
6. Click 'bot' on the left and give it `Admin` perms
7. Copy the url and go to it
8. Invite the bot
9. Run the `beanbot.py` file
Your done, the commands should take around an hour to update across guilds. You might need to restart it a few times


### **Config**
```
{
    ['token'] - (string) The bots token. This runs the bot and logs in
    ['on'] - (int) is the bot enabled? 0 is disabled, 1 is enabled
    ['chance'] - (int) Whats the random chance? (35 would be 1 in 35 chance)
    ['status'] - (string) The "Playing xxxxx" found on the bot's profile
    ['adminrole'] - (int) The role id who can edit the bot. Leave as 0 for no admin role
    ['allowedchannel'] - (int) The channel id that the random messages can be sent in. Leave 0 for use in all channels
}
```
To add messages, please use the commands



### **Commands**
You can view the commands [here](https://docs.google.com/document/d/1s1WaFZJ32MibsfDf4sYifXd84n55ymBpLoIxw8LPeZ8/edit?usp=sharing)
<> are used for arguments. Example: `/analysis Hello billy`
```
/info - gets the bot's information
/cmds - Shows the commands
/uptime - gets the bot's uptime
/analysis <string> - Uses the TextBlob sentiment analysis to test provided string

===Admin commands===
/rate <int, 1-200> - Set's the random chance
/switch - Toggles the bot on and off\
/addword <string> - Adds a random response
/addbadword <string> - Adds a bad response
/addgoodword <string> - Adds a good response
```
