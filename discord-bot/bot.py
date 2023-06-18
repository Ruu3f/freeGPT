import discord, asyncio, aiosqlite
from discord.ext import commands
from freeGPT import gpt3, gpt4, alpaca_7b

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="f?", intents=intents, help_command=None)
database = None


async def connect_to_database():
    return await aiosqlite.connect("database.db")


@bot.event
async def on_ready():
    global database
    database = await connect_to_database()
    await database.execute(
        """
        CREATE TABLE IF NOT EXISTS datastorage (
            guilds INTEGER,
            channels INTEGER,
            model TEXT
        )
        """
    )
    await database.commit()
    print(f"{bot.user.name} has connected to Discord!")
    while True:
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{len(bot.guilds)} servers.",
            ),
        )
        await asyncio.sleep(300)


@bot.hybrid_command(name="help", description="Get help.")
async def help(ctx):
    embed = discord.Embed(title="Help Menu", color=0x00FFFF)
    embed.add_field(
        name="setup",
        value="Usage:\n- `f?setup {model, gpt3, gpt4, alpaca_7b}`\n- `/setup {model, gpt3, gpt4, alpaca_7b}`",
    )
    embed.add_field(name="reset", value="Usage:\n- `f?reset`\n- `/reset`")
    await ctx.send(embed=embed)


@bot.hybrid_command(name="setup", description="Setup the chatbot.")
@commands.has_guild_permissions(manage_channels=True)
@commands.bot_has_guild_permissions(manage_channels=True)
async def setup(ctx, model: str):
    cursor = await database.execute(
        "SELECT channels, model FROM datastorage WHERE guilds = ?", (ctx.guild.id,)
    )
    data = await cursor.fetchone()
    if data:
        await ctx.send(
            "The chatbot is already set up. Try using the `/reset` command to fix this error."
        )
        return

    if model.lower() in ["alpaca_7b", "gpt3", "gpt4"]:
        channel = await ctx.guild.create_text_channel("freegpt", slowmode_delay=10)
        await database.execute(
            "INSERT OR REPLACE INTO datastorage (guilds, channels, model) VALUES (?, ?, ?)",
            (
                ctx.guild.id,
                channel.id,
                model,
            ),
        )
        await database.commit()
        await ctx.send(f"Successfully set the channel to {channel.mention}.")
    else:
        await ctx.send(
            "Error: Model not found! Please choose between `gpt3`, `gpt4` and `alpaca_7b`"
        )


@bot.hybrid_command(name="reset", description="Reset the chatbot.")
@commands.has_guild_permissions(manage_channels=True)
async def reset_gpt(ctx):
    cursor = await database.execute(
        "SELECT channels, model FROM datastorage WHERE guilds = ?", (ctx.guild.id,)
    )
    data = await cursor.fetchone()
    if not data:
        await ctx.send(
            "The chatbot is not set up. Try using the `/setup` command to fix this error."
        )
        return

    await database.execute("DELETE FROM datastorage WHERE guilds = ?", (ctx.guild.id,))
    await database.commit()
    await ctx.send("The chatbot has been reset.")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    cursor = await database.execute(
        "SELECT channels, model FROM datastorage WHERE guilds = ?", (message.guild.id,)
    )
    data = await cursor.fetchone()
    if data:
        channel_id, model = data
        if message.channel.id == channel_id:
            await message.channel.edit(slowmode_delay=10)
            async with message.channel.typing():
                try:
                    if model.lower() == "gpt3":
                        resp = str(
                            gpt3.Completion.create(prompt=message.content)["text"]
                        )
                    elif model.lower() == "gpt4":
                        resp = str(gpt4.Completion.create(prompt=message.content))
                    elif model.lower() == "alpaca_7b":
                        resp = str(alpaca_7b.Completion.create(prompt=message.content))
                    await message.channel.send(str(resp))
                except Exception as e:
                    await message.channel.send(e)


TOKEN = ""
bot.run(TOKEN)
