# docker-compose
主要的后端服务的docker-compose

# 目录说明
```
.
├── README.md
├── emqtt
│   └── docker-compose.yml
├── es
│   ├── docker-compose.yml
│   └── es_data  # 需要chmod 777 es_data
│       └── README.md
├── kafka
│   ├── demo-comsumer.py
│   ├── demo-producer.py
│   ├── docker-compose.yml
│   └── kafka_data  # 需要chmod 777 kafka_data
│       └── README.md
├── mongo_db
│   ├── Dockerfile
│   ├── LICENSE
│   ├── README.md
│   ├── docker-compose.yml
│   └── setup  # 需要chmod 777 setup
│       └── setup.js
├── my_sql
│   ├── docker-compose.yml
│   └── mysql_data  # 需要chmod 777 mysql_data
│       └── README.md
├── nginx
│   ├── conf.d
│   │   └── default.conf
│   ├── docker-compose.yaml
│   └── log  # 需要chmod 777 log
│       ├── access.log
│       └── error.log
├── pg_sql
│   ├── docker-compose.yml
│   └── pg_data  # 需要chmod 777 pg_data
│       └── README.md
└── redis
    ├── docker-compose.yml
    └── redis_data  # 需要chmod 777 redis_data
        └── README.md
```
