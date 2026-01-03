name: Keep Alive

on:
  schedule:
    - cron: "*/10 * * * *"   # every 10 minutes
  workflow_dispatch:        # allows manual run

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt || true

      - name: Run keep-alive script
        run: python keep_alive.py
