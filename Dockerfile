FROM node:20-bullseye

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/open-swe

COPY package.json yarn.lock turbo.json tsconfig.json langgraph.json ./
COPY apps ./apps
COPY packages ./packages

RUN yarn install --frozen-lockfile
RUN yarn build

EXPOSE 2024
CMD ["yarn","workspace","@open-swe/agent","dev"]
