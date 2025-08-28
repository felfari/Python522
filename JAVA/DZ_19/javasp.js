 function selectOption() {
            
            const radioButtons = document.getElementsByName('choice');
            
            let selectedValue = null;
            for (let i = 0; i < radioButtons.length; i++)
                 {
                if (radioButtons[i].checked) {
                    selectedValue = radioButtons[i].value;
                    break;}
                }
            
            if (selectedValue) {
                alert("Выбран: " + selectedValue);}
                 else {
                alert("Пожалуйста, выберите один из вариантов.");
            }}