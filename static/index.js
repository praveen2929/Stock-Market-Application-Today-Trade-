function sendMail() {
  var fullName= document.getElementById("fullName").value
  var email_id= document.getElementById("email_id").value
  var number= document.getElementById("number").value
  var message= document.getElementById("message").value

  if(fullName=="" || email_id == "" || number=="" ||message == ""){
    var w=document.getElementById("wrong");
      w.innerHTML= "Please Fill The Details First"
  }else{
    var params = {
      fullName: fullName,
      email_id: email_id,
      number: number,
      message: message,
    };
 
  emailjs
    .send("service_auf1vf6", "template_q2t2q7r", params)
    .then(function (res) {
      alert("send success!");
    });
}
function Course() {
  var fullName= document.getElementById("fullName").value
  var email_id= document.getElementById("email_id").value
  var number= document.getElementById("number").value
  var message= document.getElementById("address").value
  var course= document.getElementById("course").value
  if(fullName=="" || email_id == "" || number=="" ||course == "" || message==""){
    var w=document.getElementById("wrong");
      w.innerHTML= "Please Fill The Details First"
  }else{
    var params = {
      fullName: fullName,
      email_id: email_id,
      number: number,
      address: message,
      course: course,
    };
   
    emailjs
      .send("service_auf1vf6", "template_f75wnsg", params)
      .then(function (res) {
        alert("send success!");
      });
  }
  
}
}

