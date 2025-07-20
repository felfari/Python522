document.writeln("<div id='divSample'></div>");
let div = document.querySelector("#divSample");
div.innerHTML=`
Термоста́т — прибор для поддержания постоянной температуры. Поддержание температуры
обеспечивается либо за счёт использования терморегуляторов, либо осуществлением фазового
перехода (например, таяние льда). 
Для уменьшения потерь тепла или холода термостаты, как
правило, теплоизолируют. 
Но не всегда. Широко известны автомобильные моторы, где летом нет
никакой теплоизоляции и за счёт действия восковых термостатов поддерживается постоянная
температура. Другим примером термостата, широко используемого в быту, является холодильник

`
div.style.background="#ffff00";
div.style.color="#060606";
div.style.width= "256px";
div.style.height= "256px";
div.style.overflow="scroll";
div.style.outline="1px dashed red"

div.className = "resetFont";
let res = document.querySelector(".resetFont");
res.style.fontSize="20pt";
res.style.fontWeight="400";
res.style.textDecoration='underline';

