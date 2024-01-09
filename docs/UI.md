## Requirements:
* Node `>=14.15.1`
* Vuecli `@4.4.6`

---
## Node instalation (MacOS)
1. install nvm (Node version manager) usign brew
```
> brew install nvm
```
2. after installation read carefuly log and update your shell configuration
e.g. add the following lines to `.zshrc`
```
export NVM_DIR="$HOME/.nvm"
[ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"  # This loads nvm
```
3. install nodejs using nvm
```
> nvm install 16.13.1
```
4. verify successful installation by
```
> node -v
v16.13.1
```
## Install vue/cli:
```
npm install -g @vue/cli@4.5.15
```
## Project setup (install dependecies)
```
> cd webm_stock/ui
> npm install
```
### Local host configuration
```
/etc/hosts

127.0.0.1        local.webm.party
```

### Compiles and hot-reloads for development
```
> cd ui
> npm run serve
```

### Compiles and minifies for production
```
> cd ui
> npm run build
```

### VueJS - Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
