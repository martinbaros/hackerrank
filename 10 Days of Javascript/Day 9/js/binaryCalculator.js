var res = document.getElementById('res')

document.getElementById('btn0').onclick = () => {
  res.innerHTML += '0';
}

document.getElementById('btn1').onclick = () => {
  res.innerHTML += '1';
}

document.getElementById('btnClr').onclick = () => {
  res.innerHTML = '';
}
document.getElementById('btnSum').onclick = () => {
  res.innerHTML += '+';
}

document.getElementById('btnSub').onclick = () => {
  res.innerHTML += '-';
}

document.getElementById('btnMul').onclick = () => {
  res.innerHTML += '*';
}

document.getElementById('btnDiv').onclick = () => {
  res.innerHTML += '/';
}

document.getElementById('btnEql').onclick = () => {
  let h = res.innerHTML;
  h = h.split(/(\+|-|\*|\/)/);
  let c1 = parseInt(h[0], 2);
  let c2 = parseInt(h[2], 2);
  let z = h[1];
  let result = 0;

  switch (z){
    case "+":
      result = c1 + c2;
      break;
    case "-":
      result = c1 - c2;
      break;
    case "*":
      result = c1 * c2;
      break;
    case "/":
      result = c1 / c2;
      break;
  }

  res.innerHTML = result.toString(2);
}
