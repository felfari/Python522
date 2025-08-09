
const months = [
    "Январь", 
    "Февраль", 
    "Март", 
    "Апрель",
    "Май", 
    "Июнь", 
    "Июль", 
    "Август",
    "Сентябрь", 
    "Октябрь", 
    "Ноябрь", 
    "Декабрь"
];


function getRandomColor() {
    const r = Math.floor(Math.random() * 256); 
    const g = Math.floor(Math.random() * 256); 
    const b = Math.floor(Math.random() * 256); 
    return `rgb(${r}, ${g}, ${b})`;
}



for (let i = 0; i < months.length; i++) 
    {
    const color = getRandomColor(); 
    document.write(`
        <div style="background-color: ${color}; text-align: center; padding:18px;">
            ${months[i]}
        </div>`);
    }    