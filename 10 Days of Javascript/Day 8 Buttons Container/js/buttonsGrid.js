var b=document.getElementById('btn5');
var arr=[1,2,3,6,9,8,7,4];
var btns_o = [1,2,3,6,9,8,7,4];
b.onclick=function()
{
arr.unshift(arr.pop());
for (let i = 0; i < 8;++i){
    document.getElementById('btn'+String(btns_o[i])).innerHTML = arr[i];
}


}
