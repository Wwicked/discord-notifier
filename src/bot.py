import discord
import repo.src.messages as messages
import asyncio
import psutil
import time
import subprocess
import repo.src.config as config


def is_process_running(name):
    for proc in psutil.process_iter():
        try:
            if name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False


def broadcast_discord_message(token, channel_name, embed):
    intents = discord.Intents.default()
    intents.typing = True
    intents.messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = discord.utils.get(client.get_all_channels(), name=channel_name)

        await channel.send(embed=embed)
        await client.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(token=token, reconnect=True))


def start_game(steam_path, appid):
    subprocess.call(f"{steam_path}\Steam.exe -applaunch {appid}")


def wait_for_game_to_start(process_name, interval, max_tries=50):
    tries = 0
    started = False

    while True:
        if tries >= max_tries:
            break

        if is_process_running(process_name):
            started = True
            break
        else:
            time.sleep(interval)
            tries += 1

    return started


def wait_for_game_to_terminate(process_name, interval):
    while is_process_running(process_name):
        time.sleep(interval)


def main():
    start_time = time.time()

    print("Starting csgo...")
    start_game(config.STEAM_PATH, config.CSGO_APP_ID)
    started = wait_for_game_to_start(
        config.CSGO_PROCESS_NAME,
        config.PROCESS_LIFE_CHECK_INTERVAL,
        config.MAX_PROCESS_LIFE_CHECK_TRIES,
    )

    if not started:
        exit(0)

    print("Started successfuly!")

    # Immediately notify about the game launching
    print(f"Attempting to broadcast game launch")
    broadcast_discord_message(
        config.TOKEN, config.TARGET_CHANNEL_NAME, messages.game_on()
    )
    print(f"Broadcasted game launch successfuly")

    wait_for_game_to_terminate(
        config.CSGO_PROCESS_NAME, config.PROCESS_LIFE_CHECK_INTERVAL
    )

    # Broadcast the game process being terminated
    print(f"Attempting to broadcast game termination")
    broadcast_discord_message(
        config.TOKEN, config.TARGET_CHANNEL_NAME, messages.game_off(start_time)
    )
    print(f"Broadcasted game termination successfuly")


if __name__ == "__main__":
    main()
