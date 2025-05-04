import os
import platform
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_CHAT_ID = int(os.getenv("ALLOWED_CHAT_ID"))
SYSTEM_NAME = os.getenv("SYSTEM_NAME").lower()

def get_command(action):
    system = platform.system()
    commands = {
        'Windows': {
            'shutdown': 'shutdown /s /f /t 1',
            'reboot': 'shutdown /r /f /t 1',
            'sleep': 'rundll32.exe powrprof.dll,SetSuspendState 0,1,0'
        },
        'Linux': {
            'shutdown': 'shutdown now',
            'reboot': 'reboot',
            'sleep': 'systemctl suspend'
        },
        'Darwin': {
            'shutdown': 'sudo shutdown -h now',
            'reboot': 'sudo shutdown -r now',
            'sleep': 'pmset sleepnow'
        }
    }
    return commands.get(system, {}).get(action)

async def execute_action(action, delay, update: Update):
    if delay > 0:
        await update.message.reply_text(f"Executing {action} in {delay} seconds...")
        await asyncio.sleep(delay)
    cmd = get_command(action)
    if cmd:
        await update.message.reply_text(f"{action.capitalize()} executed.")
        os.system(cmd)
    else:
        await update.message.reply_text(f"Unsupported action on this system.")

def build_handler(action):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_chat.id != ALLOWED_CHAT_ID:
            return

        args = context.args
        if len(args) < 1:
            await update.message.reply_text("Usage: /{} <target_system> [delay_seconds]".format(action))
            return

        target = args[0].lower()
        delay = int(args[1]) if len(args) > 1 and args[1].isdigit() else 0

        if target == SYSTEM_NAME:
            await execute_action(action, delay, update)
        else:
            await update.message.reply_text(f"Ignored: Target is '{target}', I am '{SYSTEM_NAME}'")
    return handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("shutdown", build_handler("shutdown")))
    app.add_handler(CommandHandler("reboot", build_handler("reboot")))
    app.add_handler(CommandHandler("sleep", build_handler("sleep")))
    app.run_polling()

if __name__ == "__main__":
    main()