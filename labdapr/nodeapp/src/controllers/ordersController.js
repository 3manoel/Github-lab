module.exports = {
    newOrder: (req, res) => {
        const orderData = req.body;

        // Log the received order data
        console.log("New order received:", orderData);

        // Here you can add additional logic to process the order
        // For example, validating the order data or saving it to a database

        res.status(201).json({
            message: "Order processed successfully",
            order: orderData
        });
    }
};