 function swapImages() {
            const from = parseInt(document.getElementById('from').value);
            const to = parseInt(document.getElementById('to').value);

            
            if (isNaN(from) || isNaN(to) || from < 1 || from > 3 || to < 1 || to > 3) {
                alert("Введите корректные номера (1, 2 или 3)");
                return;
            }

    
            const imgFrom = document.getElementById(`img${from}`);
            const imgTo = document.getElementById(`img${to}`);

           
            if (imgFrom && imgTo) {
                const temp = imgFrom.innerHTML;
                imgFrom.innerHTML = imgTo.innerHTML;
                imgTo.innerHTML = temp;
            }
        }