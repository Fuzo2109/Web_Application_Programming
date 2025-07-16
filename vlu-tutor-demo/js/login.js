// Demo users
const demoUsers = {
  'student@vlu.edu.vn': { password: '123456', redirect: 'learner.html' },
  'tutor@vlu.edu.vn':   { password: '123456', redirect: 'tutor.html' },
  'center@vlu.edu.vn':  { password: '123456', redirect: 'center.html' },
  'admin@vlu.edu.vn':   { password: '123456', redirect: 'admin.html' }
};

function quickLogin(email, password) {
  document.getElementById('email').value = email;
  document.getElementById('password').value = password;
  document.getElementById('loginForm').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}));
}

document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  if (demoUsers[email] && demoUsers[email].password === password) {
    window.location.href = demoUsers[email].redirect;
  } else {
    alert('Invalid email or password!');
  }
}); 