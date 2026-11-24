# last-text

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/nmlyz/last-text/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/nmlyz/last-text/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

A tiny program that writes one last text message — the final words a
phone sends as its battery hits 1 percent — to a text file. The
message is a single line of 91 characters: the phone lists what it
survived (three drops, one toilet, two updates) and names what
finally killed it.

## Run it

```sh
python3 main.py
```

It writes the message to `/output/entry.txt` (`OUTPUT_DIR` overrides
the directory). Running it twice produces byte-identical output.
