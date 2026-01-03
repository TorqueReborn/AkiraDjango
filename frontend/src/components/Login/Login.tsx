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

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            username: formData.username,
            password: formData.password,
            }),
        });

        if (!response.ok) {
            throw new Error("Login failed");
        }

        console.log(await response.json());
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
    </form>
  );
}


export default Login;