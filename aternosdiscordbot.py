import discord
import asyncio
import requests

SERVER_URL = "https://api.mcstatus.io/v2/status/java/ip.aternos.me:port"  # Cambia esto y pon el puerto
EXPECTED_MOTD = "default"  # Cambia esto también

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prev_status = None  # ahora es parte del objeto (self)

    async def on_ready(self):
        print(f'Logged as {self.user}!')
        self.loop.create_task(self.check_server_status())

    async def on_message(self,message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        if message.content.startswith('holi') or message.content.startswith('hello') or message.content.startswith('holas') or message.content.startswith('olas') or message.content.startswith('ola') or message.content.startswith('oli') or message.content.startswith('hola') or message.content.startswith('hi') or message.content.startswith('que fue'):
            await message.channel.send(f'Hola {message.author} :wave:')
        elif message.content.startswith('!quesehace') or message.content.startswith('/quesehace') or message.content.startswith('quesehace') or message.content.startswith('que se hace') or message.content.startswith('que se hace aqui') or message.content.startswith('que se hace aquí') or message.content.startswith('quesehaceaqui') or message.content.startswith('quesehaceaquí') or message.content.startswith('ksehace') or message.content.startswith('quesehac'):
            embed1 = discord.Embed(title=f"¿Qué se hace aquí?",
                                   description="En este server del servidor de minecraft en aternos serás notificado por mi cuando el mismo este en línea, si deseas saberlo inmediatamente escribe el siguiente comando en el chat:",
                                   color=discord.Color.light_gray())
            embed1.set_thumbnail(url="https://media.camozzi.com/Asset/Configuratore-Deactived-Hover.gif")
            embed1.add_field(name="!server",value="",inline= True)
            embed1.set_footer(text="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
            await message.channel.send(embed=embed1)
        elif message.content.startswith('!server') or message.content.startswith('/server') or message.content.startswith('server') or message.content.startswith('serv') or message.content.startswith('aternos') or message.content.startswith('serve'):
            if await self.is_server_online():
                embed2 = discord.Embed(title=f"El server se encuentra en línea :green_circle:!",
                                       description="Únete! Quizá te esten esperando y si quieres prenderlo por ti mismo, envia un mensaje a satomu18 con tu usuario de aternos para que el te de un acceso manual",
                                       color=discord.Color.brand_green())
                embed2.set_thumbnail(url="https://theminecrafthosting.com/es/assets/images/server.gif")
                embed2.set_footer(text="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
                await message.channel.send(embed=embed2)
            else:
                embed3 = discord.Embed(title=f"El server se encuentra fuera de línea :electric_plug:",
                                       description="Si quieres prenderlo por ti mismo, envia un mensaje a satomu18 con tu usuario de aternos para que el te de un acceso manual",
                                       color=discord.Color.brand_red())
                embed3.set_thumbnail(url="https://theminecrafthosting.com/es/assets/images/server.gif")
                embed3.set_footer(text="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
                await message.channel.send(embed=embed3)

    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')  # Cambia 'general' por el nombre del canal donde querés que lo anuncie
        embed4 = discord.Embed(title=f"Bienvenido {member} :wave: :wave:", description="al server del server de mc en aternos xd, escribe en el chat **!quesehace** para descubrir que se hace aqui :v",color=discord.Color.gold())
        embed4.set_footer(text ="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
        await channel.send(embed=embed4)

    async def check_server_status(self):
        cooldown = False
        while True:
            try:
                if not cooldown:
                    response = requests.get(SERVER_URL)
                    if response.status_code == 200:
                        data = response.json()
                        is_online = data.get("motd", {}).get("clean", "") == EXPECTED_MOTD
                        motd_clean = data.get("motd", {}).get("clean", "")
                        print("intente verificarlo")
                        if is_online != self.prev_status:
                            self.prev_status = is_online
                            if is_online:
                                embed2 = discord.Embed(title=f"El server se acaba de poner en línea :green_circle:!",
                                                       description="Únanse! alguien acaba de prender el server",
                                                       color=discord.Color.brand_green())
                                embed2.set_thumbnail(url="https://theminecrafthosting.com/es/assets/images/server.gif")
                                embed2.set_footer(text="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
                                guild = discord.utils.get(self.guilds,
                                                          name='arrabal')  # pon tu nombre real del servidor
                                channel = discord.utils.get(guild.text_channels, name='ecuamid')
                                await channel.send(embed=embed2)
                                cooldown = True
                                await asyncio.sleep(5)  # espera 1 hora antes de volver a notificar
                                cooldown = False
                            else:
                                embed3 = discord.Embed(title=f"El server se acaba de desconectar :electric_plug:!",
                                                       description="Probablemente haya sido por inactividad, asi que si quieres prenderlo por ti mismo, envia un mensaje a satomu18 con tu usuario de aternos para que el te de un acceso manual",
                                                       color=discord.Color.brand_red())
                                embed3.set_thumbnail(url="https://theminecrafthosting.com/es/assets/images/server.gif")
                                embed3.set_footer(text="Bot hecho por @_ljuan en ig el 19/4/2025 a las 3:15am")
                                guild = discord.utils.get(self.guilds,
                                                          name='arrabal')  # pon tu nombre real del servidor
                                channel = discord.utils.get(guild.text_channels, name='ecuamid')
                                await channel.send(embed=embed3)
                                cooldown = True
                                await asyncio.sleep(5)  # espera 1 hora antes de volver a notificar
                                cooldown = False

                    else:
                        print(f"Falló la petición: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error al verificar estado del server: {e}")
            await asyncio.sleep(10)

    async def is_server_online(self):
        try:
            response = requests.get(SERVER_URL)
            if response.status_code == 200:
                data = response.json()
                return data.get("motd", {}).get("clean", "") == EXPECTED_MOTD
        except Exception as e:
            print(f"Error al chequear el server manualmente: {e}")
        return False
intents = discord.Intents.default()
intents.message_content = True #lo pone online o no
intents.members = True

client = Client(intents=intents)
client.run('YOUR BOT ID')