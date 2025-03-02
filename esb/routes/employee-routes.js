const express = require('express');
const router = express.Router();

const { getEmployees, createEmployee } = require('../controllers/employee-controller');

router.get('/getemp', getEmployees);
router.post('/create', createEmployee);

module.exports = router;