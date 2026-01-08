import Nav from "./Nav/Nav";
import { useEffect } from "react";
import Spotlight from "./Pages/Home/Spotlight/Spotlight";
import Trending from "./Pages/Home/Trending/Trending";
import Search from "./Pages/Search/Search";

const Login: React.FC = () => {
    useEffect(() => {
        const getHome = async () => {
            const response = await fetch('http://127.0.0.1:8000/api/home/', {credentials: "include"})
            console.log(await response.text())
        }
        getHome();
    }, [])

    return <>
        <Nav/>
        <Search/>
        <Spotlight/>
        <Trending/>
    </>
}

export default Login;