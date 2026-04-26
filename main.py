name: Daily Russian Bot
on:
  schedule:
    - cron: '30 2 * * *' # မြန်မာစံတော်ချိန် မနက် ၉ နာရီ
  workflow_dispatch: # ကိုယ်တိုင် လက်နဲ့ စမ်းနှိပ်လို့ရအောင်

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install requests
      - name: Run Script
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
        run: python main.py
