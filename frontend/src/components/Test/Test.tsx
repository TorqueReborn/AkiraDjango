import React, { useEffect } from 'react'

const Test = () => {
    useEffect(() => {

    }, [])

    const setCookie = () => {
        const setCookie = async () => {
            const response = await fetch('http://127.0.0.1:8000/test/set_cookie/', { credentials: "include" })
            console.log(await response.json())
        }
        setCookie();
    }

    return (
        <>
            <div>Test</div>
            <button onClick={setCookie}>Set Cookie</button>
        </>
    )
}

export default Test