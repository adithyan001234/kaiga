function sign(){
    name1=document.getElementById('name1').value
    email=document.getElementById('email').value
    password=document.getElementById('password').value
    cpassword=document.getElementById('cpassword').value
    if(name1==""||email==""||password==""||cpassword==""){
        document.getElementById('message').innerHTML="enter detail"
        return false
    
    }
    else if(password==cpassword){
        document.getElementById('message').innerHTML="match"
        return true
    
    }
    else{
        document.getElementById('message').innerHTML='password not match'
        return false
    }
}