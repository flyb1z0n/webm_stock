# build stage
FROM node:12.18.2-alpine as build-stage
WORKDIR /app
COPY ./ui/ .
RUN npm install
RUN npm run build


# production stage
FROM nginx:1.18.0-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]
