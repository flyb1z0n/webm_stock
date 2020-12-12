# build stage
FROM node:14.15.1-alpine as build-stage
WORKDIR /app
COPY ./ui/ .
RUN npm install
RUN npm run build


# production stage
FROM nginx:1.18.0-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
