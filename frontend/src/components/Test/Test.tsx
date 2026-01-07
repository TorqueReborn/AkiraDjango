
const Test = () => {

    const sendCookie = () => {
        const send = async () => {
            const response = await fetch('http://127.0.0.1:8000/api/home/', { credentials: "include" })
            console.log(await response.json())
        }
        send();
    }

    const createCookie = () => {

        const create = async () => {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                credentials: 'include', // important for cookies / session auth
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: 'ghost',
                    password: '12345678',
                }),
            });

            const data = await response.json();
            console.log(data);
        };
        create();
    }

    const login = () => {

        const testLogin = async () => {
            const response = await fetch('http://127.0.0.1:8000/test/login/', {
                method: 'POST',
                credentials: 'include', // important for cookies / session auth
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: 'ghost',
                    password: '12345678',
                }),
            });

            const data = await response.json();
            console.log(data);
        };
        testLogin();
    }

    return (
        <>
            <div>Test</div>
            <button onClick={sendCookie}>Send Cookie</button><br />
            <button onClick={createCookie}>Create Cookie</button> <br />
            <button onClick={login}>Login</button>
        </>
    )
}

export default Test