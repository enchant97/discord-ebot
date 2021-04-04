# Discord Ebot
A simple easy to use discord bot available for everyone and free to use.

> Please take note that this project is a work in progress, so will have more features later.

## Features
- Built for Python 3.9+
- Lightweight, so should be able to run on a Raspberry Pi 3 or later
- Includes a Dockerfile for easy deployment
- Store data in database
- Access same data across multiple servers running the bot
- Games
    - Coin Flip (Heads or Tails)
- Economy (based on credits)
    - Work
    - Gamble

## Install
1. Get/Generate your Discord Bot token
2. Install required python packages
3. Create .env file (or pass environment
variables on launch) with configs for server
4. Run the bot

## Configuration Variables
| Name        |Desc                          |Default                    |
|:------------|:-----------------------------|:--------------------------|
| DB_URI      | Where the database should be | "sqlite://:memory:"       |
| LOG_LEVEL   | What log level to display    | "INFO"                    |
| PREFIXES    | What will trigger the bot    | ["!"]                     |
| DESCRIPTION | A description of the bot     | (to long to display here) |
| TOKEN       | The discord bot token        |                           |

## Thanks To
- EvieePy for [cogs example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) &
[error handling example](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612)

## License
Copyright (C) 2021  Leo Spratt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
