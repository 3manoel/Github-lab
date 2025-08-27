const express = require('express');
const ordersController = require('../controllers/ordersController');

const router = express.Router();

// Route for handling new orders
// use the function name actually exported by the controller (newOrder)
router.post('/neworder', ordersController.newOrder);

module.exports = router;