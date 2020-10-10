from discord.ext import commands
import discord


class react_roles(commands.Cog):

    # Mappings for roles {message_id: {'emoji': role_id}}
    mapping = {
        763466119990083595: { #Batches
            "🌱": 763462230540812298,
            "🍦": 763462194473074718,
            "🥲": 763462159534653451,
            "🧟‍♂️": 763462130317131846,
            "👨‍🎓": 763461855578161192,
            "👴": 763462275277127682
        },
        763598798776827904: { #Interests
            '⚽': 763595482429653043,
            '🎮': 763595543602921512,
            '📱': 763595591531102218,
            '🔨': 763598078258315275
        },
        764011007042519060: {
            '🔋': 764010409610313739
        }
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.bot.resistorman_id:
            return
        await self.manage_roles(self, payload, True)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await self.manage_roles(self, payload, False)

    async def manage_roles(self, ctx, payload, add_role: bool):

        if not payload.message_id in self.mapping:
            print("returned on message id")
            return

        if not str(payload.emoji) in self.mapping[payload.message_id]:
            print("returned on mapping")
            return

        role_emoji = self.mapping[payload.message_id][str(payload.emoji)]
        role = discord.utils.get(self.bot.get_guild(
            payload.guild_id).roles, id=role_emoji)
        member = discord.utils.get(self.bot.get_guild(
            payload.guild_id).members, id=payload.user_id)

        if add_role:
            await payload.member.add_roles(role)
            msg = f"You have given yourself the **{role.name}** role on the **{role.guild} discord server**!"
            await payload.member.send(content=msg)

        else:
            await member.remove_roles(role)


def setup(bot):
    bot.add_cog(react_roles(bot))
