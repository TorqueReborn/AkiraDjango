import { useState } from "react";
import type { LoginFormData } from "./Login.types";

const Login = () => {
    const [formData, setFormData] = useState<LoginFormData>({
        username: '',
        password: ''
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleClick = async (e: React.FormEvent) => {
        e.preventDefault();
        let response = await fetch('http://127.0.0.1:8000/api/refresh/', {
            method: "POST",
            credentials: "include",
        });

        if (!response.ok) {
            throw new Error("Login failed");
        }

        console.log(await response.json());
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await fetch('http://127.0.0.1:8000/api/login/', {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            username: formData.username,
            password: formData.password,
            }),
            credentials: "include",
        }).then(response => response.json())
        .then(data => {
            const accessToken = data.access_token;
            localStorage.setItem('access_token', accessToken);
        });;
    }

    return (
    <form className="login-card" onSubmit={handleSubmit}>
    <h2>Login</h2>

    <input
        type="username"
        name="username"
        placeholder="Username"
        value={formData.username}
        onChange={handleChange}
        required
    />

    <input
        type="password"
        name="password"
        placeholder="Password"
        value={formData.password}
        onChange={handleChange}
        required
    />

    <button type="submit">Login</button>
    <button onClick={handleClick}>Refresh</button>
    </form>
  );
}


export default Login;