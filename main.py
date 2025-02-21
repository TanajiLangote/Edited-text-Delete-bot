import tgcrypto
from pyrogram import Client, filters

# Replace 'my_bot' with your bot's name, and provide your API ID and hash
app = Client("7828276514:AAG5JojoEFTj2o4Js9sqXgigEe2vVMR1MmA", api_id='13485297', api_hash='4858ef14a1e4e5d1f496560f33ec9cb4')

@app.on_edited_message()
async def delete_edited_message(Client, message):
        await message.delete()  # Deletes the edited message

if __name__== "main":
    app.run()
