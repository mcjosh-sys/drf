const baseEndpoint = "http://localhost:8000/api";
const loginForm = document.getElementById("login-form");
if (loginForm) {
  loginForm.addEventListener("submit", handleLogin);
}
function handleLogin(e) {
  e.preventDefault();
  const loginEndpoint = `${baseEndpoint}/token/`;
  const loginFormData = new FormData(loginForm);
  const loginObjectData = Object.fromEntries(loginFormData);
  const options = {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify(loginObjectData),
  };
  fetch(loginEndpoint, options)
    .then((res) => {
      console.log(res);
      return res.json();
    })
    .then(handleAuthData)
      .catch(err => {
        console.log({ err: err.message });
    })
}

function handleAuthData(authData) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.access)
}
