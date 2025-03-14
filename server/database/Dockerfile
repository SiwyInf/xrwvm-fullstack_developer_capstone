FROM node:18.12.1-bullseye-slim

# Aktualizacja npm
RUN npm install -g npm@9.1.3

# Kopiowanie plików aplikacji
COPY package.json .
COPY app.js .
COPY review.js .
COPY dealership.js .
COPY data/dealerships.json .
COPY data/reviews.json .

# Instalacja zależności
RUN npm install

# Ekspozycja portu
EXPOSE 3030

# Uruchamianie aplikacji
CMD [ "node", "app.js" ]
