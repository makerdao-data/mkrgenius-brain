# mkrGenius Brain

A fork of yGenius for MakerDAO

Marco's write-up for yGenius: https://medium.com/@marcoworms/ygenius-chat-with-yearn-efa17d3f0ec8  
Frontend Source: https://github.com/yearn/ygenius-webui

## Configuration

- create `.env` file with `OPENAI_API_KEY` for the api key provided by OpenAI and `INDEX_DIR` for the location of the `index.json` file.

## Run

### Local

You can always run Docker locally, please see below.

Run `python main_local.py`

### Hosted

Install docker and docker-compose and run:
`docker-compose up -d`

Whenever making changes to the code base, you need to rebuild a new docker image:
`docker-compose build`

## Usage

`curl "http://localhost:5001/ask?history=&query=what%20is%20makerdao%20%3F"`

## Training data
- training-data/collateral: https://github.com/makerdao/mcd-collateral.git
- training-data/endgame:    https://github.com/makerdao/endgame-docs.git
- training-data/governance: https://github.com/makerdao/governance-manual.git
- training-data/mips:       https://github.com/makerdao/mips.git
- training-data/mcd:        https://github.com/makerdao/mcd-docs-content.git
- training-data/community:  https://github.com/makerdao/community.git