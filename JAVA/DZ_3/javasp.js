
let sum = +prompt("Введите стоимость покупки:");
    let sale;
    if (sum > 1000) sale = 5;
    else if (sum > 500) sale = 3;
    else sale = 0;

    let discount = sum * sale / 100;
    let total = sum - discount;

alert(`Сумма: ${sum} руб.\nСкидка: ${sale}% (${discount} руб.)\nИтого: ${total} руб.`);
   