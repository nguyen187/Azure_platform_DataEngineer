// Lấy các phần tử cần thao tác
const homeLink = document.getElementById("home-link");
const loadLink = document.getElementById("load-link");
const dash1Link = document.getElementById("dashboard1-link");
const dash2Link = document.getElementById("dashboard2-link");
const submitlink = document.getElementById("submit-link");
const case1link = document.getElementById("case1-link");
const case2link = document.getElementById("case2-link");
const case3link = document.getElementById("case3-link");
const case4link = document.getElementById("case4-link");
const case5link = document.getElementById("case5-link");
const case6link = document.getElementById("case6-link");



const homeSection = document.getElementById("home");
const dashboardSection = document.getElementById("load");
const mlappSection = document.getElementById("dashboard1");
const photoSection = document.getElementById("dashboard2");
const case1 = document.getElementById("case1");
const case2 = document.getElementById("case2");
const case3 = document.getElementById("case3");
const case4 = document.getElementById("case4");
const case5 = document.getElementById("case5");
const case6 = document.getElementById("case6");




const processbar = document.getElementById('processbar');


// Ẩn tất cả các phần nội dung trừ phần Home
dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";



processbar.style.display = "none";
// // Thêm sự kiện click cho các link
// homeLink.addEventListener("click", function(e) {
//   e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
//   homeSection.style.display = "block";
//   dashboardSection.style.display = "none";
//   mlappSection.style.display = "none";
//   photoSection.style.display = "none";

// });

// dashboardLink.addEventListener("click", function(e) {
//   e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
//   homeSection.style.display = "none";
//   dashboardSection.style.display = "block";
//   mlappSection.style.display = "none";
//   photoSection.style.display = "none";

// });

// mlappLink.addEventListener("click", function(e) {
//   e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
//   homeSection.style.display = "none";
//   dashboardSection.style.display = "none";
//   mlappSection.style.display = "block";
//   photoSection.style.display = "none";

// });
// photoLink.addEventListener("click", function(e) {
//     e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
//     homeSection.style.display = "none";
//     dashboardSection.style.display = "none";
//     photoSection.style.display = "block";
//     mlappSection.style.display = "none";
    
  
//   });

// // Lấy tham chiếu đến form
// const form = document.getElementById('load-form');

// // Thêm sự kiện submit cho form
// form.addEventListener('submit', function(e) {
//   e.preventDefault(); // Ngăn chặn gửi yêu cầu mặc định

//   // Thực hiện xử lý dữ liệu form
//   // Ví dụ: Kiểm tra dữ liệu hợp lệ, tạo đối tượng FormData, vv.

//   // Tạo đối tượng FormData từ form
//   const formData = new FormData(form);

//   // Gửi yêu cầu AJAX
//   fetch('/Load', {
//     method: 'POST',
//     body: formData
//   })
//   .then(function(response) {
//     // Xử lý kết quả trả về từ Flask (response)
//     // Ví dụ: Hiển thị thông báo thành công
//     alert('Yêu cầu đã được gửi thành công!');
//     // Lấy tham chiếu đến phần tử <p>
//     const alertMessage = document.getElementById('alert-message');

//     // Cập nhật nội dung của phần tử <p> bằng giá trị của biến alert1
//     alertMessage.innerHTML = '<div style="color: red;">File upload Existed</div>';

//     // Tùy chỉnh các hành động sau khi gửi yêu cầu thành công
//     // Ví dụ: Cập nhật giao diện, chuyển hướng trang, vv.
//   })
//   .catch(function(error) {
//     // Xử lý lỗi trong quá trình gửi yêu cầu
//     // Ví dụ: Hiển thị thông báo lỗi
//     alert('Đã xảy ra lỗi khi gửi yêu cầu!');
//   });
// });

