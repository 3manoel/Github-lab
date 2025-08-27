const express = require('express');
const ordersController = require('../controllers/ordersController');

const router = express.Router();

// Route for handling new orders
router.post('/neworder', ordersController.handleNewOrder);

module.exports = router;