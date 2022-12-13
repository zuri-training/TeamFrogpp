var a;
 function passIcon() {
     if (a==1){
        document.getElementById("text").type ="password";
        document.getElementById("pass").src ="images/eye-off.svg";
  a=0     
    }
   else {
       document.getElementById("text").type ="text";
       document.getElementById("pass").src ="images/eye-on.svg";
       a=1;
  }
 }

var b;
 function passIcon1() {
     if (b==1){
        document.getElementById("text1").type ="password";
        document.getElementById("pass1").src ="images/eye-off.svg";
     b=0  
    }
   else {
       document.getElementById("text1").type ="text";
       document.getElementById("pass1").src ="images/eye-on.svg";
       b=1;
  }
 }

var c;
 function sideBar() {
     if (c==1){
            document.getElementById("sidebar").style.display="none";
   c=0;    
    }
   else {
       document.getElementById("sidebar").style.display="block";
       c=1;
  }
 }


var d;
 function menuBar() {
     if (d==1){
            document.getElementById("menuBar").style.display="none";
   d=0;    
    }
   else {
       document.getElementById("sidebar").style.display="block";
       d=1;
  }
 }
