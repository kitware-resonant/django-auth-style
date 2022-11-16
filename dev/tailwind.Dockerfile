FROM node:slim

COPY ./package.json /opt/django-project/package.json
COPY ./yarn.lock /opt/django-project/yarn.lock

WORKDIR /opt/django-project
RUN yarn install --frozen-lockfile
