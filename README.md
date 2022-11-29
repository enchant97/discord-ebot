# Discord E-Bot
E-Bot aims to be a general purpose discord bot. It is also the official bot for the Enchanted People server.

> Early in development, not suited for production

## Features
- Customisable
- Works over multiple servers (guilds)
- Data stored using [RethinkDB](https://rethinkdb.com/) a NoSQL database
- Togglable features
    - Welcome messages
    - Member Profile
      - Roles
    - Idea-Box
    - Games
        - Coin-flip
        - Random number generator
    - Admin (configure certain features)


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
To allow for customisation, cogs are used to add and remove features. By default all features apart from "testing" are enabled.

e.g.

```
ENABLED_COGS=.welcome,.games
```
