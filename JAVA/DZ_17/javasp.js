  
        document.querySelectorAll('.close').forEach(button => {
            button.addEventListener('click', function() {
                const block = this.closest('.block');
                block.classList.add('hidden');
            });
        });