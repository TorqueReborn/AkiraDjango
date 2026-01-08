import React, {useState} from "react";

const Login: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();
    const response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/api/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password
      }),
      credentials: "include",
    })
    console.log(await response.text())
  }
  return (
    <div className="bg-white text-black">
      <form onSubmit={handleSubmit}>
        <input type="text" value={username} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setUsername(e.target.value)} placeholder="Username"/>
        <input type="password" value={password} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)} placeholder="Password"/>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default Login