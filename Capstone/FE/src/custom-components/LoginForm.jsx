import { useState } from "react";
import { useAuthInfo } from "../context/AuthContext";

export default function LoginForm() {
  // const { login } = useAuthInfo();

  const [loginCreds, setLoginCreds] = useState({
    email: "",
    password: "",
  });

  const handleFieldUpdate = (e) => {
    const { name, value } = e.target;

    setLoginCreds((previous) => ({ ...previous, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("you submitted correctly, now wire it up to your BE!!");
  };

  return (
    <div className="login-form-wrapper">
      login form
      <form onSubmit={handleSubmit}>
        <div className="email-wrapper">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            value={loginCreds.email}
            type="text"
            className="email-field"
            onChange={handleFieldUpdate}
          />
        </div>
        <div className="password-wrapper">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            name="password"
            value={loginCreds.password}
            type="password"
            className="password-field"
            onChange={handleFieldUpdate}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
