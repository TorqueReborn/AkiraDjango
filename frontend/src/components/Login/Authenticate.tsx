import { useState } from "react";
import type { AuthData } from "../../types/auth";

const Authenticate = () => {
    const [formData, setFormData] = useState<AuthData>({
        username: '',
        password: ''
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const register = async () => {
        const response = await fetch('http://127.0.0.1:8000/api/register/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: formData.username,
                password: formData.password,
            })
        })
        console.log(await response.json())
    }

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
            })
        })
        console.log(await response.json())
    }

    return (
        <div className="flex items-center justify-center h-screen">
            <form className="bg-slate-600 flex flex-col" onSubmit={handleSubmit}>
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
                <button onClick={register}>Register</button>
            </form>
        </div>
    );
}


export default Authenticate;