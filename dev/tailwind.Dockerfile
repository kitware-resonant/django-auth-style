FROM node:slim

COPY ./tailwind/package.json /opt/django-project/tailwind/package.json
COPY ./tailwind/yarn.lock /opt/django-project/tailwind/yarn.lock

WORKDIR /opt/django-project/tailwind
RUN yarn install --frozen-lockfile
