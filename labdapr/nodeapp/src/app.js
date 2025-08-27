const express = require('express');
const bodyParser = require('body-parser');
const ordersRoutes = require('./routes/orders');

const app = express();

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/api/orders', ordersRoutes);

module.exports = app;