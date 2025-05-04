# Telegram Remote Power Control Bot

This Python bot allows you to remotely **shutdown**, **reboot**, or **put to sleep** multiple systems (Windows, Linux, macOS) via Telegram commands.

## 🔧 Features

- Cross-platform support: **Windows**, **Linux**, and **macOS**
- One Telegram bot, multiple systems (each with unique `SYSTEM_NAME`)
- Command delay support (in **seconds**, no `m` or `h` required)
- Safe command execution via whitelisted `ALLOWED_CHAT_ID`
- Environment configuration via `.env` file

---

## 📦 Setup

### 0. Requirements

- Python 3.10+
- Telegram Token
- Telegram Chat-ID

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create `.env` File (per machine)

```
BOT_TOKEN=your_telegram_bot_token
ALLOWED_CHAT_ID=123456789
SYSTEM_NAME=macbook  # Choose a unique name per system
```

### 3. Run the Bot

```bash
python telegram_power_control.py
```

or use 

---

## 💬 Telegram Command Format

Use the following command syntax:

```
/shutdown <system_name> [delay_seconds]
/reboot <system_name> [delay_seconds]
/sleep <system_name>
```

### Examples:

- `/shutdown macbook 600` → Shutdown "macbook" in 10 minutes
- `/reboot server01 0` → Reboot "server01" immediately
- `/sleep mediahub` → Put "mediahub" to sleep immediately

---

## 🔐 Security

- Only commands from the Telegram `ALLOWED_CHAT_ID` are accepted.
- Each system only responds to commands that match its own `SYSTEM_NAME`.

---

## 🚀 Optional: Run on Startup

Set this script to run at boot:
- **Linux/macOS**: Use `systemd` or `launchctl`
- **Windows**: Use Task Scheduler

---

## 📄 License

python package python-telegram-bot uses LGPLv3 and python-dotenv MIT

feel free to make what you think you can do with the code.