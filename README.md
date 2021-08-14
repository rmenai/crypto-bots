<br />
<p align="center">
  <a href="https://github.com/rmenai/python-structure">
    <img src="https://icons.iconarchive.com/icons/cjdowner/cryptocurrency-flat/1024/Bitcoin-BTC-icon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Crypto Bots</h3>

  <p align="center">
    Sidebar crypto discord bots
    <br />
    <a href="https://github.com/rmenai/crypto-bots/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rmenai/crypto-bots">View Demo</a>
    ·
    <a href="https://github.com/rmenai/crypto-bots/issues/new?assignees=&labels=&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="https://github.com/rmenai/crypto-bots/issues/new?assignees=&labels=&template=feature_request.md&title=">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#environment-variables">Environment Variables</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

Discord crypto bots showing:
* The price, the volume and the market cap of a coin.
* The ethereum gas price.

<img src="https://i.imgur.com/qgF1VYQ.png" height="200">

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites
You can easily run the project using Docker. The requirements are:
* [Docker CE](https://docs.docker.com/engine/install/)

Or you can install it manually

* [Python](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/)

### Installation
With Docker:
1. Pull the image
   ```shell
   docker pull ghcr.io/rmenai/crypto-bots:latest
   ```
Or manually:
1. Clone the repo
   ```shell
   git clone https://github.com/rmenai/crypto-bots.git
   ```
2. Install the dependencies
   ```shell
   poetry install
   ```

<!-- USAGE EXAMPLES -->


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file or in docker-compose.yml


| Discord bots        | Description                          |
|---------------------|--------------------------------------|
| PRICE_BOT_TOKEN     | The **price** discord bot token      |
| VOLUME_BOT_TOKEN    | The **volume** discord bot token     |
| CAP_BOT_TOKEN       | The **market cap** discord bot token |
| HOLDERS_BOT_TOKEN   | The **holders** discord bot token    |
| GAS_BOT_TOKEN       | The **eth gas** discord bot token    |

* These are not all required, you just need at least one or more.


| APIs           | Description                                                            |
|----------------|------------------------------------------------------------------------|
| NOMICS_API_KEY   | Your token of the [nomics API](https://nomics.com/)                    |
| ETH_GAS_API_KEY  | Your token of the [ethgasstation API](https://ethgasstation.info/)     |

* `NOMICS_API_KEY` is required.
* `ETH_GAS_API_KEY` is only required for the eth gas bot.


| Settings       | Description                      |
|----------------|----------------------------------|
| NOMICS_COIN_ID | The nomics id of the coin        |
| DELAY          | The delay between status refresh |
| DEBUG          | The volume discord bot token     |

* `NOMICS_COIN_ID` is required.
* `DELAY` defaults to 5 seconds.

## Usage

Now you are done! You can start your project and run it using

```shell
poetry run task start
```

or if you choose Docker
```shell
docker run ghcr.io/rmenai/crypto-bots:latest
```

## Contributing

See [CONTRIBUTING.md](https://github.com/rmenai/python-structure/blob/main/CONTRIBUTING.md) for ways to get started.

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](https://github.com/rmenai/python-structure/blob/main/LICENSE) for more
information.


<!-- CONTACT -->

## Contact

Menai Rami - [@menai_rami](https://twitter.com/menai_rami) - rami.menai@outlook.com
