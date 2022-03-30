  function valor1(num1, palo1, palo2, palo3){
    if ((palo1 === palo2) || (palo1 === palo3)){
      if (num1 <= 7){
    return num1; 
    } else if (num1 <= 12){
    return 0;
    }
    }
  }

    
  function valor2(num1, palo1, palo2, palo3){
    if ((palo2 === palo1) || (palo2 === palo3)){
      if (num1 <= 7){
    return num1; 
    } else if (num1 <= 12){
    return 0;
  }
  }
 }
  
    function valor3(num1, palo1, palo2, palo3){
    if ((palo3 === palo1) || (palo3 === palo2)){
      if (num1 <= 7){
    return num1; 
    } else if (num1 <= 12){
    return 0;
  }
  }
 }
      
function puntaje (num1, palo1, num2, palo2, num3, palo3){
  
 if ((palo1 === palo2) && (palo2 === palo3)){
    if ((num1 > num3) && (num2 > num3)){
      return valor1(num1) + valor2(num2) + 20;
    }  else if ((num1 > num2) && (num3 > num2)){
      return valor1(num1) + valor3(num3) + 20;
    } else {
      return valor2(num2) + valor3(num3) +20;
    }
 }
  
 else if (palo1 === palo2){
      return valor1(num1) + valor2(num2) + 20;
  }
  
 else if (palo1 === palo3){
      return valor1(num1) + valor3(num3) + 20;
 } 
 else if (palo2 === palo3){
      return valor2(num2) + valor3(num3) + 20;
 }
  
 else if ((palo1 !== palo2) && (palo2 !== palo3)){
   return Math.max(valor1(num1), valor2(num2), valor3(num3));
   }
  
 }