// Lấy tham chiếu đến form và phần tử <p> để hiển thị phản hồi
const form = document.getElementById('load-form');
const responseMessage = document.getElementById('alert-message');
const cusIdInput = document.querySelector('input[name="CusID"]');
const proIdInput = document.querySelector('input[name="ProID"]');
const batchIdInput = document.querySelector('input[name="BatchID"]');
// Đặt sự kiện submit cho form
form.addEventListener('submit', function(e) {
  e.preventDefault(); // Ngăn chặn hành vi mặc định khi submit form
//  show process bar
    
  var alertMessage = '<div style="color: red;"></div>';
  responseMessage.innerHTML = alertMessage;
  // Tạo đối tượng FormData từ form
  const formData = new FormData(form);
  // Kiểm tra các trường input
  if (cusIdInput.value.trim() === "" || proIdInput.value.trim() === "" || batchIdInput.value.trim() === "") {
    responseMessage.innerHTML = '<div style="color: red;">Vui lòng điền đầy đủ thông tin</div>';
    return; // Dừng tiếp tục xử lý và hiển thị thông báo lỗi
  }
  // Xử lý sự kiện input trên trường BatchID
  
  const inputValue = batchIdInput.value.trim();

  // Kiểm tra giá trị nhập vào bằng biểu thức chính quy chỉ cho phép số
  if (!/^\d*$/.test(inputValue)) {
    responseMessage.innerHTML = '<div style="color: red;">BatchID chỉ nhận giá trị số</div>'; // Xóa các ký tự không phải số
    return
  }
  processbar.style.animation = 'none'; // Reset animation
  processbar.offsetWidth; // Trigger reflow
  processbar.style.animation = 'progressAnimationStrike 6s';
  processbar.style.display = 'block';

  // Gửi yêu cầu POST đến máy chủ Flask
  fetch('/Load', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    // Xử lý phản hồi từ máy chủ Flask
    if (response.ok) {
      return response.text();
      // response.text().then(function (data) {
      //   alert(data)

      //   // var alertMessage = '<div style="color: red;">' + data + '</div>';
      // //  responseMessage.innerHTML = alertMessage;
      // }); // Trả về nội dung phản hồi dưới dạng văn bản
    } else {
      throw new Error('Error: ' + response.status);
    }
  })
  .then(function(data) {
    // Xử lý dữ liệu phản hồi

    // alert(data)
    
    if (data.match("OK")) {
      // alert('cccc')
      // alert("File uploaded successfully")
      responseMessage.innerHTML = '<div style="color: green;">File uploaded successfully</div>'; // Hiển thị phản hồi trong phần tử <p>
    // Thêm sự kiện click cho các link
 
  } else {
  var alertMessage = '<div style="color: red;">File upload Existed</div>';
  responseMessage.innerHTML = alertMessage;

  // alert("File upload Existed!")
  }
})
  .catch(function(error) {
    console.log(error);
    alert('An error occurred during the request.');
    var alertMessage = '<div style="color: red;">An error occurred during the request.</div>';
    responseMessage.innerHTML = alertMessage;
  });
});


const loginMessage = document.getElementById('login-message');
const loginMain = document.getElementById("login-main");

const userinput = document.querySelector('input[name="user"]');
const passinput = document.querySelector('input[name="pass"]');
const loginform = document.getElementById('login-form');
loginform.addEventListener('submit', function(e) {
  e.preventDefault(); // Ngăn chặn hành vi mặc định khi submit form

  // Tạo đối tượng FormData từ form
  const formData = new FormData(loginform);
  // Kiểm tra các trường input
  if (userinput.value.trim() === "" || passinput.value.trim() === "" ) {
    loginMessage.innerHTML = '<div style="color: red;">Vui lòng điền đầy đủ thông tin</div>';
    return; // Dừng tiếp tục xử lý và hiển thị thông báo lỗi
  }
  
  // Gửi yêu cầu POST đến máy chủ Flask
  fetch('/Login', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    // Xử lý phản hồi từ máy chủ Flask
    if (response.ok) {
    // if (true) {
      
      return response.text();
      // response.text().then(function (data) {
      //   alert(data)

      //   // var alertMessage = '<div style="color: red;">' + data + '</div>';
      // //  responseMessage.innerHTML = alertMessage;
      // }); // Trả về nội dung phản hồi dưới dạng văn bản
    } else {
      throw new Error('Error: ' + response.status);
    }
  })
  .then(function(data) {
    // alert(data.match("correct"))
    if (data.match("correct")) {
    // if (true) {
      // alert('cccc')

      loginMain.innerHTML = '<div style="color: green;"><h2>Demo Digital Platform</h2></div>'; // Hiển thị phản hồi trong phần tử <p>
    // Thêm sự kiện click cho các link
homeLink.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "block";

});

loadLink.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "block";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";


});

