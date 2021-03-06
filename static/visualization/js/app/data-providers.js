(function (_) {

    var app = angular.module('dataProviders', ['array-utils-module']);

    app.factory('fuzzyApi', ['$http', function ($http) {

        const url = '';//http://bartek887.pythonanywhere.com';

        const calculateSimilarity = function (requestBody) {
            return $http.post(`${url}/fuzzy/similarity`, requestBody);
        };

        const getAggregators = function () {
            return $http.get(`${url}/fuzzy/aggregators`);
        };

        const getAvailableDataSets = function () {
            return $http.get(`${url}/fuzzy/data-sets`);
        };

        const getDataSet = function (key) {
            return $http.get(`${url}/fuzzy/data-sets/${key}`);
        };

        return {
            calculateSimilarity,
            getAggregators,
            getAvailableDataSets,
            getDataSet
        }
    }]);

    const MAIN_EXAMPLE_SETS = {
        setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
        setB: [0, 0, 0.9585, 0, 0, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
    };

    const EXAMPLES = [
        {
            setA: [0.754081278931, 0.7437, 0.698, 0.7241, 0.7196, 0.7019, 0.7005, 0.7309, 0.7122, 0.7162, 0.7367, 0.7407, 0.7647, 0.7167, 0.6898, 0.6857, 0.6403, 0.6349, 0.6827, 0.669],
            setB: [0.754081278931, 0.7437, 0.698, 0.7241, 0.7196, 0.7019, 0.7005, 0.7309, 0.7122, 0.7162, 0.7367, 0.7407, 0.7647, 0.7167, 0.6898, 0.6857, 0.6403, 0.6349, 0.6827, 0.669],

        },
        {
            setA: [0.754081278931, 0.7437, 0.698, 0.7241, 0.7196, 0.7019, 0.7005, 0.7309, 0.7122, 0.7162, 0.7367, 0.7407, 0.7647, 0.7167, 0.6898, 0.6857, 0.6403, 0.6349, 0.6827, 0.669],
            setB: [0.754081278931, 0.7437, 0.698, 0.7241, 0.7196, 0.7019, 0.7005, 0.7309, 0.7122, 0.7162, 0.7367, 0.7407, 0.7647, 0.7167, 0.6898, 0.6857, 0.6403, 0.6349, 0.6827, 0.669],

        },
        //large random sets with values lower than 0.5
        {
            setA: [0.287230495809, 0.2871, 0.267, 0.2909, 0.3189, 0.3686, 0.4004, 0.3717, 0.3296, 0.3415, 0.3123, 0.3219, 0.3052, 0.314, 0.3124, 0.2977, 0.2986, 0.2999, 0.3059, 0.2976, 0.3179, 0.2837, 0.3267, 0.3135, 0.2737, 0.2723, 0.2417, 0.2094, 0.2364, 0.1895, 0.2274, 0.1864, 0.1475, 0.1725, 0.1655, 0.1392, 0.1103, 0.0781, 0.1044, 0.06, 0.104, 0.1256, 0.1281, 0.0963, 0.0633, 0.0158, 0.0282, 0.0211, 0.0617, 0.0757],
            setB: [0.287994299689, 0.2556, 0.2201, 0.1819, 0.2137, 0.1945, 0.1544, 0.1553, 0.1945, 0.1522, 0.1443, 0.1837, 0.1875, 0.2343, 0.2276, 0.2489, 0.2624, 0.2953, 0.2944, 0.2547, 0.2636, 0.216, 0.2421, 0.1997, 0.2258, 0.2735, 0.2907, 0.3237, 0.2958, 0.2993, 0.2674, 0.2457, 0.2095, 0.2426, 0.2183, 0.1913, 0.1996, 0.183, 0.1863, 0.1979, 0.2058, 0.235, 0.2379, 0.2119, 0.1755, 0.1312, 0.1438, 0.1501, 0.173, 0.1311],
        },
        {
            setA: [0.287230495809, 0.2871, 0.267, 0.2909, 0.3189, 0.3686, 0.4004, 0.3717, 0.3296, 0.3415, 0.3123, 0.3219, 0.3052, 0.314, 0.3124, 0.2977, 0.2986, 0.2999, 0.3059, 0.2976, 0.3179, 0.2837, 0.3267, 0.3135, 0.2737, 0.2723, 0.2417, 0.2094, 0.2364, 0.1895, 0.2274, 0.1864, 0.1475, 0.1725, 0.1655, 0.1392, 0.1103, 0.0781, 0.1044, 0.06, 0.104, 0.1256, 0.1281, 0.0963, 0.0633, 0.0158, 0.0282, 0.0211, 0.0617, 0.0757],
            setB: [0.287994299689, 0.2556, 0.2201, 0.1819, 0.2137, 0.1945, 0.1544, 0.1553, 0.1945, 0.1522, 0.1443, 0.1837, 0.1875, 0.2343, 0.2276, 0.2489, 0.2624, 0.2953, 0.2944, 0.2547, 0.2636, 0.216, 0.2421, 0.1997, 0.2258, 0.2735, 0.2907, 0.3237, 0.2958, 0.2993, 0.2674, 0.2457, 0.2095, 0.2426, 0.2183, 0.1913, 0.1996, 0.183, 0.1863, 0.1979, 0.2058, 0.235, 0.2379, 0.2119, 0.1755, 0.1312, 0.1438, 0.1501, 0.173, 0.1311],
        },
        //small sets and it's rescaled version
        {
            setA: [0.29905197377, 0.3366, 0.239, 0.1556, 0.2302, 0.3228, 0.2769, 0.3028, 0.3538, 0.3328],
            setB: [0.59810394754, 0.6732, 0.478, 0.3112, 0.4604, 0.6456, 0.5538, 0.6056, 0.7076, 0.6656],
        },
        {
            setA: [0.29905197377, 0.3366, 0.239, 0.1556, 0.2302, 0.3228, 0.2769, 0.3028, 0.3538, 0.3328],
            setB: [0.59810394754, 0.6732, 0.478, 0.3112, 0.4604, 0.6456, 0.5538, 0.6056, 0.7076, 0.6656],
        },
        //triangular and second triangular resized in y by 2
        {
            setA: [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0],
            setB: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0],
        },
        {
            setA: [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0],
            setB: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0],
        },
        //same shape, rescaled, triangular, small
        {
            setA: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0],
            setB: [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0],
        },
        {
            setA: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0],
            setB: [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0],
        },
        {
            setA: [0.1, 0.5, 0.1],
            setB: [0.4, 0.9, 0.4],
        },
        {
            setA: [0.1, 0.5, 0.1],
            setB: [0.4, 0.9, 0.4],
        },
        {
            setA: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
            setB: [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
        },
        {
            setA: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
            setB: [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
        },
        {
            setA: [0.0, 0.0025, 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02, 0.0225, 0.025, 0.0275, 0.03, 0.0325, 0.035, 0.0375, 0.04, 0.0425, 0.045, 0.0475, 0.05, 0.0525, 0.055, 0.0575, 0.06, 0.0625, 0.065, 0.0675, 0.07, 0.0725, 0.075, 0.0775, 0.08, 0.0825, 0.085, 0.0875, 0.09, 0.0925, 0.095, 0.0975, 0.1, 0.1025, 0.105, 0.1075, 0.11, 0.1125, 0.115, 0.1175, 0.12, 0.1225, 0.125, 0.1275, 0.13, 0.1325, 0.135, 0.1375, 0.14, 0.1425, 0.145, 0.1475, 0.15, 0.1525, 0.155, 0.1575, 0.16, 0.1625, 0.165, 0.1675, 0.17, 0.1725, 0.175, 0.1775, 0.18, 0.1825, 0.185, 0.1875, 0.19, 0.1925, 0.195, 0.1975, 0.2, 0.2025, 0.205, 0.2075, 0.21, 0.2125, 0.215, 0.2175, 0.22, 0.2225, 0.225, 0.2275, 0.23, 0.2325, 0.235, 0.2375, 0.24, 0.2425, 0.245, 0.2475, 0.25, 0.2525, 0.255, 0.2575, 0.26, 0.2625, 0.265, 0.2675, 0.27, 0.2725, 0.275, 0.2775, 0.28, 0.2825, 0.285, 0.2875, 0.29, 0.2925, 0.295, 0.2975, 0.3, 0.3025, 0.305, 0.3075, 0.31, 0.3125, 0.315, 0.3175, 0.32, 0.3225, 0.325, 0.3275, 0.33, 0.3325, 0.335, 0.3375, 0.34, 0.3425, 0.345, 0.3475, 0.35, 0.3525, 0.355, 0.3575, 0.36, 0.3625, 0.365, 0.3675, 0.37, 0.3725, 0.375, 0.3775, 0.38, 0.3825, 0.385, 0.3875, 0.39, 0.3925, 0.395, 0.3975, 0.4, 0.4025, 0.405, 0.4075, 0.41, 0.4125, 0.415, 0.4175, 0.42, 0.4225, 0.425, 0.4275, 0.43, 0.4325, 0.435, 0.4375, 0.44, 0.4425, 0.445, 0.4475, 0.45, 0.4525, 0.455, 0.4575, 0.46, 0.4625, 0.465, 0.4675, 0.47, 0.4725, 0.475, 0.4775, 0.48, 0.4825, 0.485, 0.4875, 0.49, 0.4925, 0.495, 0.4975, 0.5, 0.4975, 0.495, 0.4925, 0.49, 0.4875, 0.485, 0.4825, 0.48, 0.4775, 0.475, 0.4725, 0.47, 0.4675, 0.465, 0.4625, 0.46, 0.4575, 0.455, 0.4525, 0.45, 0.4475, 0.445, 0.4425, 0.44, 0.4375, 0.435, 0.4325, 0.43, 0.4275, 0.425, 0.4225, 0.42, 0.4175, 0.415, 0.4125, 0.41, 0.4075, 0.405, 0.4025, 0.4, 0.3975, 0.395, 0.3925, 0.39, 0.3875, 0.385, 0.3825, 0.38, 0.3775, 0.375, 0.3725, 0.37, 0.3675, 0.365, 0.3625, 0.36, 0.3575, 0.355, 0.3525, 0.35, 0.3475, 0.345, 0.3425, 0.34, 0.3375, 0.335, 0.3325, 0.33, 0.3275, 0.325, 0.3225, 0.32, 0.3175, 0.315, 0.3125, 0.31, 0.3075, 0.305, 0.3025, 0.3, 0.2975, 0.295, 0.2925, 0.29, 0.2875, 0.285, 0.2825, 0.28, 0.2775, 0.275, 0.2725, 0.27, 0.2675, 0.265, 0.2625, 0.26, 0.2575, 0.255, 0.2525, 0.25, 0.2475, 0.245, 0.2425, 0.24, 0.2375, 0.235, 0.2325, 0.23, 0.2275, 0.225, 0.2225, 0.22, 0.2175, 0.215, 0.2125, 0.21, 0.2075, 0.205, 0.2025, 0.2, 0.1975, 0.195, 0.1925, 0.19, 0.1875, 0.185, 0.1825, 0.18, 0.1775, 0.175, 0.1725, 0.17, 0.1675, 0.165, 0.1625, 0.16, 0.1575, 0.155, 0.1525, 0.15, 0.1475, 0.145, 0.1425, 0.14, 0.1375, 0.135, 0.1325, 0.13, 0.1275, 0.125, 0.1225, 0.12, 0.1175, 0.115, 0.1125, 0.11, 0.1075, 0.105, 0.1025, 0.1, 0.0975, 0.095, 0.0925, 0.09, 0.0875, 0.085, 0.0825, 0.08, 0.0775, 0.075, 0.0725, 0.07, 0.0675, 0.065, 0.0625, 0.06, 0.0575, 0.055, 0.0525, 0.05, 0.0475, 0.045, 0.0425, 0.04, 0.0375, 0.035, 0.0325, 0.03, 0.0275, 0.025, 0.0225, 0.02, 0.0175, 0.015, 0.0125, 0.01, 0.0075, 0.005, 0.0025, 0.0],
            setB: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
        },
        {
            setA: [0.0, 0.0025, 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02, 0.0225, 0.025, 0.0275, 0.03, 0.0325, 0.035, 0.0375, 0.04, 0.0425, 0.045, 0.0475, 0.05, 0.0525, 0.055, 0.0575, 0.06, 0.0625, 0.065, 0.0675, 0.07, 0.0725, 0.075, 0.0775, 0.08, 0.0825, 0.085, 0.0875, 0.09, 0.0925, 0.095, 0.0975, 0.1, 0.1025, 0.105, 0.1075, 0.11, 0.1125, 0.115, 0.1175, 0.12, 0.1225, 0.125, 0.1275, 0.13, 0.1325, 0.135, 0.1375, 0.14, 0.1425, 0.145, 0.1475, 0.15, 0.1525, 0.155, 0.1575, 0.16, 0.1625, 0.165, 0.1675, 0.17, 0.1725, 0.175, 0.1775, 0.18, 0.1825, 0.185, 0.1875, 0.19, 0.1925, 0.195, 0.1975, 0.2, 0.2025, 0.205, 0.2075, 0.21, 0.2125, 0.215, 0.2175, 0.22, 0.2225, 0.225, 0.2275, 0.23, 0.2325, 0.235, 0.2375, 0.24, 0.2425, 0.245, 0.2475, 0.25, 0.2525, 0.255, 0.2575, 0.26, 0.2625, 0.265, 0.2675, 0.27, 0.2725, 0.275, 0.2775, 0.28, 0.2825, 0.285, 0.2875, 0.29, 0.2925, 0.295, 0.2975, 0.3, 0.3025, 0.305, 0.3075, 0.31, 0.3125, 0.315, 0.3175, 0.32, 0.3225, 0.325, 0.3275, 0.33, 0.3325, 0.335, 0.3375, 0.34, 0.3425, 0.345, 0.3475, 0.35, 0.3525, 0.355, 0.3575, 0.36, 0.3625, 0.365, 0.3675, 0.37, 0.3725, 0.375, 0.3775, 0.38, 0.3825, 0.385, 0.3875, 0.39, 0.3925, 0.395, 0.3975, 0.4, 0.4025, 0.405, 0.4075, 0.41, 0.4125, 0.415, 0.4175, 0.42, 0.4225, 0.425, 0.4275, 0.43, 0.4325, 0.435, 0.4375, 0.44, 0.4425, 0.445, 0.4475, 0.45, 0.4525, 0.455, 0.4575, 0.46, 0.4625, 0.465, 0.4675, 0.47, 0.4725, 0.475, 0.4775, 0.48, 0.4825, 0.485, 0.4875, 0.49, 0.4925, 0.495, 0.4975, 0.5, 0.4975, 0.495, 0.4925, 0.49, 0.4875, 0.485, 0.4825, 0.48, 0.4775, 0.475, 0.4725, 0.47, 0.4675, 0.465, 0.4625, 0.46, 0.4575, 0.455, 0.4525, 0.45, 0.4475, 0.445, 0.4425, 0.44, 0.4375, 0.435, 0.4325, 0.43, 0.4275, 0.425, 0.4225, 0.42, 0.4175, 0.415, 0.4125, 0.41, 0.4075, 0.405, 0.4025, 0.4, 0.3975, 0.395, 0.3925, 0.39, 0.3875, 0.385, 0.3825, 0.38, 0.3775, 0.375, 0.3725, 0.37, 0.3675, 0.365, 0.3625, 0.36, 0.3575, 0.355, 0.3525, 0.35, 0.3475, 0.345, 0.3425, 0.34, 0.3375, 0.335, 0.3325, 0.33, 0.3275, 0.325, 0.3225, 0.32, 0.3175, 0.315, 0.3125, 0.31, 0.3075, 0.305, 0.3025, 0.3, 0.2975, 0.295, 0.2925, 0.29, 0.2875, 0.285, 0.2825, 0.28, 0.2775, 0.275, 0.2725, 0.27, 0.2675, 0.265, 0.2625, 0.26, 0.2575, 0.255, 0.2525, 0.25, 0.2475, 0.245, 0.2425, 0.24, 0.2375, 0.235, 0.2325, 0.23, 0.2275, 0.225, 0.2225, 0.22, 0.2175, 0.215, 0.2125, 0.21, 0.2075, 0.205, 0.2025, 0.2, 0.1975, 0.195, 0.1925, 0.19, 0.1875, 0.185, 0.1825, 0.18, 0.1775, 0.175, 0.1725, 0.17, 0.1675, 0.165, 0.1625, 0.16, 0.1575, 0.155, 0.1525, 0.15, 0.1475, 0.145, 0.1425, 0.14, 0.1375, 0.135, 0.1325, 0.13, 0.1275, 0.125, 0.1225, 0.12, 0.1175, 0.115, 0.1125, 0.11, 0.1075, 0.105, 0.1025, 0.1, 0.0975, 0.095, 0.0925, 0.09, 0.0875, 0.085, 0.0825, 0.08, 0.0775, 0.075, 0.0725, 0.07, 0.0675, 0.065, 0.0625, 0.06, 0.0575, 0.055, 0.0525, 0.05, 0.0475, 0.045, 0.0425, 0.04, 0.0375, 0.035, 0.0325, 0.03, 0.0275, 0.025, 0.0225, 0.02, 0.0175, 0.015, 0.0125, 0.01, 0.0075, 0.005, 0.0025, 0.0],
            setB: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0],
        },
    ];

    const configureExamples = (method, configurations) =>
        EXAMPLES.map((example, index) => _.extend(example, method, configurations[index]));

    app.controller("JaccardController", function () {

        const METHOD = {
            'method': 'jaccard-index'
        };

        const CONFIGS = [
            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "average",
                "gamma": 0,

            },
            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "sup",
                "gamma": 0,

            },

            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "sup",
                "gamma": 0,
            },

            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "sup",
                "gamma": 0,
            },

            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "average",
                "gamma": 0,

            },
            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "sup",
                "gamma": 0,

            },

            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "sup",
                "gamma": 0,
            },

            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "sup",
                "gamma": 0,
            },

            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "average",
                "gamma": 0,

            },
            {
                "alpha": 1,
                "beta": 1,
                "evaluator": "sup",
                "gamma": 0,

            },

            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 0.5,
                "beta": 0.5,
                "evaluator": "sup",
                "gamma": 0,
            },

            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "average",
                "gamma": 0,
            },
            {
                "alpha": 1,
                "beta": 0,
                "evaluator": "sup",
                "gamma": 0,
            },
        ];

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            "alpha": 1,
            "beta": 1,
            "evaluator": "average",
            "gamma": 0,
        });

        this.examples = configureExamples(METHOD, CONFIGS);
    });

    app.controller("SimplifiedJaccardController", function () {

        const METHOD = {
            'method': 'simplified-jaccard-index'
        };

        const CONFIGS = [
            {
                aggregator: "average",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "average",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "average",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },

            {
                aggregator: "maximum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "maximum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "maximum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },

            {
                aggregator: "minimum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "minimum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "minimum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },

            {
                aggregator: "average",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "average",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "average",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },

            {
                aggregator: "maximum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "maximum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "maximum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },

            {
                aggregator: "minimum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "minimum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "minimum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },
        ];

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            aggregator: 'average',
            tknorm: 'maxiumum',
            tnorm: 'minimum'
        });

        this.examples = configureExamples(METHOD, CONFIGS);
    });

    app.controller("MinkowskiController", function () {

        const METHOD = {
            method: 'minkowski'
        };

        const createConfig = function (rValue) {
            return {
                r: rValue
            };
        };

        const CONFIGS = [
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(1),
            createConfig(2),
            createConfig(2),
            createConfig(200)
        ];

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            r: 2
        });

        this.examples = configureExamples(METHOD, CONFIGS);
    });

    app.controller("AngularDistanceController", function () {

        const METHOD = {
            method: 'angular-distance'
        };

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD);

        //no configs needed here, no configurable parameters required for this method
        this.examples = configureExamples(METHOD, [])
    });

    app.controller("ImplicationSimilarityController", function () {

        const METHOD = {
            method: 'implication-similarity'
        };

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            aggregator: 'average',
            tnorm: 'minimum',
            implication: 'maximum'
        });


        const CONFIGS = [
            {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'maximum',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'

            },

            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'
            },
            {
                aggregator: 'maximum',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'
            },
            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'
            },
            {
                aggregator: 'minimum',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'
            },

            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                aggregator: 'maximum',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                aggregator: 'minimum',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'
            },

            {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'maximum',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'

            },
        ];

        this.examples = configureExamples(METHOD, CONFIGS);
        ;
    });

    app.controller("ComparisonDataProvider", ['$scope', 'arrayUtils', 'fuzzyApi', function ($scope, arrayUtils, fuzzyApi) {

        const comparisonCtrl = this;

        this.chartConfig = {
            data: [
                [],
                []
            ],
            colors: [
                { // grey
                    fill: false,
                    backgroundColor: 'rgba(148,159,177,0.2)',
                    pointBackgroundColor: 'rgba(148,159,177,1)',
                    pointHoverBackgroundColor: 'rgba(148,159,177,1)',
                    borderColor: 'rgba(148,159,177,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(148,159,177,0.8)'
                },
                { // dark grey
                    fill: false,
                    backgroundColor: 'rgba(77,83,96,0.2)',
                    pointBackgroundColor: 'rgba(77,83,96,1)',
                    pointHoverBackgroundColor: 'rgba(77,83,96,1)',
                    borderColor: 'rgba(77,83,96,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(77,83,96,0.8)'
                },
                { // blue
                    fill: false,
                    backgroundColor: 'rgba(0, 0, 255,0.2)',
                    pointBackgroundColor: 'rgba(0, 0, 255,1)',
                    pointHoverBackgroundColor: 'rgba(0, 0, 255,1)',
                    borderColor: 'rgba(0, 0, 255,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0, 0, 255,0.8)'
                },
                { // dark green
                    fill: false,
                    backgroundColor: 'rgba(0,100,0,0.2)',
                    pointBackgroundColor: 'rgba(0,100,0,1)',
                    pointHoverBackgroundColor: 'rgba(0,100,0,1)',
                    borderColor: 'rgba(0,100,0,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0,100,0,0.8)'
                },
                { // dark blue
                    fill: false,
                    backgroundColor: 'rgba(0, 0, 139,0.2)',
                    pointBackgroundColor: 'rgba(0, 0, 139,1)',
                    pointHoverBackgroundColor: 'rgba(0, 0, 139,1)',
                    borderColor: 'rgba(0, 0, 139,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0, 0, 139,0.8)'
                },
            ],
            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            autoSkip: true
                        },
                        gridLines: {
                            drawOnChartArea: false
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Możliwe wartości atrybutu'
                        }
                    }],
                    yAxes: [{
                        gridLines: {
                            drawOnChartArea: false
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Możliwe wartości atrybutu'
                        }
                    }]
                },
                elements: {
                    line: {
                        borderWidth: 4
                    }
                }
            }
        };

        this.selectedDataSetKey = '';

        this.similarityCalculationResults = {};

        this.summaryChartConfig = {
            series: ['Sumary'],
            data: [],
            labels: [],
            options: {
                scales: {
                    yAxes: [{
                        type: 'bar',
                        display: true,
                        ticks: {
                            autoSkip: false,
                        }
                    }]
                }
            }
        };

        this.configurations = [];

        this.rawFuzzySets = {
            setA: "0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0",
            setB: "0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0"
        };

        this.configurationsWithoutSets = [
            {
                method: "implication-similarity",
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'
            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'

            },
            {
                method: "minkowski",
                r: 2

            },
            {
                method: "minkowski",
                r: 2

            },
            {
                method: "minkowski",
                r: 2
            },
        ];

        this.createValidConfigurations = function () {
            const setA = arrayUtils.stringToArray(this.rawFuzzySets.setA);
            const setB = arrayUtils.stringToArray(this.rawFuzzySets.setB);

            comparisonCtrl.summaryChartConfig.data = [];
            comparisonCtrl.summaryChartConfig.labels = [];

            this.chartConfig = _.extend(this.chartConfig, {
                data: [
                    setA,
                    setB
                ],
                labels: _.range(Math.max(setA.length, setB.length))
            });

            const configurations = [];
            _.each(this.configurationsWithoutSets, (value, index) => {
                const copied = _.extend({}, value);
                copied.setA = setA;
                copied.setB = setB;
                copied.id = index;
                configurations.push(copied);
            });
            return configurations;
        };

        this.getDataSet = function (key) {
            if (!key) {
                return;
            }
            fuzzyApi.getDataSet(key)
                .then(
                    (successResponse) => {
                        const responseBody = successResponse.data.dataSet;
                        comparisonCtrl.configurationsWithoutSets = responseBody.methods;
                        comparisonCtrl.rawFuzzySets = responseBody.rawSets;
                        comparisonCtrl.calculateResult();
                        console.log(successResponse);
                    },
                    (errorResponse) => {
                        console.log(errorResponse);
                    }
                );
        };

        this.configurations = this.createValidConfigurations();

        this.results = [];

        this.calculateResult = function () {
            this.configurations = this.createValidConfigurations();
            this.similarityCalculationResults = {};
            this.results = [];
        };

        $scope.$on('FUZZY_SIMILARITY_CALCULATED', function (event, data) {
            console.log('event: ' + data);
            comparisonCtrl.similarityCalculationResults[data.id] = data;
            const storedResults = Object.values(comparisonCtrl.similarityCalculationResults);
            const sortedResults = _.sortBy(storedResults, ['id']);
            const results = _.map(sortedResults, o => o.result.toFixed(2));
            const labels = _.map(sortedResults, o => o.method);
            comparisonCtrl.summaryChartConfig.data = results;
            comparisonCtrl.summaryChartConfig.labels = labels;
            console.log("labels: " + results.join(" & "));
            console.log("results: " + labels.join(" "));
        });

        $scope.$watch('comparisonCtrl.selectedDataSetKey', function (newValue) {
            comparisonCtrl.getDataSet(newValue);
            console.log(newValue);
        }, true);
    }]);

    app.controller("DrawChartController", ['$scope', 'arrayUtils', 'fuzzyApi', function ($scope, arrayUtils, fuzzyApi) {


        const _self = this;

        this.rawSetValues = "0 0 0 0 0 0 0 0.08333333333333337 0.16666666666666663 0.25 0.33333333333333337 0.41666666666666663 0.5 0.5833333333333333 0.6666666666666667 0.75 0.8333333333333333 0.9166666666666667 1 1 1 1 1 1 1 1 1 1.01";

        this.rawSets = [
            {
                setAsString: this.rawSetValues,
                label: 'Wysocy ludzie'
            }
        ];

        this.labels = "0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240";

        this.xAxisLabel = "Wzrost [cm]";

        this.yAxisLabel = "Stopień przynależności";

        this.chartConfig = {
            data: [
                []
            ],
            series: ["Set"],
            colors: [
                { // grey
                    fill: false,
                    backgroundColor: 'rgba(148,159,177,0.2)',
                    pointBackgroundColor: 'rgba(148,159,177,1)',
                    pointHoverBackgroundColor: 'rgba(148,159,177,1)',
                    borderColor: 'rgba(148,159,177,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(148,159,177,0.8)'
                },
                { // dark grey
                    fill: false,
                    backgroundColor: 'rgba(77,83,96,0.2)',
                    pointBackgroundColor: 'rgba(77,83,96,1)',
                    pointHoverBackgroundColor: 'rgba(77,83,96,1)',
                    borderColor: 'rgba(77,83,96,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(77,83,96,0.8)'
                },
                { // blue
                    fill: false,
                    backgroundColor: 'rgba(0, 0, 255,0.2)',
                    pointBackgroundColor: 'rgba(0, 0, 255,1)',
                    pointHoverBackgroundColor: 'rgba(0, 0, 255,1)',
                    borderColor: 'rgba(0, 0, 255,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0, 0, 255,0.8)'
                },
                { // dark green
                    fill: false,
                    backgroundColor: 'rgba(0,100,0,0.2)',
                    pointBackgroundColor: 'rgba(0,100,0,1)',
                    pointHoverBackgroundColor: 'rgba(0,100,0,1)',
                    borderColor: 'rgba(0,100,0,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0,100,0,0.8)'
                },
                { // dark blue
                    fill: false,
                    backgroundColor: 'rgba(0, 0, 139,0.2)',
                    pointBackgroundColor: 'rgba(0, 0, 139,1)',
                    pointHoverBackgroundColor: 'rgba(0, 0, 139,1)',
                    borderColor: 'rgba(0, 0, 139,1)',
                    pointBorderColor: '#fff',
                    pointHoverBorderColor: 'rgba(0, 0, 139,0.8)'
                },
            ],
            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            autoSkip: false
                        },
                        gridLines: {
                            drawOnChartArea: false
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Możliwe wartości atrybutu'
                        }
                    }],
                    yAxes: [{
                        gridLines: {
                            drawOnChartArea: false
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Możliwe wartości atrybutu'
                        }
                    }]
                },
                legend: {
                    display: true,
                    labels: {
                        fontColor: 'rgb(0, 0, 0)'
                    }
                },
                elements: {
                    line: {
                        borderWidth: 4
                    }
                }
            }
        };

        this.redrawChart = () => {
            const setValues = _.map(_self.rawSets, (rawSet) => arrayUtils.stringToArray(rawSet.setAsString));
            console.log("setValues: ");
            console.log(setValues);
            _self.chartConfig.data = setValues;
            _self.chartConfig.series = _.map(_self.rawSets, (rawSet) => rawSet.label);
            const labels = _self.labels.split(/\s+|,|;/);
            console.log("labels: ");
            console.log(labels);
            _self.chartConfig.labels = labels;

            _self.chartConfig.options.scales.xAxes[0].scaleLabel.labelString = _self.xAxisLabel;
            _self.chartConfig.options.scales.yAxes[0].scaleLabel.labelString = _self.yAxisLabel;
        };

        this.addSet = () => {
            _self.rawSets.push({
                setAsString: ''
            });
        }

        this.wysocy = () => {
            var labels = [];
            var values = [];
            for (var i = 0; i <= 240; i += 10) {
                labels.push(i);
                if (i <= 60) {
                    values.push(0);
                } else if (i >= 240) {
                    values.push(1);
                } else {
                    values.push(i / 120.0 - 0.5);
                }
            }
            console.log(labels);
            console.log(values);
        };
    }

    ]);


})(_);