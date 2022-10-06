from typing import Optional

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from simple_chalk import chalk, green


class Commands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="ping")
    async def ping_command(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @command(name="slap", aliases=["hit"])
    async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "for no reason"):
        await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reason}!")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("commands")
        print(f'{green.yellow("[SYS]")} Ready to serve you Master')


async def setup(bot):
    await bot.add_cog(Commands(bot))
