# desafio-tecnico-python-pleno

Desáfio Técnico para vaga Python na Delivery IT


## Tecnologias

#### Docker + Django + Nginx + PostgresSQL + SSL ### 



## Deploy local

### **Instale o docker-compose no seu computador e execute:** ### 

``` 
docker-compose -f docker-compose-dev.yml up --build
```

- A aplicação pode ser acessada em 0.0.0.0:8000

___ 

## Deploy em produção

### **Altere os valores em env_files nos arquivos *-prod e execute:** ### 

``` 
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-prod.yml up -d
```

---

## API

### **A API da aplicação pode ser acessada  em** ### 

``` 
0.0.0.0:8000/docs
```

---

## Demo online



``` 
https://deliveryit.growtechnologies.com.br/
```

---