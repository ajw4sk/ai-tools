function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    const resultDiv = document.getElementById('result');
    
    // Validate inputs
    if (isNaN(num1) || isNaN(num2)) {
        resultDiv.innerHTML = '<span style="color: red;">Please enter valid numbers</span>';
        return;
    }
    
    let result;
    
    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            if (num2 === 0) {
                resultDiv.innerHTML = '<span style="color: red;">Cannot divide by zero!</span>';
                return;
            }
            result = num1 / num2;
            break;
        default:
            resultDiv.innerHTML = '<span style="color: red;">Invalid operation</span>';
            return;
    }
    
    // Format result
    const formattedResult = Number.isInteger(result) ? result : result.toFixed(2);
    resultDiv.innerHTML = `<span style="color: #28a745;">Result: ${formattedResult}</span>`;
}

// Add keyboard support
document.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        calculate();
    }
});

// Initialize with a welcome message
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('result').innerHTML = '<span style="color: #6c757d;">Enter numbers and click Calculate</span>';
});