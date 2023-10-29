try {
    const messages = document.querySelector('.messages').querySelectorAll('.message')

    messages.forEach(message => {
        setTimeout(() => {
            message.remove()
        }, 10000)
    })
} catch {
    console.log('')
}

function setValue() {
	var rangeValue = document.getElementById('avarge-ticet-ulgowy-price').value;
    var textValue = document.getElementById('range-value1');
    textValue.setValue = rangeValue
}