dash1Link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "block";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";

});
case1link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "block";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";


});
case2link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "block";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";


});
case3link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "block";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";


});
case4link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "block";
case5.style.display = "none";
case6.style.display = "none";
homeSection.style.display = "none";


});
case5link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "block";
case6.style.display = "none";
homeSection.style.display = "none";


});
case6link.addEventListener("click", function(e) {
  e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
  dashboardSection.style.display = "none";
mlappSection.style.display = "none";
photoSection.style.display = "none";
case1.style.display = "none";
case2.style.display = "none";
case3.style.display = "none";
case4.style.display = "none";
case5.style.display = "none";
case6.style.display = "block";
homeSection.style.display = "none";


});



// dash2Link.addEventListener("click", function(e) {
//     e.preventDefault(); // Ngăn chặn trình duyệt đi đến URL trong href
//     dashboardSection.style.display = "none";
// mlappSection.style.display = "none";
// photoSection.style.display = "block";
// case1.style.display = "none";
// case2.style.display = "none";
// case3.style.display = "none";
// case4.style.display = "none";
// case5.style.display = "none";
// case6.style.display = "none";
// homeSection.style.display = "none";
    
  
//   });
    } else {
      var alertMessage = '<div style="color: red;">User name or password incorrect.</div>';
      loginMessage.innerHTML = alertMessage;
    }
  })
  .catch(function(error) {
    console.log(error);
    alert('An error occurred during the request.');
  });
});





// Lấy tham chiếu đến form và phần tử <p> để hiển thị phản hồi
const formloadfile = document.getElementById('loadfile-form');
const listfile = document.getElementById('file-list');

// Đặt sự kiện submit cho form
formloadfile.addEventListener('submit', function(e) {
  e.preventDefault(); // Ngăn chặn hành vi mặc định khi submit form

  // Tạo đối tượng FormData từ form
  const formfile = new FormData(formloadfile);
  
  // Gửi yêu cầu POST đến máy chủ Flask
  fetch('/LoadFile', {
    method: 'POST',
    body: formfile
  })
  .then(function(response) {
    // Xử lý phản hồi từ máy chủ Flask
    if (response.ok) {
      return response.json();
      // response.text().then(function (data) {
      //   alert(data)

      //   // var alertMessage = '<div style="color: red;">' + data + '</div>';
      // //  responseMessage.innerHTML = alertMessage;
      // }); // Trả về nội dung phản hồi dưới dạng văn bản
    } else {
      throw new Error('Error: ' + response.status);
    }
  })
  .then(function(data) {
    // Xử lý dữ liệu phản hồi

    // alert(data)
    // // const fileListElement = document.getElementById('file-list');
    // for (let i = 0; i < data.length; i++) {
    //   const filename = data[i];
    //   alert(filename);
    // }
//     // / Xử lý phản hồi từ Flask
    const fileList = document.getElementById('file-list');
    fileList.innerHTML = '';
    data.forEach(filename => {
      const listItem = document.createElement('li');
      listItem.textContent = filename;
      fileList.appendChild(listItem);
})
  })
  .catch(function(error) {
    console.log(error);
    alert('An error occurred during the request.');
  });
});
