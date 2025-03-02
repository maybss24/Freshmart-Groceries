const axios = require('axios');

const getEmployees = async (req, res) => {
    try {
        const response = await axios.get(`${process.env.EMPLOYEE_SERVICE}/employee/all`);
        res.status(200).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ 
                success: false, 
                message: `Failed to fetch employees: ${error.message}` 
            });
        }
    }
};

const createEmployee = async (req, res) => {
    try {
        const response = await axios.post(`${process.env.EMPLOYEE_SERVICE}/employee/create`, req.body);
        res.status(201).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ 
                success: false, 
                message: `Failed to create employee: ${error.message}` 
            });
        }
    }
};

module.exports = { getEmployees, createEmployee };