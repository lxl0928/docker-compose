db = db.getSiblingDB('acms_webhooks');

db.createUser(
    {
        user: "root",
        pwd: "123456",
        roles: [
            { role: "dbOwner", db: "acms_webhooks"}
        ]
    },
);
db.createCollection("newCollection_test");



db = db.getSiblingDB('antelope_data');
db.createUser(
    {
        user: "root",
        pwd: "123456",
        roles: [
            { role: "dbOwner", db: "antelope_data"}
        ]
    },
);
