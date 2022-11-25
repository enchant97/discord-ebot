# Discord E-Bot
The official discord bot for the Enchanted People server.

> Early in development, not suited for production

## Config
Very WIP...
| Name           | Notes | Default     |
| :------------- | :---- | :---------- |
| DISCORD_TOKEN  |       |             |
|                |       |             |
| ENABLED_COGS   |       |             |
| COMMAND_PREFIX |       | "!e"        |
|                |       |             |
| DB_HOST        |       | "127.0.0.1" |
| DB_PORT        |       | "28015"     |
| DB_DB          |       | "test"      |
| DB_USER        |       | "admin"     |
| DB_PASS        |       | ""          |

### Enabling Cogs
To allow for customisation, cogs are used to add features into the bot.

e.g.

```
ENABLED_COGS=.welcome,.games
```
