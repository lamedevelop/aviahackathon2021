FROM nginx:alpine

COPY AR/html /etc/nginx/html
COPY AR/conf.d /etc/nginx/conf.d

EXPOSE 80