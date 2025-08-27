module.exports = {
    port: process.env.PORT || 3000,
    db: {
        host: process.env.DB_HOST || 'localhost',
        port: process.env.DB_PORT || 27017,
        name: process.env.DB_NAME || 'orders_db'
    },
    api: {
        version: '1.0',
        baseUrl: '/api'
    },
    logging: {
        level: process.env.LOG_LEVEL || 'info'
    }
};