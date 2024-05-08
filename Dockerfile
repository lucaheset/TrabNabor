FROM wordpress:5.4.2-php7.2-apache

# Copia o script wait-for-it.sh para o contêiner
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh

# Torna o script executável
RUN chmod +x /usr/local/bin/wait-for-it.sh