//import { testData } from "./testData.mjs";

const express = require("express");
const app = express();
const parse = require('csv-parse');

const port = process.env.PORT || 8080;

// controller logic
const download = (req, res) => {

    res.setHeader("Content-Type", "text/csv");
    res.setHeader("Content-Disposition", "attachment; filename=test.csv");
    res.status(200).end(csvData);
};


app.listen(port, ()=> {
    console.log(`Function has been fired on ${port}`);
});

app.get("/products.csv", async (req, res) => {

    // read CSV file as string
    
    // convert to string to CSV

    // submit as csv file
    res.setHeader("Content-Type", "text/csv");
    res.setHeader("Content-Disposition", "attachment; filename=productTest.csv");
    res.status(200).end('testData');
    console.log('At product download csv route!');
});