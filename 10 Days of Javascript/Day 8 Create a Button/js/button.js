var b = document.createElement('button');
b.id = 'btn';
b.innerHTML = '0';
b.addEventListener("click", function(){let p = parseInt(b.innerHTML);
                                       b.innerHTML = String(p+1)});
document.body.appendChild(b);
