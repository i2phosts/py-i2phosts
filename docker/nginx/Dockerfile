FROM nginx:stable

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/i2p.conf /etc/nginx/conf.d/
COPY nginx/py-i2phosts.conf /etc/nginx/sites-enabled/
RUN rm -f /etc/nginx/conf.d/default.conf
