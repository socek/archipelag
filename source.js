var password = document.getElementById('password')
var submit = document.getElementById('submit')

var token = 0
var userLogin = 0;

submit.onclick = function(){
    if ( password.value == 0 || password.value < 6) {
        console.log('send data')
        const token = Math.floor((Math.random() * 100000000000) + 1);
        localStorage.setItem('id_token', token)
        localStorage.getItem('id_token')
    }
}


